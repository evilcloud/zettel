![](media/zettel_logo.png)

## What

A set of utilities for Zettelkasten, mostly around cleaning .md files and building schemas for different database formats. Currently supported:

- [Pyvis](https://pyvis.readthedocs.io/en/latest/) (and by extension NetworkX could be added with no issues)
- [graphXR](https://www.kineviz.com/)
- [Neo4j](https://neo4j.com/developer/cypher/) in the form of cypher commands

Also there is an awkward Obsidian reformatted.

## State

This is far from being even alpha. Missing:

- config
- testing
- maybe kill off Obsidian reformatting (it appears to have an adapter build-in now -- also, my solution is way too messy)

## Next

Further work is required to add meaningful data to connections, and this would be a result of systemic review of the Zettel format (probably add cypher at the bottom in a YAML or something)
