def should_forward(message, keywords):
    text = message.text or ""
    return any(keyword.lower() in text.lower() for keyword in keywords)
