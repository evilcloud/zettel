from io import TextIOWrapper
from helpers import filename


def get_lines(filename: str) -> list:
    """ Returns file content by lines"""
    try:
        with open(filename, "r") as f:
            return f.readlines()
    except ValueError:
        return [""]


def get_content(filename: str) -> str:
    """ Returns the file content as one string"""
    try:
        with open(filename, "r") as f:
            return f.read()
    except ValueError:
        return ""


def save_new(filename: str, lines: list):
    """ Saves file line-by-line """
    with open(filename, "w") as f:
        f.writelines(lines)
