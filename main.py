#!/usr/bin/env python

# from socket import *
import socket
import sys

# import optparse
from cli import Cli
from scanner import Scanner


def scan(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(5)

    # for port in range(1, 1001):
    try:
        if sock.connect((host, port)):
            pass
    except Exception as error:
        print(error)
        pass


if __name__ == "__main__":
    cli = Cli(sys.argv[1:])
    host = cli.get_host()
    port = cli.get_port()

    scanner = Scanner(host=host, port=port)

    scan(host, port)
