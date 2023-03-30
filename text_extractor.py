from pdfminer.high_level import extract_text
import pyttsx3
import re


def format_text(text):
    #detect tab formating
    tab_regex = r"\(cid\:[0-9]+\)"

    #detect header text
    header_regex = r"\♀A T A L E O F T W O C I T I E S"

    #detect double  spaces
    spaces_regex = r"\s\s+"

    #detect new line
    new_line_regex = r"\n"

    text = re.sub(tab_regex, " ", text)
    text = re.sub(header_regex, " ", text)
    text = re.sub(new_line_regex, " ", text)
    text = re.sub(spaces_regex, " ", text)
    return text

