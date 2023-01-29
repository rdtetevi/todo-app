import pathlib
import zipfile as zf
import pathlib as pt

"""
 the better way to create python path it's use pathlib who 
 is library disponible in Python installation
 a = pathlib.Path("dest", "compressed.zip")
"""


def make_archive(filepaths, dest_dir):
    dest_path = pt.Path(dest_dir, "compressed.zip")
    with zf.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)


if __name__ == "__main__":
    make_archive(filepaths=["day11", "day12"], dest_dir="Dest")
