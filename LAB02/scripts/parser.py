import argparse
from go2websocket import Go2WebSocket
from modules import Display

class CLIParser:

    @staticmethod
    def take_input():
        parser = argparse.ArgumentParser()

        parser.add_argument(
            "-u",
            "--url",
            dest="input_url",
            default=None
        )

        parser.add_argument(
            "-s",
            "--search",
            dest="search_term",
            default=None
        )

        args = parser.parse_args()

        if args.input_url is not None:
            return "URL", args.input_url
        else:
            return "Search", args.search_term


if __name__ == '__main__':

    r, msg = CLIParser.take_input()

    if r == "URL":
        res = Go2WebSocket.request_url(msg)
        Display.display_site(res)
    else:
        res = Go2WebSocket.search_term(msg)
        Display.process_data(res)
