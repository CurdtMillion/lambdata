# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="another-lambdata", # the name that you will install via pip
    version="1.1",
    author="Curdt Million",
    author_email="curtcecil@gmail.com",
    description="A second try at doing Sprint 1 from Unit 3",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/CurdtMillion/lambdata",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)
