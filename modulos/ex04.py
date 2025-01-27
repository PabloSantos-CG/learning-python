

import os
import shutil


HOME = os.path.expanduser('~')
ORIGINAL_FOLDER = os.path.join(HOME, "Pictures", "img_ia")
COPY_FOLDER = os.path.join(HOME, "Pictures", "NOVA_PASTA")

os.makedirs(COPY_FOLDER, exist_ok=True)

for root, dirs, files in os.walk(ORIGINAL_FOLDER):
    for dir_ in dirs:
        new_folder = os.path.join(
            root.replace(ORIGINAL_FOLDER, COPY_FOLDER), dir_
        )
        os.makedirs(new_folder, exist_ok=True)

    for file in files:
        path_actual = os.path.join(root, file)
        path_for_new_copy = os.path.join(
            root.replace(ORIGINAL_FOLDER, COPY_FOLDER), file
        )
        shutil.copy(path_actual, path_for_new_copy)