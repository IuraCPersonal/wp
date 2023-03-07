import argparse

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
