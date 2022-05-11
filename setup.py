import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="html-jingfelix",
    version="0.0.2",
    author="Felix Jing",
    author_email="jingfelix@outlook.com",
    description="build html dom as python objects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jingfelix/htmlobj",
    project_urls={
        "Bug Tracker": "https://github.com/jingfelix/htmlobj/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.5",
)
