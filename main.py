def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()

def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(book_text)

if __name__=="__main__":
    main()