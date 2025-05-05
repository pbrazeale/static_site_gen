import os
import shutil
import blocks

PUBLIC = "public/"
STATIC = "static/"
CONTENT = "content/"
TEMPLATE = "template.html"

def main():
    print("testing")
    build_site()
    generate_page(CONTENT, TEMPLATE, f"{PUBLIC}index.html")

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
            recursive_copy(src, dst)
        else:
            shutil.copy(src, dst)
            print(f"Copied {src} to {dst}")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as from_file:
        markdown_file = from_file.read()

    with open(template_path) as temp_file:
        template_file = temp_file.read()

    html_node = blocks.markdown_to_html_node(markdown_file)
    html_string = html_node.to_html()
    title = extract_title(markdown_file)

    html_file = temp_file.replace("{{ Title }}", title).replace("{{ Content }}", html_string)
    
    with open(dest_path, "w") as out_file:
        out_file.write(html_file)
        print(f"Wrote HTML to {dest_path}")

def extract_title(markdown):
    lines = markdown.splitlines()
    for line in lines:
        if line.startswith("# "):
           clean_line = line.lstrip("# ")
           return clean_line.strip()
    raise Exception("no title found")

main()