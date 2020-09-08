import inquirer
from inquirer.themes import GreenPassion

import graph.graphrx
from obsidian import obsidian
from graph import graph


def confirm(message: str, default: bool = True):
    """ A yes/no confirmation.
    Accepts Message string and True / False for default answer.
    If no default is provided, True is assigned. """
    questions = [
        inquirer.Confirm(message, message=message, default=default),
    ]
    answers = inquirer.prompt(questions)
    return answers[message]


def menu_list(items: dict, label: str = "Questions"):
    menu_items = items
    choices = [menu_items[value] for value in menu_items]
    questions = (inquirer.List(label, choices=choices),)
    answers = inquirer.prompt(questions, theme=GreenPassion())
    return answers[label]


def main():
    menu_items = {
        "graph": "Build the graph",
        "obsidian": "Obsidian specific format and folder",
        "quit": "...quit",
    }
    while True:
        a = menu_list(menu_items, "Main")

        if a == menu_items["quit"]:
            print("-" * 5, "\nQuitting now... bye")
            break

        if a == menu_items["graph"]:
            graph.main()

        if a == menu_items["obsidian"]:
            obsidian.main()


if __name__ == "__main__":
    main()
