def word_count(text: str) -> int:

    words = len(text.split())

    return words

def char_count(text: str) -> dict[str, int]:
    char_count = {}

    for char in text.lower():

        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count
