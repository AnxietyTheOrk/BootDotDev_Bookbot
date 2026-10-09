def get_book_text(book_title):
    with open(book_title) as f:
        file_contents = f.read()
    return file_contents

def char_count(text):
    book_text = text
    char_count = {}
    for char in book_text.lower():
        char_count[char] = char_count.get(char, 0) + 1
    return char_count


def book_stats(text):
    book_text = text
    words = book_text.split()
    return words

def sort_on(char_counts: tuple[str, int]):
    return char_counts[1]

def chars_dict_to_sorted_list(char_counts: dict[str, int]):
    unsorted_list = []
    for char in char_counts:
        unsorted_list.append((char, char_counts[char]))
    sorted_list = sorted(unsorted_list, reverse=True, key=sort_on)
    return sorted_list