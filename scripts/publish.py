#!/usr/bin/env python3
"""
Publish script for ENOUGH journal package.
This script automates the process of building and uploading to PyPI.
"""
import os
import shutil
import subprocess
from pathlib import Path

def clean_build_dirs():
    """Remove old build artifacts."""
    dirs_to_clean = ['build', 'dist', '*.egg-info']
    for dir_pattern in dirs_to_clean:
        for path in Path('.').glob(dir_pattern):
            if path.is_dir():
                shutil.rmtree(path)
            else:
                path.unlink()
    print("✓ Cleaned build directories")

def install_build_deps():
    """Install required build tools."""
    subprocess.run([
        'pip', 'install', '--upgrade',
        'pip', 'build', 'twine'
    ], check=True)
    print("✓ Installed build dependencies")

def build_package():
    """Build source and wheel distributions."""
    subprocess.run(['python', '-m', 'build'], check=True)
    print("✓ Built package distributions")

def upload_to_pypi():
    """Upload the built distributions to PyPI."""
    subprocess.run(['python', '-m', 'twine', 'upload', 'dist/*'], check=True)
    print("✓ Uploaded to PyPI")

def main():
    """Run the publish workflow."""
    try:
        clean_build_dirs()
        install_build_deps()
        build_package()
        upload_to_pypi()
        print("\n✨ Successfully published to PyPI!")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error during publishing: {e}")
        exit(1)

if __name__ == "__main__":
    main() 