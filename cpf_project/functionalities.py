import os
from pathlib import Path
from random import randint
from datetime import datetime


def random_digits():
    get_time_now = datetime.today().microsecond
    get_random_digits = randint(10000, 99999)
    return (get_time_now, get_random_digits)


def clean_terminator():
    return os.system("clear") if os.name in "posix" else os.system("cls")


def check_is_exists_folder():
    folder_name = "cpfs"
    cpf_folder = Path(folder_name)

    if not cpf_folder.exists():
        return os.mkdir(path=cpf_folder, mode=0o750)
