import setuptools

pacakge_name = "abc_core"


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("VERSION", "r", encoding="utf-8") as fh:
    version_number = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    install_requires = fh.read().splitlines()

setuptools.setup(
    name=pacakge_name,
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
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    python_requires=">=3.9",
    test_suite="tests/",
)
