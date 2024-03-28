# Relative and Absolute Python File Paths

In Python, file paths can be specified using either relative or absolute paths. (Remeber you might use `python3` instead of `python` in your Terminal commands, depending on your system.)

---

## Relative Paths

Relative paths are specified relative to the current working directory of the script or the location from where the script is executed.

 Assuming the current directory contains a folder named `build` with a file named `main.py`, this line would run the python code inside `build/main.py`:

`python main.py`

## Absolute Paths

Absolute paths specify the complete path from the root directory of the file system to the desired file or directory. You can get the absolute path of a file by dragging it into the terminal window. 

This would run the same  `main.py` code as above, this time referencing the absolute path. 

`python '/home/user/projects/project_name/data/file.txt'`

Absolute paths are different on different computers, whereas relative paths are the same assuming the same directory contents. 

---

### When to Use Each?

- **Relative Paths**: Convenient for referencing files within the project structure, making code more portable.
- **Absolute Paths**: Necessary when the file's location is fixed and independent of the execution environment or when accessing files outside the project directory.

---

Understanding relative and absolute paths helps in managing file operations effectively in Python scripts.
