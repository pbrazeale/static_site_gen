import os
import shutil

PUBLIC = "./docs"
STATIC = "./static"


def build_static():
    # first delete public/...
    if os.path.exists(PUBLIC):
        path = os.path.join(PUBLIC)
        directories = os.listdir(path)
        for directory in directories:
            subpath = os.path.join(path, directory)
            if os.path.isdir(subpath):
                shutil.rmtree(subpath)
            else:
                os.remove(subpath)
    # copy all dir/files and subdir/files from "static/" to "public/"
    if os.path.exists(STATIC):
        recursive_copy(STATIC, PUBLIC)
      
def recursive_copy(static_path, pbulic_path):
    for name in os.listdir(static_path):
        src = os.path.join(static_path, name)
        dst = os.path.join(pbulic_path, name)

        if os.path.isdir(src):
            os.makedirs(dst, exist_ok=True)
            recursive_copy(src, dst)
        else:
            shutil.copy(src, dst)
            print(f"Copied {src} to {dst}")