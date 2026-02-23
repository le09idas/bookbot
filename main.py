from stats import word_count, character_count, sort_chars

import sys

#get the text of the book from the file path given by the user
def get_book_text(book_path):
    
    with open(book_path, "r", encoding="utf-8") as f:
        file_contents = f.read()
    
    return file_contents

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    #book_path = input("Enter path to book text file: i.e. /path/to/book/text\n")
    #file_contents = ""
    book_path = sys.argv[1]
    file_contents = ""

    with open(book_path, "r", encoding="utf-8") as f:
        file_contents = f.read()

    words = word_count(file_contents)

    #print(f'Found {words} total words')

    chars = character_count(file_contents)

    #print(chars)

    char_dict = sort_chars(chars)

    #print(char_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")

    for dic in char_dict:
        if dic["char"].isalpha():
            print(f"{dic["char"]}: {dic["num"]}")

    print("============= END ===============")

main()