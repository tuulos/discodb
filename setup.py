import glob
from distutils.core import setup, Extension

discodb_module = Extension('discodb._discodb',
                           sources=['python/discodbmodule.c'] + glob.glob('./src/*.c'),
                           include_dirs=['./src'],
                           libraries=['cmph'])

setup(name='discodb',
      version='0.2',
      description='An efficient, immutable, persistent mapping object.',
      author='Nokia Research Center',
      ext_modules=[discodb_module],
      package_dir = {'': 'python'},
      packages=['discodb'])
