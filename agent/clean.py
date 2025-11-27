import re

def strip_markdown(md: str) -> str:
    """
    Convert Markdown itinerary into clean, plain text.
    Removes bold, headers, and formats bullets.
    """
    text = md

    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)  # remove bold
    text = re.sub(r'^\s*#{1,6}\s*(.*)', r'\1', text, flags=re.MULTILINE)  # remove headings
    text = text.replace("* ", "- ")  # convert bullets
    text = text.replace("#", "")  # remove leftover hashes
    text = re.sub(r'\n\s*\n', '\n\n', text)  # clean extra blank lines

    return text.strip()
