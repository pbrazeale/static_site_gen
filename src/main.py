import os
import shutil

from copystatic import build_static
from gencontent import generate_page, find_content

dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    build_static()
    print("Generating page...")
    find_content(dir_path_content, template_path, dir_path_public)


main()