from stats import word_count, character_count

#get the text of the book from the file path given by the user
def get_book_text(book_path):
    
    with open(book_path, "r", encoding="utf-8") as f:
        file_contents = f.read()
    
    return file_contents

def main():

   #book_path = input("Enter path to book text file: i.e. /path/to/book/text\n")
    #file_contents = ""
    book_path = "books/frankenstein.txt"
    file_contents = ""

    with open(book_path, "r", encoding="utf-8") as f:
        file_contents = f.read()

    words = word_count(file_contents)

    print(f'Found {words} total words')

    chars = character_count(file_contents)

    print(chars)
    
    '''
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count(file_contents)} words found in the document")
    print("")
    
    char_count = character_count(file_contents)

    for char in char_count:
        print(f"The '{char}' character was found {char_count[char]} times")

    print("--- End report ---")
    '''

main()