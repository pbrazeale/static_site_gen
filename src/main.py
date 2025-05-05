import os
import shutil

from copystatic import build_static
from gencontent import generate_page

dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    build_static()
    print("Generating page...")
    generate_page(
        os.path.join(dir_path_content, "index.md"),
        template_path,
        os.path.join(dir_path_public, "index.html"),
    )


main()