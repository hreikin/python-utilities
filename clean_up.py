import logging
from pathlib import Path

def delete_all_targets(source_path, targets):
    """
    Takes a source directory and a list of files or extensions to delete as 
    input and then removes all matching items.
    
    :param source_path(str): The location of the files to search through.
    :param targets(list): Items to delete from the directory.
    """
    src = Path(source_path).resolve()
    all_files = src.rglob("*.*")
    for file in all_files:
        for target in targets:
            if str(file.resolve()).endswith(target):
                file.resolve().unlink()
                break

def delete_all_except_targets(source_path, targets=list()):
    """
    Takes a source directory and a list of files or extensions to keep as input 
    and then deletes all other files.
    
    :param source_path(str): The location of the files to search through.
    :param targets(list): Items to keep from within the directory.
    """
    src = Path(source_path).resolve()
    all_files = src.rglob("*.*")
    for file in all_files:
        for target in targets:
            if not str(file.resolve()).endswith(target):
                file.resolve().unlink()
                break

src = "test/"
remove = [".py"]
keep = ["clean_up.py"]
# delete_all_targets(src, remove)
delete_all_except_targets(src, keep)