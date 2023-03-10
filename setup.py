import setuptools
# from Cython.Build import cythonize



# Package Settings
__package_name__ = "pybulldozer"
__app_name__ = "pybulldozer"
__version__ = "0.0.3"
__author__ = 'Mike Huls'
__license__ = "MIT"
__maintainer__ = "Mike Huls"
__email__ = "mikehuls42@gmail.com"
__status__ = "Development"
__description__ = "pybulldozer aims to make working with non-relation data files as easy as possible"
__project_url__ = "https://github.com/mike-huls/pybulldozer"


# Reads the content of your README.md into a variable to be used in the setup below
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


# extensions = [
#     setuptools.Extension(
#         "test",
#          sources=["ext/pyx/test.cp39-win_amd64.pyd"],
#         include_dirs=['ext/pyx/']
    # ),
# ]



setuptools.setup(
    name=__package_name__,
    packages=[__package_name__],
    # For including non-python files (in this example all files in the ./files folder)
    # package_data={'': ['files/*']},
    version=__version__,
    license=__license__,
    description=__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=__author__,
    author_email=__email__,
    url=__project_url__,

    # ext_modules=cythonize(extensions),
    # ext_modules=extensions,
    # ext_modules=[setuptools.Extension('test', sources=['ext/pyx/test.c'])],


    project_urls = {
        # "Bug Tracker": "https://github.com/profile/project/issues"
    },
    # Entry points make CLI access possible
    # entry_points={
    #     'console_scripts': [
    #         f'pybulldozer=pybulldozer.cli:main',
    #     ],
    # },
    # Add packages that need to be installed along this package:
    install_requires=['colorama'],
    # Describe this package in a few keywords:
    keywords=[],
    # https://pypi.org/classifiers
    classifiers=[                                   
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ]
)