from colorama import Fore, Back, Style


class Hello:

    def __init__(self, text_wth_bg, colored_text, styled_text):
        self.text_wth_bg = text_wth_bg

        self.colored_text = colored_text

        self.styled_text = styled_text

    def Hello(self):
        print(Style.DIM + self.styled_text)

        print(Back.MAGENTA + self.text_wth_bg)

        print(Back.RESET + Fore.LIGHTYELLOW_EX + self.colored_text)


hello = Hello("Hello (with color bg)","Hello(colored text)", "Hello(styled text)")

hello.Hello()