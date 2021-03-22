import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ascii-tarot", # Replace with your own username
    version="0.0.1",
    author="Dean Poulos",
    author_email="dean.poulos7@gmail.com",
    description="A command-line tool for tarot readings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/deanpoulos/ASCIITarot",
    include_package_data=True,
    project_urls={
        "Bug Tracker": "https://github.com/deanpoulos/ASCIITarot/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
