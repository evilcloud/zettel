""" This is a module, which deals with the graph building.
Communication between functions is done by passing arguments.
Main formats are:
    filename: full filename, which includes the path
	filebase: filename without the path
	purename: filename without path and without extension
	Parts of the purename:
		zid: Zettel-style ID (12 or 14 numbers, usually in the beginning of the filename or betwee [[.]])
		ztitle: alpha-numeric type of the file, which is not z_id
	Parts of the file content:
		header: the first # header in the file
		link: Zettelkasten-style [[link]] from the file

	Multiples packed into a list are indicated as plurals.
	If dictionary of complex list structure is necessary, use different naming conventions
"""
from prompt_toolkit.widgets.menus import MenuItem
from graph.graphrx import graphrx
import menu

from graph.pyvis import pyvis


def cypher(directory):
    pass


def main():
    directory = "/Users/kg/Dropbox/academic"
    menu_items = {
        "return": "...return",
        "pyvis": "PYVIS graph",
        "graphxr": "graphXR graph",
        "cypher": "Cypher code",
    }
    a = menu.menu_list(menu_items, "Graph")
    input(a)
    if a == menu_items["pyvis"]:
        pyvis(directory)
    if a == menu_items["graphxr"]:
        graphrx(directory)
    if a == menu_items["cypher"]:
        cypher(directory)


if __name__ == "__main__":
    main()
