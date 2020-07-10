
import os
import platform
import subprocess as sp
from argparse import ArgumentParser

if __name__ == "__main__":
    parser = ArgumentParser(description = "Converts C header files to python files")
    parser.add_argument(type=str, dest='input_file')
    args = parser.parse_args()
    print("Processing %s ..." % (args.input_file))

    input_file = os.path.abspath(args.input_file)
    base_dir, filename = os.path.split(input_file)
    filename_root, filename_ext = os.path.splitext(filename)
    
    os_name = platform.system()
    output_file = filename_root + '.py'
    if os_name == "Windows":
        ctypesgen_path = os.environ['CTYPESGEN'] + '\ctypesgen.py'
        sp.call(['python', ctypesgen_path, '--includedir="../include"', '-a', '-o', output_file, input_file])
    else:
        sp.call(['ctypesgen', '--includedir="../include"', '-a', '-o', output_file, input_file])
        
