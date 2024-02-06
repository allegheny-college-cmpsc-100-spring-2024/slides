import os
import shutil
import re
import sys
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
            try:
                index = re.search('[A-Z]', title).start()
                title = title[:index].capitalize() + ' ' + title[index:].capitalize()
            except:
                title = title.capitalize()
            txt += f"{number}. [{title}](/{folder}/{file})\n"
    file = open("README.md", "a")
    file.write(txt)

def unlinkslides(folder):
    # for each numbered markdown file in the folder
    # remove the last line
    for file in sorted(os.listdir(folder), reverse = True):
        if file.endswith(".md") and file[0].isdigit():
            # get the file path
            path = os.path.join(folder, file)
           
            file = open(path, "r")
            lines = file.readlines()
            lines = lines[:-1]
            wfile = open(path, "w")
            wfile.write("\n".join(lines))
         

def linkslides(folder):
    tmp = f"{folder}/temp"
    try:
        shutil.rmtree(tmp)
    except:
        pass
    # copy contents of folder to a subfolder called temp
    shutil.copytree(folder, tmp)
    # delete al lfiles in subfolder that are not numbered markdown files
    for file in os.listdir(tmp):
        if not file.endswith(".md") or not file[0].isdigit():
            os.remove(os.path.join(tmp, file))
    # for each numbered markdown file in the folder
    for file in sorted(os.listdir(tmp), reverse = True):
        if file.endswith(".md") and file[0].isdigit():
            # get the file number
            number = file.split("_")[0]
        
            # get the file title
            title = file.split("_")[1]
            title.split('.')[0]
            # get the file path
            path = os.path.join(tmp, file)
            # get the highest number file in folder
            if (int(number) == len(os.listdir(tmp))):
                link = ""
            wfile = open(path, "a")
            wfile.write(link)
            # convert title to title case
            
            # search for first uppercase letter in title
            try:
                index = re.search('[A-Z]', title).start()
                title = title[:index].capitalize() + ' ' + title[index:].capitalize()
            except:
                title = title.capitalize()
            title = title.split('.')[0]

            
            # get the file link
            link = f"\n\n[-> {title}](/{folder}/{file})"
            # if not the first file, append the previous file link
            
            print(link)

if __name__ == "__main__":
    
    folder = "while-true"
    header = "Animations and Loops (2/6)"
    #unlinkslides(folder)
    #sys.exit()
    linkslides(folder)
    update_readme(header, folder)