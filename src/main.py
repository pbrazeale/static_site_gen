import os
import shutil

PUBLIC = "public/"
STATIC = "static/"

def main():
    print("testing")
    build_site()

def build_site():
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
            recusive_copy(src, dst)
        else:
            shutil.copy(src, dst)
            print(f"Copied {src} to {dst}")


main()