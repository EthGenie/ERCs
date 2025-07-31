from setuptools import setup, find_packages

setup(
    name="erc-check",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "sentence-transformers",
        "faiss-cpu",
        "markdown",
        "beautifulsoup4"
    ],
    entry_points={
        "console_scripts": [
            "erc-check=erc_check.cli:main"
        ]
    }
)
