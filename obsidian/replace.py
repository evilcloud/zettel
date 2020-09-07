import re
from helpers import files


def replace_nums(line: str, file_data: dict):
    hashes = re.findall(r"(\d{12}|\d{14})", line)
    for hashtag in hashes:
        if file_data.get(hashtag):
            line = line.replace(hashtag, file_data.get(hashtag).strip())
    return line


def replace_hashes_inside(filename: str, file_data: dict):
    new_text = []
    for line in files.get_lines(filename):
        new_text.append(replace_nums(line, file_data))
    return new_text
