#!/usr/bin/env python3
"""
AUR Publishing Script for ENOUGH Journal
Automates the process of updating PKGBUILD and submitting to AUR
"""

import os
import subprocess
import sys
import re
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

def get_version_from_pyproject():
    """Extract version from pyproject.toml"""
    try:
        with open("pyproject.toml", "r") as f:
            content = f.read()
            match = re.search(r'version = "([^"]+)"', content)
            if match:
                return match.group(1)
    except FileNotFoundError:
        print("❌ pyproject.toml not found")
    return None

def update_pkgbuild():
    """Update PKGBUILD with new version and source URL"""
    print("\n📝 Updating PKGBUILD...")
    
    version = get_version_from_pyproject()
    if not version:
        print("❌ Could not determine version")
        return False
    
    # Read current PKGBUILD
    try:
        with open("PKGBUILD", "r") as f:
            content = f.read()
    except FileNotFoundError:
        print("❌ PKGBUILD not found")
        return False
    
    # Update version
    content = re.sub(r'pkgver=([^\n]+)', f'pkgver={version}', content)
    
    # Update source URL (assuming GitHub release)
    source_url = f"https://github.com/sipistab/ENOUGH/archive/refs/tags/v{version}.tar.gz"
    content = re.sub(r'source=\([^)]+\)', f'source=("{source_url}")', content)
    
    # Update sha256sums to SKIP for now (user should update manually)
    content = re.sub(r'sha256sums=\([^)]+\)', 'sha256sums=("SKIP")', content)
    
    # Write updated PKGBUILD
    with open("PKGBUILD", "w") as f:
        f.write(content)
    
    print(f"✅ Updated PKGBUILD to version {version}")
    return True

def check_aur_tools():
    """Check if AUR tools are available"""
    print("🔍 Checking AUR tools...")
    
    # Check if makepkg is available
    result = run_command("makepkg --version", "Checking makepkg")
    if not result:
        print("⚠️  makepkg not found. This script is designed for Arch Linux.")
        print("   You can still update the PKGBUILD file for manual submission.")
        return False
    
    # Check if aurpublish is available
    result = run_command("aurpublish --version", "Checking aurpublish")
    if not result:
        print("⚠️  aurpublish not found. Please install aurpublish")
        print("   Install with: yay -S aurpublish")
        return False
    
    return True

def build_aur_package():
    """Build the AUR package"""
    print("\n📦 Building AUR package...")
    
    # Clean previous builds
    run_command("makepkg -c", "Cleaning previous builds")
    
    # Build the package
    result = run_command("makepkg -f", "Building AUR package")
    return result is not None

def submit_to_aur():
    """Submit to AUR"""
    print("\n🚀 Submitting to AUR...")
    
    # Check if .SRCINFO exists
    if not os.path.exists(".SRCINFO"):
        print("❌ .SRCINFO not found. Please run: makepkg --printsrcinfo > .SRCINFO")
        return False
    
    # Get AUR credentials
    print("\n🔐 AUR Credentials Required")
    username = input("Enter your AUR username: ").strip()
    password = input("Enter your AUR password: ").strip()
    
    if not username or not password:
        print("❌ Username and password are required")
        return False
    
    # Set environment variables for this session
    os.environ['AUR_USERNAME'] = username
    os.environ['AUR_PASSWORD'] = password
    
    # Submit to AUR
    result = run_command("aurpublish", "Submitting to AUR")
    return result is not None

def main():
    """Main function"""
    print("🚀 ENOUGH Journal - AUR Publishing Script")
    print("=" * 50)
    
    # Check AUR tools
    aur_tools_available = check_aur_tools()
    
    # Update PKGBUILD
    if not update_pkgbuild():
        print("❌ Failed to update PKGBUILD. Exiting.")
        sys.exit(1)
    
    if aur_tools_available:
        # Build AUR package
        if not build_aur_package():
            print("❌ Failed to build AUR package. Exiting.")
            sys.exit(1)
        
        # Submit to AUR
        if submit_to_aur():
            print("\n🎉 Successfully submitted to AUR!")
            print("📋 You can now install with: yay -S enough-journal")
        else:
            print("\n❌ Failed to submit to AUR.")
            print("💡 Make sure you have AUR credentials configured.")
    else:
        print("\n📝 PKGBUILD has been updated for manual submission.")
        print("💡 You can manually submit the PKGBUILD to AUR when ready.")
        print("   Or run this script on an Arch Linux system with AUR tools.")

if __name__ == "__main__":
    main() 