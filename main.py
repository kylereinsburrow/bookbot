def main():
    book_path = "books/frankenstein.txt"
    book_contents = get_book_text(book_path)
    print(book_contents)

def get_book_text(path: str) -> str:
    with open(path, encoding='utf-8') as f:
        return f.read()


main()