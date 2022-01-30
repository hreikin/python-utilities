import os

def clean_up_remove(source_path):
    """
    Walks through the source path and removes the partial and original 
    files after conversion.
    
    :param source_path(str): The location of the files to search through.
    """
    source_path = os.path.realpath(source_path)
    remove = ["-PARTIAL.html", "-ORIGINAL.html"]
    for root, dirnames, filenames in os.walk(source_path):
        for filename in filenames:
            for item in remove:
                if filename.endswith(item):
                    os.remove(f"{root}/{filename}")

def clean_up_keep(source_path):
    """
    Walks through the source path and removes the partial and original 
    files after conversion.
    
    :param source_path(str): The location of the files to search through.
    """
    source_path = os.path.realpath(source_path)
    keep = "-PARTIAL.html"
    for root, dirnames, filenames in os.walk(source_path):
        for filename in filenames:
            if not filename.endswith(keep):
                os.remove(f"{root}/{filename}")