from stats import get_book_text, count_words, count_characters, sort_characters


def main():
    path = "books/frankenstein.txt"
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
