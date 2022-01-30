import os, shutil

def move_to_location(source_path, output_path):
    """
    Moves all files and folders from one location to another.
    
    :param source_path(str): Location of the files and folders to be moved.
    :param output_path(str): Location to be moved to.
    """
    for file in os.listdir(source_path):
        shutil.move(source_path + file, output_path + file)