from setuptools import setup, find_packages

setup(
    name="asv_samples",
    version="0.1.0",
    packages=find_packages(include=["asv_samples", "asv_samples.*"]),
)
