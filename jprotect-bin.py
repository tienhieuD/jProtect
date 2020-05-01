#!python
# cython: language_level=3
import argparse
import os
import re
import sys
from distutils.core import setup
from distutils.extension import Extension

from Cython.Distutils import build_ext

from helper.separate_dir import separate_dir, get_files_in_dir


if __name__ == '__main__':  # RUN
    parser = argparse.ArgumentParser(description='Process some args for jProtect')
    parser.add_argument('-fr', '--from_dir', required=True, help='Folder contains list add-ons.')
    parser.add_argument('-to', '--to_dir', help='Folder to save after compile add-ons.')
    parser.add_argument('-in', '--includes', nargs='+', help='File path must include all regex.')
    parser.add_argument('-ex', '--excludes', nargs='+', help='File will be passed if include one of regex in list.')
    parser.add_argument('-nm', '--name', help='Name of project (optional).')

    args = parser.parse_args()
    name = args.name or 'JPROTECT'
    fromDirectory = args.from_dir  # or 'D:\\myaddon\\tristar_project\\073.Odoo_TriStar\\trunk\\3. SourceCode\\addons'
    toDirectory = args.to_dir or (os.path.dirname(__file__) + '/dist')
    includes = args.includes  # or ['.+?models.+?', '.+?tristar.+?']
    excludes = args.excludes  # or ['.+?__.py', '.+?tristar_payslip_sumary_canteen_foreign.py']

    separate_dir(fromDirectory, toDirectory, includes, excludes)
    files = get_files_in_dir(toDirectory)
    ext_modules = []
    to_remove_files = []
    for file_path in files:
        if 'jprotect_' in file_path:
            module_name = file_path.split(os.path.dirname(__file__))[-1].replace('\\', '.')[1:-3]
            ext_modules.append(Extension(module_name, [file_path]), )
            to_remove_files += [file_path]
    for extension in ext_modules:
        extension.cython_directives = {'language_level': "3"}

    sys.argv = [sys.argv[0], 'build_ext', '--inplace']
    setup(name=name, cmdclass={'build_ext': build_ext}, ext_modules=ext_modules)

    for remove_file_path in to_remove_files:
        if os.path.exists(remove_file_path):
            os.remove(remove_file_path)
            os.remove(remove_file_path[:-3] + '.c')

    complied_files = get_files_in_dir(toDirectory, ext=['.pyd', '.so'])
    for file_path in complied_files:
        new_name = re.sub(r'(.+?jprotect_\w+?)\.(.+?)\.(pyd|so)', r'\g<1>.\g<3>', file_path)
        os.rename(file_path, new_name)
