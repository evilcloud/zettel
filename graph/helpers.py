from graph.graph_tmp import links_db
import os
import re


def get_filenames(directory: str, extension: str = ".md") -> list:
    """ Returns list of filenames in the given directory with a given extension.
    If no extension is provided, default '.md' is used"""
    return [
        os.path.join(directory, filebase)
        for filebase in os.listdir(directory)
        if filebase.endswith(extension)
    ]


def zid_filenames_db(filenames) -> dict:
    """ Returns {zid: filename} for easy access """
    db = {}
    for filename in filenames:
        db[extract_zid(filename)] = filename
    return db


def zid_header_db(filenames: list) -> dict:
    """Returns {zit: header} for the easy value access """
    db = {}
    for filename in filenames:
        db[extract_zid(filename)] = extract_header(filename)
    return db


def zid_links_db(filenames: list) -> list:
    """ Returns {zid : [zid files liked to key]} for easy access """
    db = []
    for filename in filenames:
        db.extend([(link, extract_zid(filename)) for link in extract_links(filename)])
    return db


def get_file_content(filename: str) -> str:
    """ Returns the content of the file """
    try:
        with open(filename, "r") as f:
            return f.read()
    except TypeError:
        return ""


def to_pure(filename: str) -> str:
    """ Returns filename converted to purename (no ext and no path) """
    one = os.path.basename(filename)
    two = os.path.splitext(one)[0]
    print(two)
    return two


def extract_zid(filename: str) -> str:
    """ Returns the Zettel-style ID (12 or 14 digits), or '' in case ID is missing """
    try:
        return re.search(r"^\d{12}|\d{14}\s", os.path.basename(filename)).group()
    except AttributeError:
        return ""


def extract_ztitle(filename: str) -> str:
    """ Returns purename of the given filename withouth Zettel-style ID, if such present """
    pure = to_pure(filename)
    zid = extract_zid(filename)
    return pure.replace(extract_zid(filename), "") if zid else pure


def extract_header(filename: str) -> str:
    """ Returns the first # header from the given file """
    content = get_file_content(filename).split("\n")
    for line in content:
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def extract_links(filename: str) -> list:
    return re.findall(r"(\d{12}|\d{14})", get_file_content(filename))


def save_file(name, content: str):
    with open(name, "w") as f:
        f.write(content)
