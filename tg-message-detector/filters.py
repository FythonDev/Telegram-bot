def is_sensitive(text, keywords):
    if not text:
        return False
    return any(word.lower() in text.lower() for word in keywords)