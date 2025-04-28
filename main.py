import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

with open(book_path) as f:
    book_text = f.read()

import stats

print("============ BOOKBOT ============")
print(f"Analyzing book found at {book_path}...")
print("----------- Word Count ----------")
word_count = stats.count_words(book_text)
print(f"Found {word_count} total words")
print("--------- Character Count -------")
char_count = stats.count_chars(book_text)
new_list = stats.sorted_list(char_count)
for list_item in new_list:
    print(f"{list_item['char']}: {list_item['num']}")
print("============= END ===============")