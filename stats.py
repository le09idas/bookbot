#get total count of words in text
def word_count(book_text):
    #simple counting of the split of the text of the book

    word_total = len(book_text.split())

    return word_total

#get the count of each individual character in a dict 
#with case-insensitive comparison
def character_count(book_text):
    
    excluded_chars = {".", " ", "#"}
    character_totals = {}

    for word in book_text:
        for char in word:
            c = char.casefold()             #casefold() is used because casing is ignored
            if c in excluded_chars:
                pass
            elif c not in character_totals:
                character_totals[c] = 1
            else:
                character_totals[c] += 1

    return character_totals

def sort_on(dict):
    return dict["num"]

def sort_chars(char_map):
    
    char_dict_list = []

    for char in char_map:
        char_dict_list.append({
            "char": char,
            "num": char_map[char]
        })

    char_dict_list.sort(reverse=True, key=sort_on)

    return char_dict_list




