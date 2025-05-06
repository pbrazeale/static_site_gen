import os
import shutil

dir_path_public = "./public"
dir_path_content = "./content"

def content_file_list():
    if os.path.exists(dir_path_content):
        directories = os.listdir(path)
        for directory in directories:
            subpath = os.path.join(path, directory)
            if os.path.isdir(subpath):
                shutil.rmtree(subpath)
            else:
                os.remove(subpath)