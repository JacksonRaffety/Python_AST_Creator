import pytest
import _pytest

from astcreator.filehandler import FileHandler


def test_validateDirectorySuccess(tmp_path):
    directory = tmp_path
    assert FileHandler.validateDirectory(directory) is True


def test_validateDirectoryFailure(tmp_path):
    file = tmp_path / "test.txt"
    assert FileHandler.validateDirectory(file) is False

def test_getPythonFiles(tmpdir):
    directory = tmpdir.mkdir("dir")
    f1 = directory.join("test.txt")
    f2 = directory.join("test.py")
    f3 = directory.join("python.py")

    # create stubs so the files will actually be created to be found
    f1.write("stub")
    f2.write("stub")
    f3.write("stub")

    expected_result = [f2.strpath, f3.strpath]

    result = FileHandler.getPythonFiles(directory)
    assert all([a == b] for a, b in zip(expected_result, result))

def test_getFileContents(tmpdir):
    directory = tmpdir.mkdir("dir")
    file = directory.join("test.py")

    # the contents to extract from the file
    contents = "these are the expected contents from the file"
    file.write(contents)

    assert contents == FileHandler.getFileContents(file)
