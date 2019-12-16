from pythonutils.input_utils import *
from pythonutils.yes_or_no_input import *
from pythonutils.os_utils import *
import os

print("")
path = stripped_input("Enter/paste the target path: ")
recursive = yes_or_no("Recursive?")
include_dirs = yes_or_no("Include dirs?")
include_files = yes_or_no("Include files?")
paths = get_all_in_dir(path, recursive=recursive, include_dirs=include_dirs, include_files=include_files)
for path in paths:
    print(path)
    print(type(path))
    # new_path = path.sub
    # os.rename(path, )
