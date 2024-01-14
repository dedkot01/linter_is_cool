if __name__ == "__main__":
    msg: str = "Это строка слишком длинная, потому что она содержит в себе тело Email сообщения.\nМожно было бы использовать тройные кавычки, но тогда сообщение будет иметь отступы вначале каждой строки."
    print(type(msg))
    print(msg)

    print("---------------")

    msg: str = """
        Это строка слишком длинная, потому что она содержит в себе тело Email сообщения.
        Можно было бы использовать тройные кавычки, но тогда сообщение будет иметь отступы вначале каждой строки.
    """
    print(type(msg))
    print(msg)

    print("---------------")

    msg: str = (
        "А вот эта строка всё такая же длинная, но тем не менее, она всё же помещается в экран."
        "\nИ только благодаря линтеру Flake8 я захотел найти этот способ разделять "
        "длинную строку на несколько строк кода."
        "\nТак вот как мне настроить на такую же работу Ruff?"
    )
    print(type(msg))
    print(msg)

