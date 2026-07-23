class Document:
    """
    Универсальный документ PFOS.
    """

    def __init__(self, text: str):

        self.text = text

        self.header = ""

        self.body = ""

        self.footer = ""