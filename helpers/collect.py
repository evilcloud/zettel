import re
from helpers import files
from helpers.filename import split_num_title


def get_header(filename: str) -> str:
    """ Returns the first # title from the file excl. hashtag and leading space.
    Character '/' is removed to avoid filesystem interference.
    File must contain the full path"""
    for line in files.get_lines(filename):
        if re.findall("(^# )", line):
            return line[2:].replace("/", "")
    return ""


def get_nums_headers(filenames: list) -> dict:
    """ Returns {ID : # title} """
    file_data = dict()
    for file in filenames:
        if header := get_header(file):
            num, _ = split_num_title(file)
            if num:
                file_data[num] = header
    return file_data
