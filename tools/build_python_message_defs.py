
import os
import subprocess as sp
import sys
from argparse import ArgumentParser

PARSER = 'ctypeslib' # ctypeslib or ctypesgen

if PARSER == 'ctypeslib':
    from ctypeslib import clang2py
elif PARSER == 'ctypesgen':
    from ctypesgen import main as ctg_main

if __name__ == "__main__":
    parser = ArgumentParser(description = "Converts C header files to python files")
    parser.add_argument(type=str, dest='input_file')
    parser.add_argument(type=str, dest="output_file", default=None)
    args = parser.parse_args()
    print("Processing %s ..." % (args.input_file))

    input_file = os.path.abspath(args.input_file)
    base_dir, filename = os.path.split(input_file)
    filename_root, filename_ext = os.path.splitext(filename)

    py_exe = sys.executable # path to same version of python that called this script

    if PARSER == 'ctypeslib':
        if args.output_file is None:
            output_file = os.path.join(base_dir, filename_root) + '.py'
        else:
            output_file = args.output_file
        clang2py_path = clang2py.__file__ # path to clang2py.py
        args = ['-c', '-k', 'cdefmstu', '-o', output_file, input_file]
        sp.call([py_exe, clang2py_path] + args)
    elif PARSER == 'ctypesgen':
        if args.output_file is None:
            output_file = filename_root + '.py'
        else:
            output_file = args.output_file
        args = ['--includedir="../include"', '-a', '-o', output_file, input_file]
        ctg_main.main(args)
        
    
