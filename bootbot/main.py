def main():
    book_path = "books/frankenstein.txt"

    print(f"--- Being report of {book_path} ---")
    
    
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"total number of words found {num_words}")
    chars_dict = get_chars_dict(text)
    

    char_list = [(key, value) for key, value in chars_dict.items() if key.isalpha()]

    
    char_list.sort()

    for lines in char_list:
        k,v = lines
        print(f"The {k} character was found {v} times")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()