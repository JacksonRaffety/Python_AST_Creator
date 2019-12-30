# main.py
# author: Jackson Raffety

import ast
import sys
from filehandler import FileHandler
import astpretty


def main():
    """
    This function represents the main logic of the program. It scans through a directory, and creates an
    Abstract Syntax Tree for each python file it finds, and outputs it to a new file.

    The system prematurely exits if there is no directory given, if the given directory does not exist or is a file,
    or if no python files could be found from the directory.

    Parameters
    ------------
    sys.argv[1] : str
        the directory to search through in the program
    """
    # if no arugments were given to the function, exit prematurely
    if len(sys.argv) < 2:
        print("Missing Arguments Error: Please provide a path to a directory.")
        sys.exit(1)

    # set the directory to the first argument given
    rootpath = sys.argv[1]

    # determine if the directory is valid to use or not
    if not FileHandler.validateDirectory(rootpath):
        sys.exit(1)

    # get all pyhton files found from the directory
    python_files = FileHandler.getPythonFiles(rootpath)

    # if the directory and its subdirectories contain no python files, alert the user and exit.
    if len(python_files) == 0:
        print("No python files could be found from the directory given.")
        sys.exit(0)

    # create an AST for each python file and export the tree
    for file in python_files:
        # open the file and extract the contents
        file_contents = FileHandler.getFileContents(file)

        try:
            # parse and create the AST from the file contents
            head_node = ast.parse(file_contents)
            # use astpretty to create detailed output form of the AST
            output_string = astpretty.pformat(head_node, indent="    ", show_offsets=False)
            # output this AST to a new file
            FileHandler.outputNewFile(file, output_string)
        except SyntaxError as err:
            # in case the parser cannot parse due to a syntax error, alert the user
            print("Error: Syntax Error found while parsing file " + file + " -- ", err)


# run the program
if __name__ == "__main__":
    main()
