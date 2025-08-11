from collections import Counter

def count_words(words):
    list = words.split()
    print(f"Found {len(list)} total words")

def count_char(filepath):

    with open(filepath, "r", encoding="utf-8") as f:
        text = ''.join(c for c in f.read().lower() if c.isalpha())
        counts = Counter(text)

    for písmeno, počet in counts.most_common():
        print(f"{písmeno}: {počet}")
