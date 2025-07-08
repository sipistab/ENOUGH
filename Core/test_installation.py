"""Test script to verify the sentence completion program installation."""
import sys
from pathlib import Path

def test_imports():
    """Test that all required packages are installed and importable."""
    required_packages = [
        'rich',
        'cryptography',
        'click'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package)
            print(f"✓ {package} is installed")
        except ImportError:
            missing_packages.append(package)
            print(f"✗ {package} is missing")
            
    return len(missing_packages) == 0

def test_file_structure():
    """Test that all required files and directories exist."""
    required_files = [
        'sentence_completion/__init__.py',
        'sentence_completion/__main__.py',
        'sentence_completion/core/__init__.py',
        'sentence_completion/core/exercise_manager.py',
        'sentence_completion/utils/__init__.py',
        'sentence_completion/utils/encryption.py',
        'sentence_completion/utils/exceptions.py',
        'sentence_completion/utils/file_handler.py',
        'sentence_completion/utils/logger.py',
        'sentence_completion/cli/__init__.py',
        'sentence_completion/cli/interface.py',
        'SentenceCompletion.txt',
        'requirements.txt'
    ]
    
    missing_files = []
    for file_path in required_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)
            print(f"✗ {file_path} is missing")
        else:
            print(f"✓ {file_path} exists")
            
    return len(missing_files) == 0

def test_program_start():
    """Test that the program can be imported and initialized."""
    try:
        from sentence_completion.core import ExerciseManager
        from sentence_completion.cli import cli
        from sentence_completion.utils import logger
        
        # Initialize core components
        manager = ExerciseManager()
        print("✓ Program components initialized successfully")
        return True
        
    except Exception as e:
        print(f"✗ Program initialization failed: {str(e)}")
        return False

def main():
    """Run all tests."""
    print("\nTesting Sentence Completion Program Installation\n")
    
    print("1. Testing package imports...")
    imports_ok = test_imports()
    
    print("\n2. Testing file structure...")
    files_ok = test_file_structure()
    
    print("\n3. Testing program initialization...")
    init_ok = test_program_start()
    
    print("\nTest Results:")
    print(f"Package imports: {'✓' if imports_ok else '✗'}")
    print(f"File structure: {'✓' if files_ok else '✗'}")
    print(f"Program initialization: {'✓' if init_ok else '✗'}")
    
    if imports_ok and files_ok and init_ok:
        print("\nAll tests passed! The program is ready to use.")
        return 0
    else:
        print("\nSome tests failed. Please fix the issues before using the program.")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 