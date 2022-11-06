import sys
import re


class Cli:
    def __init__(self, arguments) -> None:
        self.options = {}
        for (option, value) in zip(arguments[0::2], arguments[1::2]):
            self.options[option[1:]] = value

    def get_options(self):
        """ """
        return self.options

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

    def get_ports(self):
        """ """
        ports = []

        if "p" not in self.options.keys():
            sys.exit("port(s) [-p] not provided")

        for port in self.options["p"].split(","):
            if 0 > int(port) or int(port) > 65535:
                sys.exit("port is out of range [0 - 65535]")
            ports.append(int(port))

        return ports
