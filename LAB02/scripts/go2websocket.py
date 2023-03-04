import ssl
import socket
from colorama import Fore, Style
from urllib.parse import urlparse


class URLParser:
    def parse_url(url):
        # Following the syntax specifications in RFC 1808, urlparse recognizes a netloc only if it is properly introduced by ‘//’.
        o = urlparse("//" + url.replace("https", "").replace("http", "").replace("://", ""))

        return [o.hostname, o.path]
            

class Go2WebSocket:
    
    def request_url(url):
        hostname, path = URLParser.parse_url(url)

        print(f"[go2web] Trying to connect to ** {hostname} **")
        context = ssl.create_default_context()

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                ssock.connect((hostname, 443))    

                print(f"[go2web] SSL Protocol Version: {ssock.version()}")

                # Creating the request.
                request = f"GET {path if path is not None else '/'} HTTP/1.1\r\nHost:{hostname}\r\nConnection: close\r\n\r\n"
                print(request)
                # Send data to the socket.
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
                    print("[{Fore.CYAN}go2web{Style.RESET_ALL}] Exception Raised: TimeoutError")

                return response


    def search_term(term):
        API_KEY = "AIzaSyBLdMXvxPlqmiQ7GETElC_wO_hJplSR-dA"
        hostname = "www.googleapis.com"
        path = f"/customsearch/v1?key={API_KEY}&cx=f2ff5f215d5484786&q={term}"
        request = f"GET {path} HTTP/1.1\r\nHost:{hostname}\r\nConnection: close\r\n\r\n"
        context = ssl.create_default_context()

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

            print(f"[{Fore.CYAN}go2web{Style.RESET_ALL}] Trying to connect to ** {hostname} **")
            
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                ssock.connect((hostname, 443))

                print(f"[{Fore.CYAN}go2web{Style.RESET_ALL}] SSL Protocol Version: {ssock.version()}")
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
                    print("[go2web] Exception Raised: TimeoutError")


                return response
