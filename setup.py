import os
import sys

from setuptools import setup
from setuptools import find_packages
from setuptools.command.install import install


__version__ = "0.1.0"

with open("README.md", "r") as fh:
    long_description = fh.read()


def get_requirements(filename):
    with open(filename, "r", encoding="utf-8") as fp:
        reqs = [x.strip() for x in fp.read().splitlines()
                if not x.strip().startswith('#') and not x.strip().startswith('-i')]
    return reqs


class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version"""
    description = 'verify that the git tag matches our version'

    def run(self):
        tag = os.getenv('CI_COMMIT_TAG')

        if tag != f"v{__version__}":
            info = "Git tag: {0} does not match the version of this app: {1}".format(
                tag, __version__
            )
            sys.exit(info)


setup(
    name="doge",
    version=__version__,
    author="GetInData",
    author_email="office@getindata.com",
    description="Data Online Generator",
    long_description=long_description,
    url="https://gitlab.com/getindata/streaming-labs/doge",
    packages=find_packages(),
    python_requires='>=3.8',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    install_requires=get_requirements('requirements.txt'),
    py_modules=['doge'],
    cmdclass={
        'verify': VerifyVersionCommand,
    }
)