import sys
from stats import counting_words, counting_each_character, sorting

def get_book_text(path_to_file):

    with open(path_to_file) as f:
        file_content = f.read()

        return file_content


def main():

    #path = "books/frankenstein.txt"
    
    if len(sys.argv) >= 2:
        script_name, book_link = sys.argv

        path = book_link

        new_list = sorting(counting_each_character(get_book_text(path)))
    
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}")
        print("----------- Word Count ----------")
        print(f"Found {counting_words(get_book_text(path))} total words")
        print("--------- Character Count -------")
    
        for dict_letter in new_list:
        
            print(f"{dict_letter["letter"]}: {dict_letter["num"]}")

        print("============= END ===============")

    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    

main()

    
