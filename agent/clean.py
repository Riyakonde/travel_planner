import re

def strip_markdown(md: str) -> str:
    """
    Convert Markdown itinerary into clean, plain text.
    Removes **bold**, # headers, and formats bullets.
    """
    text = md

    # Remove bold formatting
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)

    # Remove headings (#, ##, ###)
    text = re.sub(r'^\s*#{1,6}\s*(.*)', r'\1', text, flags=re.MULTILINE)

    # Replace bullets
    text = text.replace("* ", "- ")

    # Remove leftover #
    text = text.replace("#", "")

    # Remove extra blank lines
    text = re.sub(r'\n\s*\n', '\n\n', text)

    return text.strip()
