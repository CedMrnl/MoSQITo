import setuptools
import platform

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

python_requires = ">= 3.5"

# Pyleecan dependancies
install_requires = [
    "setuptools",
    "numpy>=1.18.1",
    "scipy>=1.4.1",
    "matplotlib>=3.1.3",
    "pandas",
]

tests_require = ["pytest>=5.4.1"]

setuptools.setup(
    name="mosqito",
    version="0.0.1.1",
    author="MoSQITo Developers",
    author_email="martin.glesser@eomys.com",
    description="Python Library for Electrical Engineering Computational Analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Eomys/MoSQITo",
    download_url="https://github.com/Eomys/SciDataTool/archive/0.0.1.tar.gz",
    packages=setuptools.find_packages(exclude=["documentation", "tutorials"]),
    # package_data={
    #     # Include any *.json files found in pyleecan:
    #     # '': ['*.json'],
    #     "": [""]
    # },
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=python_requires,
    install_requires=install_requires,
    tests_require=tests_require,
)
