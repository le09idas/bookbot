from stats import char_count, chars_dict_to_sorted_list, word_count
import sys

def get_book_text(file_path: str) -> str:

    file_contents = ""

    with open(file_path, "r") as f:
        file_contents = f.read()

    return file_contents

def print_report(path: str, word_count: int, char_counts: list[tuple[str,int]]) -> int:

    print(f'''============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------''')

    for char in char_counts:
        if char[0].isalpha():
            print(f"{char[0]}: {char[1]}")

    print("============= END ===============")
    return 0

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)
    num_words = word_count(text)
    char_counts = chars_dict_to_sorted_list(char_count(text))

    print_report(path, num_words, char_counts)

main()
