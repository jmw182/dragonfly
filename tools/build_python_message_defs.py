import os
import platform
import subprocess as sp
from argparse import ArgumentParser

if __name__ == '__main__':
    parser = ArgumentParser(description = 'Converts C header files to python files')
    parser.add_argument(type=str, dest='input_file')
    args = parser.parse_args()
    print('Processing %s ...' % (args.input_file))

    input_file = os.path.abspath(args.input_file)
    base_dir, filename = os.path.split(input_file)
    filename_root, filename_ext = os.path.splitext(filename)
    
    os_name = platform.system()
    if os_name == 'Linux':
        # This needs updated to call clang2py
        xml_file = os.path.join(base_dir, filename_root) + '.xml'
        sp.call(['h2xml', '-c', '-o', xml_file, input_file])
        out_file = os.path.join(base_dir, filename_root) + '.py'
        sp.call(['xml2py', '-o', out_file, xml_file])

    elif os_name == 'Windows':
        output_file = os.path.join(base_dir, filename_root) + '.py'
        python_base = os.environ['PYTHON3_BASE']
        clang2py = os.path.join(python_base, 'Lib\site-packages\ctypeslib\clang2py.py')
        sp.call(['python', clang2py, '-c', '-k', 'cdefmstu', '-o', output_file, input_file])