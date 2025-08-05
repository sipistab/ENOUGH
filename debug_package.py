#!/usr/bin/env python3
"""
Debug script to check if exercises.yaml is included in the package
"""

import importlib.resources
import os

def debug_package():
    print("🔍 Debugging package inclusion...")
    
    # Check if enough package exists
    try:
        import enough
        print("✅ enough package found")
    except ImportError as e:
        print(f"❌ enough package not found: {e}")
        return
    
    # List all resources in the package
    try:
        with importlib.resources.path('enough', '') as package_path:
            print(f"📦 Package path: {package_path}")
            if os.path.exists(package_path):
                files = os.listdir(package_path)
                print(f"📦 Package files: {files}")
    except Exception as e:
        print(f"❌ Error listing resources: {e}")
    
    # Try to get exercises.yaml
    try:
        with importlib.resources.path('enough', 'exercises.yaml') as exercises_file:
            print(f"📄 exercises.yaml path: {exercises_file}")
            
            if os.path.exists(exercises_file):
                print("✅ exercises.yaml exists!")
                with open(exercises_file, 'r') as f:
                    content = f.read()
                    print(f"📏 File size: {len(content)} characters")
                    print(f"📋 First 200 chars: {content[:200]}...")
            else:
                print("❌ exercises.yaml does not exist at that path!")
                
    except Exception as e:
        print(f"❌ Error getting exercises.yaml: {e}")

if __name__ == "__main__":
    debug_package() 