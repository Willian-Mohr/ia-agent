from setuptools import setup, find_packages

setup(
    name="marvin-agent",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "pytest"
    ],
) 