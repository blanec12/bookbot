def get_num_words(text):
    return len(text.split())


def get_num_chars(text):
    char_counts = {}
    for char in text:
        c = char.lower()
        if c not in char_counts:
            char_counts[c] = 1
        else:
            char_counts[c] = char_counts[c] + 1
    return char_counts
