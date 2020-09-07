from pyvis.network import Network
import os
import re

from helpers.collect import get_header
from helpers.filename import canonical_basename
from helpers.files import get_content

net = Network("800px", "1200px")


def build_nodes(nodes: dict):
    """Builds nodes in pyvis graph with nodes {node ID: node label}"""
    node_id = []
    node_label = []
    for node in nodes:
        node_id.append(node)
        node_label.append(nodes[node])
    net.add_nodes(node_id, label=node_label)


def build_edges(edges: list):
    """Builds edges in pyvis graph with edges [(node 1, node 2)]"""
    for node1, node2 in edges:
        print(node1, node2)
        input()
        net.add_nodes([node1, node2], label=[(node1), canonical_basename(node2)])
        net.add_edge(node1, node2)


def build_graph(nodes):  # , edges: dict):
    """Builds pyvis graph
    nodes {node ID: nodeValue} and edges {source node: [connecting nodes]}"""
    # build_nodes(nodes)
    build_edges(edges)
    net.show_buttons()
    net.show("myg.html")


def link_content(content: str) -> list:
    """ Returns a list of all [[links]] in the file """
    return re.findall(r"(\d{12}|\d{14})", content)


def links_db(files_list: list) -> dict:
    """ Returns {ID: [internal links]}"""
    db = dict()
    for filename in files_list:
        fnum, _ = canonical_basename(filename)
        db[fnum] = link_content(get_content(filename))
    return db


def fnum_ftitle_filename_db(files_list: list) -> dict:
    """ Returns a list of IDs from all files in the list"""
    sn = {}
    for filename in files_list:
        fnum, ftitle = canonical_basename(filename)
        sn[fnum] = [ftitle, filename]
    return sn


def connect(links_db: dict, source_db: dict) -> list:
    connections = []
    for file_id in links_db:
        for link in links_db[file_id]:
            connections.append((link, file_id))
    return connections


def list_dir(directory: str, extension: str = ".md") -> list:
    """Returns the list of files in given directory with the given extension(s).
    Extensions can be passed as 'str' or 'list'.
    If no extension given ".md" is used"""
    # e = tuple(extension)
    return [
        os.path.join(directory, files)
        for files in os.listdir(directory)
        if files.endswith(extension)
    ]
    # if os.path.splitext(filename) in e
    # ]


def main():
    directory = "/Users/kg/Dropbox/academic"
    files_list = list_dir(directory)
    links = links_db(files_list)
    source_db = fnum_ftitle_filename_db(files_list)
    edges = connect(links, source_db)
    # nodes = get_nums_headers(files_list)
    # build_graph(nodes)
    build_edges(edges)


if __name__ == "__main__":
    main()
