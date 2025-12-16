import sys
from stats import *

def get_book_text(file_input):
    with open(file_input) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)



    book_text = get_book_text(sys.argv[1])
    total_words = get_total_words(book_text)
    total_count = get_character_count(book_text)
    sorted_list_of_dictionaries = get_sorted_dictionary(total_count)
    
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    
    print(f"Found {total_words} total words\n--------- Character Count -------")
    
    for i in sorted_list_of_dictionaries:
        if i["char"].isalpha():
            print(f"{i['char']}: {i['num']}")
    
    print("============= END ===============")

if __name__ == "__main__":
    main()
