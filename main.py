#!/usr/bin/env python

import sys

from cli import Cli
from scanner import Scanner


if __name__ == "__main__":
    cli = Cli(sys.argv[1:])
    host = cli.get_host()
    ports = cli.get_ports()

    scanner = Scanner(host=host, ports=ports)

    scanner.scan()
