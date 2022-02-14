import shutil
from pathlib import Path

def copy_to_location(source_path, destination_path, file_extensions=None, overwrite=False):
    """
    Recursively copies files from source to destination directory.
    
    :param source_path(str): Source directory that contains files and folders to be copied.
    :param destination_path(str): Destination directory to copy to.
    :param file_extensions(list): Optional list of file extensions to copy, if none given all files and folders are copied.
    :param overwrite(bool): If True all files will be overwritten, otherwise if false skip file.
    :return files_count(int): Count of copied files.
    """
    source_path = Path(source_path).resolve()
    destination_path = Path(destination_path).resolve()
    files_count = 0
    destination_path.mkdir(parents=True, exist_ok=True)
    items = source_path.rglob("*")
    for item in items:
        if item.is_dir():
            path = Path(destination_path / item.name)
            print(path)
            files_count += copy_to_location(source_path=item, destination_path=path, file_extensions=file_extensions, overwrite=overwrite)
        elif file_extensions != None:
            for extension in file_extensions:
                if item.name.endswith(extension):
                    file = Path(destination_path / item.name)
                    if not file.exists() or overwrite:
                        shutil.copyfile(item, file)
                        files_count += 1
        else:
            file = Path(destination_path / item.name)
            if not file.exists() or overwrite:
                shutil.copyfile(item, file)
                files_count += 1
    return files_count

src = "test/test_a/"
out = "test/test_b/"
copy_to_location(src, out)