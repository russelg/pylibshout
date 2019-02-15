"""Python libshout2 interface

Based on the c-libary libshout 2 and built with Cython
"""
from distutils.extension import Extension
from distutils.core import setup


classifiers = """\
Development Status :: 3 - Alpha
Intended Audience :: Developers
Programming Language :: Python
Topic :: Software Development :: Libraries :: Python Modules
Topic :: Multimedia :: Sound/Audio
Operating System :: OS Independent
"""


VERSION = '1.0.0'

try:
    from Cython.Distutils import build_ext
except ImportError:
    have_cython = False
else:
    have_cython = True

doclines = __doc__.split("\n")

if have_cython:
    ext_modules = [Extension(
        "pylibshout", ["pylibshout.pyx"],
        include_dirs=['/usr/local/Cellar/libshout/2.4.1/include/'],
        library_dirs=['/usr/local/Cellar/libshout/2.4.1/lib/'],
        libraries=['shout']  # .h files
    )]

    setup(
        name='pylibshout',
        version=VERSION,
        author='Leon Bogaert',
        author_email='leon@vanutsteen.nl',
        url='http://github.com/LeonB/pylibshout',
        platforms=["any"],
        description=doclines[0],
        classifiers=filter(None, classifiers.split("\n")),
        long_description="\n".join(doclines[2:]),
        # py_modules = ['pylibshout'],
        ext_modules=ext_modules,
        cmdclass={'build_ext': build_ext},
        requires=['Cython']
    )
else:
    ext_modules = [Extension("pylibshout",
                             ["pylibshout.c"],
                             libraries=["shout"])]

    setup(
        name='pylibshout',
        version=VERSION,
        author='Leon Bogaert',
        author_email='leon@vanutsteen.nl',
        url='http://github.com/LeonB/pylibshout',
        platforms=["any"],
        description=doclines[0],
        classifiers=filter(None, classifiers.split("\n")),
        long_description="\n".join(doclines[2:]),
        # py_modules = ['pylibshout'],
        ext_modules=ext_modules
    )
