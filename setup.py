from setuptools import setup, find_packages

setup(
    name="asv_samples",
    version="0.1.0",
    description="A set of asv samples",
    long_description=open('readme.md').read(),
    long_description_content_type='text/markdown',
    author="Rohit Goswami",
    author_email="rgoswami@ieee.org",
    url="https://github.com/HaoZeke/asv_samples",
    license="LICENSE",
    packages=find_packages(include=["asv_samples", "asv_samples.*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    project_urls={
        "Bug Tracker": "https://github.com/HaoZeke/asv_samples/issues",
    }
)
