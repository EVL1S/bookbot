from stats import count_words, count_char
import sys

def main():

    filepath = get_input()

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    get_book_text(filepath)
    print("--------- Character Count -------")
    count_char(filepath)
    print("============= END ===============")

def get_book_text(filepath):

    with open(filepath, encoding="utf-8") as f:
        file_contents = f.read()
        #print(file_contents)
        count_words(file_contents)

def get_input():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return sys.argv[1]







main()

    