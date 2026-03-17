import re

def detect_quality(text):

    if "1080" in text:
        return "1080p"

    if "720" in text:
        return "720p"

    if "480" in text:
        return "480p"

    return "Unknown"


def detect_size(text):

    match = re.search(r'(\d+(?:\.\d+)?\s?(GB|MB))', text)

    if match:
        return match.group(1)

    return ""


def extract_links(text):

    return re.findall(r'(https?://\S+)', text)
