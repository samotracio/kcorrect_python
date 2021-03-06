from distutils.core import setup, Extension
try:
    import numpy
except ImportError:
    raise SystemExit('requires NumPy version > 1.7.0') 

import os
try:
    kcorrect_dir = os.environ['KCORRECT_DIR']
except KeyError:
    raise SystemExit('KCORRECT_DIR must be set') 
    
INC_DIR = [os.path.join(kcorrect_dir,'include'),
           numpy.get_include()]
LIB_DIR = [os.path.join(kcorrect_dir,'lib')]
modulekcorrect = Extension('_kcorrect',
                           include_dirs = INC_DIR,
                           libraries = ['kcorrect', 'm'],
                           library_dirs = LIB_DIR,
                           sources = ['src/_kcorrectmodule.c'])
moduleztransform = Extension('_ztransform',
                           include_dirs = INC_DIR,
                           libraries = ['kcorrect', 'm'],
                           library_dirs = LIB_DIR,
                           sources = ['src/_ztransformmodule.c'])

setup (name = 'kcorrect_python',
       version = '2017.07.05',
       description = 'Python wrapper for Kcorrect library',
       url = 'https://github.com/nirinA/kcorrect_python',
       author = 'nirina raseliarison',
       author_email = 'nirina.raseliarison@gmail.com',
       ext_modules = [modulekcorrect, moduleztransform],
       packages =['kcorrect', 'kcorrect.ztransform', 'kcorrect.utils'],
       license = 'Public Domain')
