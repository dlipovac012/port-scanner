import sys
import re


class Cli:
    def __init__(self, arguments) -> None:
        self.options = {}
        for (option, value) in zip(arguments[0::2], arguments[1::2]):
            self.options[option[1:]] = value

    def get_host(self):
        """ """
        if "h" not in self.options.keys():
            sys.exit("host [-h] is not provided")
        if not re.fullmatch(
            re.compile(r"^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$"),
            self.options["h"],
        ):
            sys.exit("host [-h] format is not valid")
        return self.options["h"]

    def get_port(self):
        """ """
        if "p" not in self.options.keys():
            sys.exit("port [-p] is not provided")
        if 0 > int(self.options["p"]) or int(self.options["p"]) > 65535:
            sys.exit("port is out of range [0 - 65535]")
        return int(self.options["p"])
