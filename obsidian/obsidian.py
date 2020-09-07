from helpers import collect, dir, files
from obsidian import replace
import os
import menu


def main():
    source = "/Users/kg/Dropbox/academic"
    destination = "/Users/kg/Dropbox/obsidian"

    print(f"Zettel-Obsidian rough formatter v0.1")
    print(f"Source directory: {source}")
    print(f"Destination directory: {destination}")
    files_list = dir.list_dir(source, [".md"])
    print(f"{len(files_list)} .md files found")
    num_title_collection = collect.get_nums_headers(files_list)
    print(f"{len(num_title_collection)} of {len(files_list)} entries collected")
    if menu.confirm("Do you wish to continue?"):
        dir.init_dest_dir(destination)
        for filename in files_list:
            new_file_data = replace.replace_hashes_inside(
                filename, num_title_collection
            )
            n = collect.get_header(filename)
            new_filename = (
                os.path.join(destination, n.strip("\n") + ".md") if n else filename
            )
            print(os.path.basename(new_filename), len(new_file_data))
            files.save_new(new_filename, new_file_data)
    print("Obsidian module completed")


if __name__ == "__main__":
    main()
