import re

def extract_links(text):
    return re.findall(r'(https?://\S+)', text)


def detect_quality(text):

    if "1080" in text:
        return "1080p"
    if "720" in text:
        return "720p"
    if "480" in text:
        return "480p"

    return "Unknown"


def detect_size(text):

    m = re.search(r'(\d+(?:\.\d+)?\s?(GB|MB))', text)

    if m:
        return m.group(1)

    return ""


def detect_title(text):

    lines = text.split("\n")

    for line in lines:
        if "(" in line and ")" in line:
            return line.strip()

    return text.split("\n")[0]
