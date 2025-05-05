import os
import shutil

def main():
    print("testing")
    build_site()

def build_site():
    # first delete public/...
    if os.path.exists("public/"):
        directories = os.listdir("public/")
        for directory in directories:
            if os.path.isdir(directory):
                shutil.rmtree(f'public/{directory}')
            else:
                os.remove(f'public/{directory}')



    # copy all dir/files and subdir/files from "static/" to "public/"

    # log the path of each file copied
    pass

main()