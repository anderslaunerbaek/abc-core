import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("VERSION", "r", encoding="utf-8") as fh:
    version_number = fh.read()

setuptools.setup(
    name="abc-core",
    version=version_number,
    author="Anders Launer Baek-Petersen",
    author_email="anderslaunerbaek@gmail.com",
    description="TODO",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anderslaunerbaek/abc-core/",
    project_urls={
        "Bug Tracker": "https://github.com/anderslaunerbaek/abc-core//issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "abc-core"},
    packages=setuptools.find_packages(where="abc-core"),
    python_requires=">=3.9",
)
