from stats import get_book_text, count_words, count_characters, sort_characters
import sys

def main():
    # Check CLI args
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]  # the book path from command line
    book_text = get_book_text(path)

    # Word count
    num_words = count_words(book_text)

    # Character count
    char_counts = count_characters(book_text)
    sorted_chars = sort_characters(char_counts)

    # Print report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
