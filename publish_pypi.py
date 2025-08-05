#!/usr/bin/env python3
"""
PyPI Publishing Script for ENOUGH Journal
Automates the process of building and uploading to PyPI
"""

import os
import subprocess
import sys
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"Error: {e.stderr}")
        return None

def check_prerequisites():
    """Check if required tools are installed"""
    print("🔍 Checking prerequisites...")
    
    # Check if twine is installed
    try:
        import twine
        print("✅ twine is installed")
    except ImportError:
        print("❌ twine is not installed. Installing...")
        run_command("pip install twine", "Installing twine")
    
    # Check if build is installed
    try:
        import build
        print("✅ build is installed")
    except ImportError:
        print("❌ build is not installed. Installing...")
        run_command("pip install build", "Installing build")

def build_package():
    """Build the package"""
    print("\n📦 Building package...")
    
    # Clean previous builds
    if os.path.exists("dist"):
        import shutil
        shutil.rmtree("dist")
        print("✅ Cleaned previous builds")
    
    # Build the package
    result = run_command("python -m build", "Building package")
    return result is not None

def upload_to_pypi():
    """Upload to PyPI"""
    print("\n🚀 Uploading to PyPI...")
    
    # Check if dist directory exists
    if not os.path.exists("dist"):
        print("❌ dist directory not found. Please build the package first.")
        return False
    
    # List files in dist
    dist_files = os.listdir("dist")
    print(f"📁 Found {len(dist_files)} files in dist/:")
    for file in dist_files:
        print(f"   - {file}")
    
    # Get PyPI credentials
    print("\n🔐 PyPI Credentials Required")
    print("💡 PyPI now requires API tokens instead of passwords.")
    print("   Get your token at: https://pypi.org/manage/account/token/")
    username = input("Enter your PyPI username: ").strip()
    api_token = input("Enter your PyPI API token: ").strip()
    
    if not username or not api_token:
        print("❌ Username and API token are required")
        return False
    
    # Set environment variables for this session
    os.environ['TWINE_USERNAME'] = "__token__"
    os.environ['TWINE_PASSWORD'] = api_token
    
    # Upload to PyPI
    result = run_command("twine upload dist/*", "Uploading to PyPI")
    if result is None:
        print("💡 Try running: twine upload dist/* --verbose")
        print("   Or check your API token at: https://pypi.org/manage/account/token/")
    return result is not None

def main():
    """Main function"""
    print("🚀 ENOUGH Journal - PyPI Publishing Script")
    print("=" * 50)
    
    # Check prerequisites
    check_prerequisites()
    
    # Build package
    if not build_package():
        print("❌ Build failed. Exiting.")
        sys.exit(1)
    
    # Upload to PyPI
    if upload_to_pypi():
        print("\n🎉 Successfully published to PyPI!")
        print("📋 You can now install with: pip install enough-journal")
    else:
        print("\n❌ Failed to upload to PyPI.")
        print("💡 Make sure you have PyPI credentials configured.")
        print("   You can configure them with: twine configure")

if __name__ == "__main__":
    main() 