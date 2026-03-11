def extract_text_and_tags(words):
    tags = []
    text_words = []

    for word in words:
        if word.startswith("#"):
            tags.append(word)
        else:
            text_words.append(word)

    text = " ".join(text_words)

    return text, tags