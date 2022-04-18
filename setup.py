from setuptools import find_packages, setup
from cicd_sample_python_project import __version__

setup(
    name="cicd_sample_python_project",
    packages=find_packages(exclude=["tests", "tests.*"]),
    setup_requires=["wheel"],
    version=__version__,
    description="cicd sample python project",
    author="wchen@odeko.com",
)
