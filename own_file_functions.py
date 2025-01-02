import pathlib
import shutil


def file_processing(source_path, file):
    """The function for sorting files"""

    status: bool = True
    file_name: str = get_file_name(file)
    destination_path: str = source_path + "\\" + file_name[0:10]

    try:
        if not pathlib.Path(destination_path).is_dir():
            pathlib.Path.mkdir(destination_path)

        path_in = pathlib.PurePosixPath(file)
        path_to = pathlib.PurePosixPath(destination_path + "\\" + get_file_name(file))

        shutil.move(path_in, path_to)
    except KeyError:
        status = False

    return status


def files_search(source_directory, recursive, file_format):
    """The function for file search"""

    if recursive:
        images: list = list(pathlib.Path(source_directory).rglob(file_format, case_sensitive=False))
    else:
        images: list = list(pathlib.Path(source_directory).glob(file_format, case_sensitive=False))

    return list(images)


def get_file_name(file):
    """The function for getting the file name"""

    return pathlib.PurePosixPath(file).name


def checking_path(path):
    """The function for checking the path"""

    if pathlib.Path(path).is_dir():
        status: bool = True
    else:
        status: bool = False

    return status
