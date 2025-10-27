from setuptools import setup, find_packages

setup(
    name="Avox",
    version="1.0.0",
    author="Aditya Gotekar",
    description="A simple Python module for converting speech to text.",
    packages=find_packages(),
    install_requires=[
        "speechrecognition",
        "pyaudio",
    ],
    python_requires=">=3.8",
)
