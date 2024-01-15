import os
import shutil
# needs more
def rename(files):
#if number in format 1-9, add a 0 to the front
    if len(number) == 1:
        number = "0" + number
    # rename file
    os.rename(os.path.join(folder, file), os.path.join(folder, number + "_" + file.split("_")[1]))

def update_readme(topic, folder):
    txt = f"## {topic} \n\n"
    for file in sorted(os.listdir(folder)):
        if file.endswith(".md") and file[0].isdigit():
            number = file.split("_")[0]
            number = int(number)
            title = file.split("_")[1]
            title = title.split(".")[0]
            title = title.capitalize()
            txt += f"{number}. [{title}](/{folder}/{file})\n"
    file = open("README.md", "a")
    file.write(txt)

def linkslides(folder):
    tmp = f"{folder}/temp"
    try:
        shutil.rmtree(tmp)
    except:
        pass
    # copy contents of folder to a subfolder called temp
    shutil.copytree(folder, tmp)
    # for each numbered markdown file in the folder
    for file in sorted(os.listdir(tmp), reverse = True):
        if file.endswith(".md") and file[0].isdigit():
            # get the file number
            number = file.split("_")[0]
         

            # get the file title
            title = file.split("_")[1]
            # get the file path
            path = os.path.join(tmp, file)
            if number == "10":
                link = ""
            wfile = open(path, "a")
            wfile.write(link)
            # get the file link
            link = f"\n\n[-> {title.split('.')[0].capitalize()}](/{folder}/{file})"
            # if not the first file, append the previous file link
            
            print(link)

if __name__ == "__main__":
    #update_readme("About this Course", "about-100")
    linkslides("about-100")