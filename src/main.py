import os
import shutil
import sys

from copystatic import build_static
from gencontent import generate_page, find_content

dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    if sys.argv[1]:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    build_static()
    print("Generating page...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath)


main()