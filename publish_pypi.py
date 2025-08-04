#!/usr/bin/env python3
"""
Helper script for publishing enough-journal to PyPI
"""
import subprocess
import sys
import os
from pathlib import Path

def run_command(cmd, description):
    print(f"\n🔄 {description}...")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ Error: {result.stderr}")
        return False
    print(f"✅ {description} completed successfully")
    return True

def main():
    print("🚀 ENOUGH Journal - PyPI Publishing Helper")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not Path("pyproject.toml").exists():
        print("❌ Error: pyproject.toml not found. Please run this from the project root.")
        sys.exit(1)
    
    # Clean previous builds
    if not run_command("python -m build --clean", "Cleaning previous builds"):
        sys.exit(1)
    
    # Build the package
    if not run_command("python -m build", "Building package"):
        sys.exit(1)
    
    # Check the package
    if not run_command("python -m twine check dist/*", "Checking package"):
        sys.exit(1)
    
    # Test install locally
    if not run_command("pip install dist/*.whl --force-reinstall", "Testing local install"):
        sys.exit(1)
    
    print("\n✅ Package is ready for publishing!")
    print("\n📦 To publish to PyPI Test (recommended first):")
    print("   python -m twine upload --repository testpypi dist/*")
    print("\n📦 To publish to PyPI Production:")
    print("   python -m twine upload dist/*")
    print("\n⚠️  Make sure you have:")
    print("   - PyPI account and API token")
    print("   - ~/.pypirc configured with credentials")
    print("   - Version updated in pyproject.toml if needed")
    
    response = input("\n🤔 Do you want to publish to PyPI Test now? (y/N): ")
    if response.lower() in ['y', 'yes']:
        if not run_command("python -m twine upload --repository testpypi dist/*", "Publishing to PyPI Test"):
            sys.exit(1)
        print("\n✅ Published to PyPI Test!")
        print("🔗 Check: https://test.pypi.org/project/enough-journal/")

if __name__ == "__main__":
    main() 