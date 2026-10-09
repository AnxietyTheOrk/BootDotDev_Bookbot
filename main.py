from stats import get_book_text
from stats import book_stats
from stats import char_count
from stats import chars_dict_to_sorted_list
import sys



def print_report(path, words, sorted_list):
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {len(words)} total words")
    print("--------- Character Count -------")
    for char, count in sorted_list:
            if char.isalpha():
                print(f"{char}: {count}")
    print("============= END ===============")

def main():
    
    if len(sys.argv) <  2:
         print("Usage: python3 main.py <path_to_book>")        
         sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)
    words = book_stats(text)
    count = char_count(text)
    sorted_list = chars_dict_to_sorted_list(count)
    print_report(path, words, sorted_list)


main()