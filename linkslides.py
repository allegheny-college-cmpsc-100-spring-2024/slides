import os
def linkslides(folder):
    # for each numbered markdown file in the folder
    for file in sorted(os.listdir(folder)):
        if file.endswith(".md") and file[0].isdigit():
            # get the file number
            number = file.split("_")[0]
            # if number in format 1-9, add a 0 to the front
            # if len(number) == 1:
            #     number = "0" + number
            # # rename file
            # os.rename(os.path.join(folder, file), os.path.join(folder, number + "_" + file.split("_")[1]))

            # get the file title
            title = file.split("_")[1]
            # get the file path
            path = os.path.join(folder, file)
            # if not the first file, append the previous file link
            if number != "10":
                wfile = open(path, "w")
                wfile.write(link)

            # get the file link
            link = f"[next: {title}]({folder}/blob/main/{file})"
            print(link)

if __name__ == "__main__":
    linkslides("about-100")