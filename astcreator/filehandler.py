# filehandler.py
# Author: Jackson Raffety

import os


class FileHandler:
    """
        A class used for interacting with files and directories.

        ...

        Methods
        --------
        validateDirectory(rootpah)
            determines whether a given directory is a valid one in the current system.

        getPythonFiles(rootpath)
            Scans a directory and its sub-directories, and returns a list of all files ending in .py

        getFileContents(file)
            opens a file and returns the contents of the file as a string.

        outputNewFile(oldFile, contents)
            creates a new file with the same name as the oldFile, but with .ast appended to the end.
            The contents of the new file are written directly from the passed contents.
     """

    @staticmethod
    def validateDirectory(rootpath):
        """
        This function takes a path to a directory and returns True or False depending on whether it is valid.

        The function prints to console any specific problem there is with the directory. Whether it does not exist,
        could not be found, or is a file and not a directory.

        Parameters
        ------------
        rootpath : string
            the directory to validate

        Returns
        ---------
        bool
            True if the directory exists and is valid. False if otherwise.
        """
        # first, check if the given path is actually found in the system
        if not os.path.exists(rootpath):
            print("Error: Given directory could not be found or does not exist.")
            return False

        # next, check if the given path is a directory or a file
        if not os.path.isdir(rootpath) or os.path.isfile(rootpath):
            print("Error: Found a file, not a directory.")
            return False

        return True

    @staticmethod
    def getPythonFiles(rootpath):
        """
        This function searches through a directory and it's subdirectories for python files, and returns them as a list.

        A file is considered a pyhton file if it has the file extension .py. The full path to every python file
        is then added to a list and returned at the end. Returns an empty list if no files were found.

        Parameters
        ------------
        rootpath : string
            The path to the directory to scan

        Returns
        ----------
        list[string]
            a list of the full path of all found python files
        """
        py_files = [] # initialize empty list to save files to
        # scan through the directory and all it's subdirectories
        for subdir, dirs, files in os.walk(rootpath):
            for file in files:
                # determine if a pyhton file if ends with .py
                if file.lower().endswith(".py"):
                    # return the full path to the found file
                    full_file = os.path.join(subdir, file)
                    py_files.append(full_file)

        return py_files

    @staticmethod
    def getFileContents(file):
        """
        This function opens a file and returns the contents of the file as a string.

        Returns an empty string if the file has no contents

        Parameters
        --------------
        file : string
            the file to open and extract the contents from

        Returns
        ------------
        str
            the contents of the opened file
        """
        return_string = ""
        with open(file) as source:
            return_string = source.read()

        return return_string

    @staticmethod
    def outputNewFile(old_file, contents):
        """
        This function creates a new file and writes the parameter contents to that file

        The new file name is the same name as the old_file, but appended with .ast.

        Parameters
        ------------
        old_file : str
            the name of the old file to base the new name after.
        contents : str
            the contents to write to the new file being created

        Returns
        ---------
        returns nothing, but creates a new file named {old_file}.ast
        """
        new_file = old_file + ".ast" # new file named the same as the old, but appended with .ast
        with open(new_file, "w") as source:
            source.write(contents)
            source.close()
            # print to console of the success of new file creation
            print("Created new file: " + new_file)
