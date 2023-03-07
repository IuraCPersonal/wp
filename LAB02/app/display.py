from colorama import Fore, Style


class Display:

    def begin():
        print("#---------------------- Page ----------------------#")
        print()

    def end():
        print()
        print("#---------------------- End -----------------------#")

    def ul(list):
        Display.begin()

        for index, link in enumerate(list):
            print(f"[{Fore.RED}{index}{Style.RESET_ALL}] {link}")

        Display.end()
