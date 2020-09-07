from pyvis.network import Network
import pyperclip

import menu
from graph.helpers import get_filenames, zid_header_db, zid_links_db


def pyvis(directory: str):
    html_file = "zettel_pyvis.html"
    net = Network("90%", "100%")
    filenames = get_filenames(directory)
    zid_headers = zid_header_db(filenames)
    connections = zid_links_db(filenames)
    if menu.confirm("Add non-existent nodes?", False):
        add_none = True
    else:
        add_none = False
    # build nodes
    for zid in zid_headers:
        net.add_node(zid, label=zid_headers[zid])
    # build connections
    net.add_node("None")
    i = 0
    for item in connections:
        n1, n2 = item
        if add_none and (not n1 or not n2):
            continue
        if n1 not in zid_headers:
            n1 = "None"
        if n2 not in zid_headers:
            n2 = "None"
        net.add_edge(n1, n2)
        i += 1
    net.show_buttons()
    net.show(html_file)
    copy_text = f"open {html_file}"
    pyperclip.copy(copy_text)
    print(f"Graph build done")
    print(f"{len(net.nodes)} nodes")
    print(f"{len(net.edges)} edges, of projected {len(connections)}")
    print(f"Edges to non-existent nodes mode: {add_none}")
    print(f"The data has been stored in {html_file}")
    print(f"[{copy_text}] has been placed in the clipboard and can be Ctr-V")
    print("----")
