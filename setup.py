from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="sentence-completion",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A flexible journaling system for personal growth and self-reflection",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/sentence-completion",
    packages=find_packages(where="Core"),
    package_dir={"": "Core"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Office/Business :: News/Diary",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "click>=8.0.0",
        "rich>=10.0.0",
        "pyyaml>=6.0.0",
        "python-dateutil>=2.8.0",
    ],
    entry_points={
        "console_scripts": [
            "sentence-completion=sentence_completion.__main__:main",
        ],
    },
    include_package_data=True,
    package_data={
        "sentence_completion": ["templates/*.yaml"],
    },
) 