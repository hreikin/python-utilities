from pathlib import Path

def move_to_location(src, dest):
    """
    Moves all files and folders from one location to another.
    
    :param src(str): Location of the files and folders to be moved.
    :param dest(str): Location to be moved to.
    """
    src = Path(src).resolve()
    dest = Path(dest).resolve()
    src.rename(dest)

src = "test/"
dest = "dest/"
move_to_location(src, dest)