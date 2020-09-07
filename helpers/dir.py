import os
import shutil
import menu


def list_dir(directory: str, extensions: any = ".md") -> list:
    """ Returns the list of files in the given directory with
    given extension(s) (list or strings).
    If no extension given, default '.md' is used"""
    extension = tuple(extensions)
    return [
        os.path.join(directory, file)
        for file in os.listdir(directory)
        if os.path.splitext(file)[1] in extension
    ]


def init_dest_dir(directory):
    if not os.path.isdir(directory):
        os.mkdir(directory)
        print(f"Directory [{directory}] created")
    fnum = len(os.listdir(directory))
    if fnum > 0:
        print(f"{fnum} items found in {directory}")
        if menu.confirm("REBUILD the directory (old files will be erased)?", False):
            shutil.rmtree(directory)
            os.mkdir(directory)
            print(f"{directory} rebuilt from scratch")
