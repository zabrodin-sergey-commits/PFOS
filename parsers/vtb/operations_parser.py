import re

from models.operation import Operation


def parse_operations(text: str):

    operations = []

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]


    date_pattern = r"\d{2}\.\d{2}\.\d{4}"


    i = 0


    while i < len(lines):

        if re.fullmatch(date_pattern, lines[i]):


            date = lines[i]


            # проверяем, что следующая строка тоже дата
            if i + 1 >= len(lines):
                break


            if not re.fullmatch(date_pattern, lines[i + 1]):
                i += 1
                continue



            block = lines[i:i+12]


            amounts = []


            description = ""


            for line in block:


                if "RUB" in line:


                    numbers = re.findall(
                        r"-?\d+[.,]\d+",
                        line
                    )


                    for number in numbers:

                        amounts.append(
                            float(
                                number.replace(",", ".")
                            )
                        )



                if (
                    "Оплата" in line
                    or "Снятие" in line
                    or "Переводы" in line
                ):

                    description = line



            if amounts:


                value = amounts[0]


                direction = (
                    "OUT"
                    if value < 0
                    else "IN"
                )


                operations.append(

                    Operation(

                        date=date,

                        description=description,

                        amount=abs(value),

                        direction=direction

                    )

                )


            # перескакиваем через первую дату
            i += 2


        else:

            i += 1


    return operations