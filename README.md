# Python_AST_Creator
============

Description
----------
A basic python package that takes a path to a directory as an argument and creates AST (Abstract Syntax Tree) files from found python files.
The program searches the directory and all of it's subdirectories for python files (*.py) and then creates an AST from the code in the file.
The program creates a file containting the plaintext of the created AST in the same directory as the found file, with the name *.py.ast.

Installation
--------------
Download this project as a ZIP and extract, or clone the project via:
```bash
git clone https://github.com/JacksonRaffety/Python_AST_Creator
```

Then, in the directory with setup.py, install:
```bash
pip install .
```

Running the Program
----------------------
```bash
# running in same directory
python astcreator <path to directory to search>

# running in other directory
python <path to astcreator> <path to directory to search>

# example
python ./astcreator ../../myPythonProject
```

Testing
--------------
Tests made using pytest. To test, use the pytest command:
```bash
# in local directory
pyetst

# in other directory
pytest <path to installed directory>
