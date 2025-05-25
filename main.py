
import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text():
    with open(sys.argv[1]) as f:
        file_contents = f.read()
    return file_contents

from stats import num_words

from stats import character_count

from stats import sorted_list


def main():
    book_text = get_book_text()
    words = num_words(book_text)
    results = character_count(book_text)
    report = sorted_list(results)
    print (f"Found {words} total words")
    for pair in report:
      print(f"{pair['char']}: {pair['num']}")
    

if __name__ == "__main__":
    main()    


