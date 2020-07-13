
import os
import subprocess as sp
import sys
from argparse import ArgumentParser
from ctypeslib import clang2py

if __name__ == "__main__":
    parser = ArgumentParser(description = "Converts C header files to python files")
    parser.add_argument(type=str, dest='input_file')
    args = parser.parse_args()
    print("Processing %s ..." % (args.input_file))

    input_file = os.path.abspath(args.input_file)
    base_dir, filename = os.path.split(input_file)
    filename_root, filename_ext = os.path.splitext(filename)
    output_file = os.path.join(base_dir, filename_root) + '.py'

    py_exe = sys.executable # path to same version of python that called this script
    clang2py_path = clang2py.__file__ # path to clang2py.py
    args = ['-c', '-k', 'cdefmstu', '-o', output_file, input_file]
    sp.call([py_exe, clang2py_path] + args)