import datetime
import os
from application import doc_scripts


def create_folder_with_name(name: str):
    items = os.listdir("c:/")
    if name not in items:
        os.mkdir(f"c:/{name}")


def create_random_file_in_my_random_files():
    create_folder_with_name("random files")
    date = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S-%f")
    file_name = f"c:/random files/{date}.txt"
    open(file_name, 'w+').close()


# printing doc scripts
print(doc_scripts.__doc__)

# create_folder_with_name("shapoor")
create_random_file_in_my_random_files()
