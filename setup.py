import sys
import glob
import numpy

try:
    from setuptools import setup
    from setuptools import Extension
except ImportError:
    from distutils.core import setup
    from distutils.extension import Extension
#
# Force `setup_requires` stuff like Cython to be installed before proceeding
#
from setuptools.dist import Distribution
Distribution(dict(setup_requires='Cython'))

try:
    from Cython.Distutils import build_ext
except ImportError:
    print("Could not import Cython.Distutils. Install `cython` and rerun.")
    sys.exit(1)
    
# Check for GPU support
GPU_SUPPORT = False
try:
    import pycuda
    import skcuda
    print("GPU support found. Will build GPU extensions.")
    GPU_SUPPORT = True
except ImportError:
    print("No GPU support found. Continuing install.")
    pass
    
    


# from distutils.core import setup, Extension
# from Cython.Distutils import build_ext



# Build extensions 
module1 = Extension(    name         = "openpiv.process",
                        sources      = ["openpiv/src/process.pyx"],
                        include_dirs = [numpy.get_include()],
                    )
                    
module2 = Extension(    name         = "openpiv.lib",
                        sources      = ["openpiv/src/lib.pyx"],
                        include_dirs = [numpy.get_include()],
                    )
                    
if(GPU_SUPPORT == True):
    module3 = Extension(    name         = "openpiv.gpu_process",
                            sources      = ["openpiv/src/gpu_process.pyx"],
                            include_dirs = [numpy.get_include()], 
                       )                 

# a list of the extension modules that we want to distribute
if(GPU_SUPPORT == True):
    ext_modules = [module1, module2, module3]
else:
    ext_modules = [module1, module2]


# Package data are those filed 'strictly' needed by the program
# to function correctly.  Images, default configuration files, et cetera.
package_data =  [ 'data/defaults-processing-parameters.cfg', 
                  'data/ui_resources.qrc',
                  'data/images/*.png',
                  'data/icons/*.png',
                ]


# data files are other files which are not required by the program but 
# we want to ditribute as well, for example documentation.
data_files = [ ('openpiv/examples/tutorial-part1', glob.glob('openpiv/examples/tutorial-part1/*') ),
               ('openpiv/examples/masking_tutorial', glob.glob('openpiv/examples/masking_tutorial/*') ),
               ('openpiv/docs/openpiv/examples/example1', glob.glob('openpiv/docs/examples/example1/*') ),
               ('openpiv/docs/openpiv/examples/gurney-flap', glob.glob('openpiv/docs/examples/gurney-flap/*') ),
               ('openpiv/docs/openpiv', ['README.md'] ),
               ('openpiv/data/ui', glob.glob('openpiv/data/ui/*.ui') ),
             ]


# packages that we want to distribute. THis is how
# we have divided the openpiv package.
packages = ['openpiv', 'openpiv.ui']


setup(  name = "OpenPIV",
        version = "0.20.9",
        author = "OpenPIV contributors",
        author_email = "openpiv-users@googlegroups.com",
        description = "An open source software for PIV data analysis",
        license = "GNU General Public License v3 (GPLv3)",
        url = "http://www.openpiv.net",
        long_description =  """OpenPIV is a set of open source algorithms and methods
                            for the state-of-the-art experimental tool
                            of Particle Image Velocimetry (PIV) which 
                            are free, open, and easy to operate.""",
                            
        ext_modules = ext_modules, 
        packages = packages,
        cmdclass = {'build_ext': build_ext},
        package_data = {'': package_data},
        data_files = data_files,
        install_requires = ['scipy','numpy','cython','scikit-image == 0.14.5','progressbar2 == 3.53.1', 'networkx == 2.2', 'decorator == 4.4.2', 'cloudpickle == 1.3.0', 'pywavelets == 1.0.3', 'python_utils == 2.4.0'],
        classifiers = [
        # PyPI-specific version type. The number specified here is a magic constant
        # with no relation to this application's version numbering scheme. *sigh*
        'Development Status :: 4 - Beta',

        # Sublist of all supported Python versions.
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',

        # Sublist of all supported platforms and environments.
        'Environment :: Console',
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',

        # Miscellaneous metadata.
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering',
    ]
)

