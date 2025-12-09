from stats import get_num_words, get_num_chars
from collections import Counter
import sys


def get_book_text(filepath):
    with open(filepath, "r") as f:
        contents = f.read()

    return contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    filepath = sys.argv[1]
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    num_chars = Counter(get_num_chars(text)).most_common()

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for c, count in num_chars:
        if c.isalpha():
            print(f"{c}: {count}")
    print("============= END ===============")


main()
