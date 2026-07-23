from import_center.registry import PARSERS


def detect_parser(text: str):

    print("=" * 50)
    print("Проверяем парсеры...")
    print("=" * 50)

    for parser in PARSERS:

        print(parser.__class__.__name__)

        result = parser.can_parse(text)

        print("can_parse =", result)

        if result:
            print("Парсер найден")
            return parser

    print("Ни один парсер не подошел")

    return None