import re
import ssl
import json
import socket

from bs4 import BeautifulSoup
from colorama import Fore, Style
from urllib.parse import urlparse

from app.cache import Cache
from app.modules import API_KEY
from app.display import Display


class Parser:
    def parse_url(url: str) -> list:
        pass

    def parse_terms(terms: str) -> str:
        pass

    def parse_html(r) -> str:
        pass

    def parse_links(r) -> list:
        pass


class URLParser(Parser):
    def parse_url(url):
        # Following the syntax specifications in RFC 1808, urlparse recognizes a netloc only if it is properly introduced by ‘//’.
        o = urlparse("//" + url.replace("https",
                     "").replace("://", ""))

        return [o.hostname, o.path]


class HTMLParser(Parser):
    def parse_html(r) -> str:
        soup = BeautifulSoup(r.decode(), "html.parser")
        body = soup.get_text().strip()

        print(body.encode("utf-8"))


class LinksParser(Parser):
    def parse_links(r) -> list:
        data = r.decode().replace("\n", "").replace("\r", "")
        match = re.findall(r"{.+[:,].+}|\[.+[,:].+\]", data)
        items = json.loads(match[0])["items"] if match else None
        links = [link["formattedUrl"] for link in items]

        return links


class Go2WebSocket:

    def request_url(url):
        hostname, path = URLParser.parse_url(url)

        print(
            f"[{Fore.CYAN}go2web{Style.RESET_ALL}] Trying to connect to ** {hostname} **")
        context = ssl.create_default_context()

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                ssock.connect((hostname, 443))

                print(
                    f"[{Fore.CYAN}go2web{Style.RESET_ALL}] SSL Protocol Version: {ssock.version()}")

                # Creating the request.
                request = f"GET {path if path is not None else '/'} HTTP/1.1\r\nHost:{hostname}\r\nConnection: close\r\n\r\n"

                # Send data to the socket.
                ssock.send(request.encode())
                ssock.settimeout(10)

                response = b""

                try:
                    while True:
                        data = ssock.recv(4096)
                        response = response + data

                        if not data:
                            break

                        # Check for HTTP redirect status codes (301, 302, 303, 307, 308)
                        if response.startswith(b"HTTP/1.1 301") or response.startswith(b"HTTP/1.1 302") or response.startswith(b"HTTP/1.1 303") or response.startswith(b"HTTP/1.1 307") or response.startswith(b"HTTP/1.1 308"):
                            # Extract the redirect location from the response headers
                            redirect_location = re.search(
                                b"Location: (.+?)\r\n", response).group(1)

                            redirect_link = hostname + \
                                redirect_location.decode("utf-8")

                            # Follow the redirect by making a new request to the new location
                            return Go2WebSocket.request_url(redirect_link)

                        if response.endswith(b"\r\n0\r\n\r\n"):
                            break
                except socket.timeout as e:
                    print(
                        "[{Fore.CYAN}go2web{Style.RESET_ALL}] Exception Raised: TimeoutError")

                return response

    def search_term(term):
        hostname = "www.googleapis.com"
        path = f"/customsearch/v1?key={API_KEY}&cx=f2ff5f215d5484786&q={term}"
        request = f"GET {path} HTTP/1.1\r\nHost:{hostname}\r\nConnection: close\r\n\r\n"
        context = ssl.create_default_context()

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

            print(
                f"[{Fore.CYAN}go2web{Style.RESET_ALL}] Trying to connect to ** {hostname} **")

            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                ssock.connect((hostname, 443))

                print(
                    f"[{Fore.CYAN}go2web{Style.RESET_ALL}] SSL Protocol Version: {ssock.version()}")
                print(f"[{Fore.CYAN}go2web{Style.RESET_ALL}] Searchin for {term}")

                ssock.send(request.encode())
                ssock.settimeout(10)

                response = b""

                try:
                    while True:
                        data = ssock.recv(4096)
                        response = response + data

                        if not data or response.endswith(b"\r\n0\r\n\r\n"):
                            break
                except socket.timeout as e:
                    print(
                        "[{Fore.CYAN}go2web{Style.RESET_ALL}] Exception Raised: TimeoutError")

                return response


class Go2Web(Go2WebSocket, Parser):
    def start(arg, msg):
        cache = Cache()

        if arg == "URL":
            r = Go2WebSocket.request_url(msg)
            HTMLParser.parse_html(r)

        elif arg == "Search":
            r = Go2WebSocket.search_term(msg)
            links = LinksParser.parse_links(r)
            Display.ul(links)

            while True:
                user_input = input(f"[{Fore.RED}go2web{Style.RESET_ALL}] >_ ")

                if user_input == 'll':
                    Display.ul(links)
                    continue

                if user_input == 'exit':
                    exit()

                if user_input in "0123456789" and len(user_input) == 1:
                    target_url = links[int(user_input)]
                    r = Go2WebSocket.request_url(target_url)
                    cache.add_url(r)
                    HTMLParser.parse_html(r)

                if user_input == 'forward':
                    r = cache.forward()
                    HTMLParser.parse_html(r)

                if user_input == 'back':
                    r = cache.back()
                    HTMLParser.parse_html(r)
