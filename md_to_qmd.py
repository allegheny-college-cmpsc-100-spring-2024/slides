import os

template = """
---
title: "TITLE"
subtitle: "CMPSC 100: Computational Expression, Spring 2025"
author: "Morgan Green"
slide-number: true
format:
  revealjs: 
    theme: [dark, ../custom.scss]
touch: true
controls: true
---

"""
def md_to_qmd(md_folder, template=template):
    folder = md_folder
    # copy folder to qmd
    os.system(f"cp -r {folder} qmd")
    output_file = f"qmd/{folder}/index.qmd"
    template = template.replace("TITLE", folder.replace("-", " ").title())
    with open(output_file, "a") as f:
        f.write(template)
    
        for file in sorted(os.listdir(folder)):
            if file.endswith(".md"):
                f.write("::: incremental\n")
                for line in open(f"{folder}/{file}").readlines():
                    if "[->" in line:
                        continue
                    f.write(f"{line}")
                f.write(":::\n")
                # delete copy in qmd folder
                os.system(f"rm -r qmd/{folder}/{file}")

if __name__ == "__main__":
    # for each directory not named "qmd" and not starting with ., run md_to_qmd
    for directory in os.listdir("."):
        if directory != "qmd" and "." not in directory:
            md_to_qmd(directory)

