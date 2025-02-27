import sys
from stats import get_wordcount
from stats import get_char_count
from stats import sort_dict

def main():
    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    bookpath = sys.argv[1]
    text = get_book_text(bookpath)
    wordcount = get_wordcount(text)
    char_count = get_char_count(text)
    sorted_chars = sort_dict(char_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookpath}...")
    print("----------- Word Count ----------")
    print(f"Found {wordcount} total words")
    print("--------- Character Count -------")
    
    for char_dict in sorted_chars:
        char = list(char_dict.keys())[0]
        count = char_dict[char]
        print(f"{char}: {count}")



def get_book_text(path):
    with open (path) as f:
        return f.read()



main()




