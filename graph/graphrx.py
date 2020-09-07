from graph import helpers
from graph.helpers import extract_header, save_file


def graphrx(directory):
    csv_file = "grx.csv"
    f = [f"Source, Target"]
    filenames = helpers.get_filenames(directory)
    zid_filenames = helpers.zid_filenames_db(filenames)
    for filename in filenames:
        t1 = helpers.extract_header(filename)
        links = [
            extract_header(zid_filenames.get(zid))
            for zid in helpers.extract_links(filename)
        ]
        links_clean = [link for link in links if link]
        for link in links_clean:
            f.append(f"{t1}, {link}")
    csv = "\n".join(f)
    save_file(csv_file, csv)
    print("Graph build done")
    print(f"{len(f)} pair entries")
    print(f"[{csv_file}] has been saved")
    print("-----")