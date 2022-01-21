import os, glob, shutil

def copy_to_location(source_path, destination_path, override=False):
    """
    Recursively copies files from source to destination directory.
    
    :param source_path(str): Source directory that contains files and folders to be copied.
    :param destination_path(str): Destination directory to copy to.
    :param override(bool): If True all files will be overwritten, otherwise if false skip file.
    :return files_count(int): Count of copied files.
    """
    source_path = os.path.realpath(source_path)
    destination_path = os.path.realpath(destination_path)
    files_count = 0
    if not os.path.exists(destination_path):
        os.mkdir(destination_path)
    items = glob.glob(source_path + '/*')
    for item in items:
        if os.path.isdir(item):
            path = os.path.join(destination_path, item.split('/')[-1])
            files_count += copy_to_location(source_path=item, destination_path=path, override=override)
        else:
            file = os.path.join(destination_path, item.split('/')[-1])
            if not os.path.exists(file) or override:
                shutil.copyfile(item, file)
                files_count += 1
    return files_count