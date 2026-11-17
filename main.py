from stats import word_count, char_count

def get_book_text(file_path: str) -> str:

    file_contents = ""

    with open(file_path, "r") as f:
        file_contents = f.read()

    return file_contents

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = word_count(text)
    char_counts = char_count(text)

    print(f"Found {num_words} total words")
    print(char_counts)

main()
