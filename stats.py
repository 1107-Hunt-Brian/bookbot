def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    """Counts the number of times each character appears in the text."""
    text = text.lower()  # normalize to lowercase
    char_counts = {}

    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts


def sort_characters(char_counts):
    """Converts dict into sorted list of dicts: [{'char': 'a', 'num': 123}, ...]"""
    sorted_list = []

    for char, count in char_counts.items():
        if char.isalpha():  # skip spaces, punctuation, etc.
            sorted_list.append({"char": char, "num": count})

    # Sort list of dicts by "num" descending
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_list
