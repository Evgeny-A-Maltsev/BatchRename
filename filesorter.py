import click
import own_file_functions as own_file
from typing import Any


program_description: str = "FileSorter by Evgeny A. Maltsev (yevmal@gmail.com)"
program_version: str = "0.0.1"


@click.command("cli", context_settings={'show_default': True})
@click.argument('source_directory', required=True)
@click.option('-r', '--recursive', is_flag=True, default=False, help='Recursively file search')
def batch_rename(source_directory, recursive):
    count_ok: int = 0
    count_fail: int = 0

    if own_file.checking_path(source_directory):
        files: list[Any] = own_file.files_search(source_directory, recursive, "*.*")

        for file in files:
            if own_file.file_processing(source_directory, file):
                count_ok += 1
                print(f"The file {own_file.get_file_name(file)} has been sorting")
            else:
                count_fail += 1
                print(f"The file {own_file.get_file_name(file)} was not sorting")

        print(f"Out of {len(files)} photos, {count_ok} were processed and {count_fail} were skipped.")
    else:
        print("Error: SOURCE_DIRECTORY does not exist")

    return 0


if __name__ == '__main__':
    print(f'{program_description}\nversion {program_version}\n')

    batch_rename()
