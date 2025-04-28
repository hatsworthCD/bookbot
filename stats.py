def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    chara_totals = {}
    for char in text:
        char = char.lower()
        if char in chara_totals:
            chara_totals[char] += 1
        else:
            chara_totals[char] = 1
    return chara_totals

def sorted_list(dict):
    filtered_items = [{"char": k, "num": v} for k, v in dict.items() if k.isalpha()]
    new_list = sorted(filtered_items, key=lambda x: x["num"], reverse=True)
    return new_list