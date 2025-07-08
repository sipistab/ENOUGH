"""Main entry point for the sentence completion program."""
from pathlib import Path
from .cli.interface import cli

def main():
    """Run the main program."""
    # Ensure required directories exist
    Path("Submissions").mkdir(exist_ok=True)
    Path("Exercises").mkdir(exist_ok=True)
    
    # Run CLI
    cli()

if __name__ == "__main__":
    main() 