import os
import shutil

def main():
    build_site()

def build_site():
    # first delete public/...
    if os.path.exists("../public/"):
        shutil.rmtree("../public/")



    # copy all dir/files and subdir/files from "static/" to "public/"

    # log the path of each file copied
    pass

main()