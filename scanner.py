from threading import Thread
from socket import socket, AF_INET, SOCK_STREAM, setdefaulttimeout


class Scanner:
    """
    Scanner class
    """

    def __init__(self, **kwargs) -> None:
        """Constructor"""
        self.host = kwargs["host"]
        self.ports = kwargs["ports"]

    def scan(self):
        for port in self.ports:
            t = Thread(target=self.connect, args=(port,))
            t.run()

    def connect(self, port):
        try:
            setdefaulttimeout(2)

            s = socket(AF_INET, SOCK_STREAM)
            s.connect((self.host, port))

            banner = self.read_banner(s)
            print(banner)

            print(f"Port {port} is open")
        except Exception as e:
            pass
        finally:
            s.close()

    def read_banner(self, sock):
        return sock.recv(1024)
