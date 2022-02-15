import shutil
from pathlib import Path

def copy_to_location(src_path, dest_path, file_extensions=None, overwrite=False):
    """
    Recursively copies files from source to destination directory.
    
    :param src_path(str): Source directory that contains files and folders to be copied.
    :param dest_path(str): Destination directory to copy to.
    :param file_extensions(list): Optional list of file extensions to copy, if none given all files and folders are copied.
    :param overwrite(bool): If True all files will be overwritten, otherwise if false skip file.
    :return files_count(int): Count of copied files.
    """
    src_path = Path(src_path).resolve()
    dest_path = Path(dest_path).resolve()
    files_count = 0
    dest_path.mkdir(parents=True, exist_ok=True)
    items = src_path.rglob("*")
    for item in items:
        if item.is_dir():
            path = Path(dest_path / item.name)
            print(path)
            files_count += copy_to_location(src_path=item, dest_path=path, file_extensions=file_extensions, overwrite=overwrite)
        elif file_extensions != None:
            for extension in file_extensions:
                if item.name.endswith(extension):
                    file = Path(dest_path / item.name)
                    if not file.exists() or overwrite:
                        shutil.copyfile(item, file)
                        files_count += 1
        else:
            file = Path(dest_path / item.name)
            if not file.exists() or overwrite:
                shutil.copyfile(item, file)
                files_count += 1
    return files_count

def simple_copy_all(src, dest):
    """
    Simple copy function that copies all files and folders from one directory to 
    another. This DOES NOT overwrite files if they exist at the destination path 
    already.

    :param src(str): Source directory to copy contents from.
    :param dest(str): Destination directory to copy contents to.
    """
    src = Path(src).resolve()
    dest = Path(dest).resolve()
    shutil.copytree(src, dest, dirs_exist_ok=True)

src = "test_a/"
out = "test_b/"
# copy_to_location(src, out)
src = "test_b/"
out = "test_a/"
simple_copy_all(src, out)