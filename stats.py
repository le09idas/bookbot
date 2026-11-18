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

def sort_on(count: tuple[str,int]) -> int:
    return count[1]

def chars_dict_to_sorted_list(counted_chars: dict[str, int]) -> list[tuple[str, int]]:
    sorted_count = []

    for char in counted_chars:
        sorted_count.append((char, counted_chars[char]))

    return sorted(sorted_count, reverse=True, key=sort_on)
