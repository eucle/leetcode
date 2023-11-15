def greatestLetter(s: str) -> str:
    list_of_letters = sorted(s, reverse=True)
    set_of_letters = set(list_of_letters)
    for letter in list_of_letters:
        if letter.isupper() and letter.lower() in set_of_letters:
            return letter
    return ''
