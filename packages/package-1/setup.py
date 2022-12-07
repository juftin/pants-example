import numpy
from Cython.Build import cythonize
from setuptools import setup, find_packages, Extension

extensions = [
    Extension(
        "package_1.foo",
        ["package_1/foo.pyx"],
        include_dirs=[numpy.get_include()],
    ),
]

setup(
    name="package-1",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    ext_modules=cythonize(extensions, compiler_directives={"language_level": 3}),
    install_requires=[
        "numpy>=1,<2",
        "scipy>=1,<2",
    ],
)
