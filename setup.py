from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    name="excel2python",
    version="datasplit",
    author="Sewedo",
    author_email="todowede@gmail.com",
    description="Replace excel macro to split master file into countries",
    long_description=readme,
    url="https://github.com/todowede/PHSM-Data-Cleaning/",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
