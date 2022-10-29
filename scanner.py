class Scanner:
    """
    Scanner class
    """

    def __init__(self, **kwargs) -> None:
        self.host = kwargs["host"]
        self.port = kwargs["port"]
