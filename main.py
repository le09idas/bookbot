#get total count of words in text
def word_count(book_text):
    #simple counting of the split of the text of the book

    word_total = len(book_text.split())

    return word_total

#get the count of each individual character in a dict 
#with case-insensitive comparison
def character_count(book_text):
    
    character_totals = {}

    for word in book_text:
        for char in word:
            c = char.casefold()             #casefold() is used because casing is ignored
            if c not in character_totals:
                character_totals[c] = 1
            else:
                character_totals[c] += 1

    return character_totals


def main():

    book_path = "books/frankenstein.txt"

    with open(book_path, "r", encoding="utf-8") as f:
        file_contents = f.read()
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count(file_contents)} words found in the document")
    print("")
    
    char_count = character_count(file_contents)

    for char in char_count:
        print(f"The '{char}' character was found {char_count[char]} times")

    print("--- End report ---")

main()