def format_caption(original, template):
    return template.replace("{original_caption}", original or "")
