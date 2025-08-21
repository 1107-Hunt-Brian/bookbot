def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()

def count_words(text):
    words= text.split()
    return len(words)

def main():
    book_text = get_book_text("books/frankenstein.txt")
    
    print(book_text)

    num_words = count_words(book_text)

    print(f"{num_words} words found in the document")
if __name__=="__main__":
    main()