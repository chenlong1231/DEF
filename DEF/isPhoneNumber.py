def is_phone_number(text):
    if len(text) != 11:
        return False
    for i in range(0, len(text)):
        number = text[i]
        if not number.isdecimal():
            return False
    return True
