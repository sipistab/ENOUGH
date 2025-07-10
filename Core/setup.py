"""
ENOUGH - A command-line journaling system for mindful reflection
"""

from setuptools import setup, find_packages

setup(
    name="enough-journal",
    version="1.0.0",
    description="A focused command-line journaling system that emphasizes mindful reflection through structured prompts",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="Sipos Istvan | Stephen Piper",
    author_email="sipistab@gmail.com",
    url="https://github.com/sipistab/ENOUGH",
    packages=find_packages(where="Core"),
    package_dir={"": "Core"},
    include_package_data=True,
    install_requires=[
        'cryptography>=3.4.7',
        'pyyaml>=5.4.1',
        'rich>=10.2.2',
        'prompt_toolkit>=3.0.18',
    ],
    entry_points={
        'console_scripts': [
            'enough=enough.__main__:main',
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Office/Business :: News/Diary",
        "Topic :: Text Processing :: General",
    ],
    python_requires=">=3.8",
) 