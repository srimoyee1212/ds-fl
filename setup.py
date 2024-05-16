import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "ds-fl"
AUTHOR_USER_NAME = "srimoyee1212"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "entbappy73@gmail.com"


setuptools.setup(
    name="ds-fl",
    version=__version__,
    author="srimoyee1212",
    author_email="srimoyeem1@gmail.com",
    description="A small python package for ml app",
    long_description="",
    long_description_content="text/markdown",
    url=f"https://github.com/srimoyee1212/ds-fl",
    project_urls={
        "Bug Tracker": f"https://github.com/github.com/srimoyee1212/ds-fl/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)