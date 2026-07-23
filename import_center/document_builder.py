from models.document import Document


def build_document(text: str) -> Document:
    """
    Создает объект документа.
    Пока разделяем документ условно.
    """

    document = Document(text)

    lines = text.splitlines()

    # Пока считаем, что первые 120 строк — это шапка документа.
    header_size = min(120, len(lines))

    document.header = "\n".join(lines[:header_size])

    document.body = "\n".join(lines[header_size:])

    document.footer = ""

    return document