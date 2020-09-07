import os
import platform
import time
import logging

from helpers import collect


def canonical_basename(filename: str) -> (str, str):
    """ Returns (ID, title)
     If ID is not found, a creation / last modification date is used.
     If title not found, a # header from the file is used. """
    fnum, ftitle = split_num_title(filename)
    if not fnum:
        fnum = creation_date(filename)
    if t := collect.get_header(filename):
        ftitle = t
    return fnum, ftitle


def creation_date(filename: str) -> str:
    """ Returns the file birth time. OS specific:
    In in some cases on macOS and in all cases in Linux
    the date of last modification is returned instead."""
    if platform.system() == "Windows":
        # Windows has different procedure
        logging.debug("windows")
        bt = os.path.getctime(filename)
    else:
        stat = os.stat(filename)
        try:
            # macOS
            logging.debug("macos")
            bt = os.path.getatime(filename)
        except AttributeError:
            # Linux is complicated with birth times,
            # so last mod is the second best here
            logging.debug("linux or failed macos")
            bt = stat.st_mtime(filename)
    return time.strftime("%Y%m%d%H%M", time.localtime(bt))


def split_num_title(filename: str) -> tuple():
    """ Returns (Zettel ID, filename). Whatever is not present is replaced by ''"""
    fn = os.path.splitext(os.path.basename(filename))[0]
    try:
        file_num, file_title = fn.split(" ", 1)
        if file_num.isdigit() and any([len(file_num) == 12, len(file_num) == 14]):
            ret = (file_num, file_title)
        else:
            ret = ("", filename)
    except ValueError:
        ret = (filename, "") if filename.isdigit() else ("", filename)
    return ret

# ============ after graph
