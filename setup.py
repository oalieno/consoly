from setuptools import setup
from consoly import __version__

with open('README.md') as f:
    long_description = f.read()

setup(
    name = 'consoly',
    version = __version__,
    description = 'elegant console logger for python',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    author = 'oalieno',
    author_email = 'jeffrey6910@gmail.com',
    python_requires = '>=3.6',
    url = 'https://github.com/OAlienO/consoly',
    packages = ['consoly', 'consoly.formatter'],
    include_package_data = True,
    keywords = 'color console terminal ansi text hues logging logger',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)

