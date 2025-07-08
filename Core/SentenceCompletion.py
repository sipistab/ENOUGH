import os
import yaml
import logging
from pathlib import Path
from datetime import datetime

# Constants for directory paths
CORE_DIR = Path(__file__).parent
DATA_DIR = CORE_DIR / "Data"
EXERCISES_DIR = Path(__file__).parent.parent / "Exercises"
LOG_DIR = DATA_DIR / "logs"

# Set up logging
def setup_logging():
    """Configure logging with both file and console handlers"""
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    log_file = LOG_DIR / f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

class ExerciseError(Exception):
    """Base exception for exercise-related errors"""
    pass

class TemplateError(ExerciseError):
    """Raised when there are issues with exercise templates"""
    pass

class DataError(ExerciseError):
    """Raised when there are issues with data files"""
    pass

def ensure_data_dir():
    """Ensure the Data directory exists"""
    DATA_DIR.mkdir(parents=True, exist_ok=True)

def get_exercise_path(exercise_type="Nathanial Branden - Sentence Completion"):
    """Get path to exercise YAML files"""
    path = EXERCISES_DIR / exercise_type
    if not path.exists():
        raise FileNotFoundError(f"Exercise type '{exercise_type}' not found")
    return path

def validate_template(template):
    """Validate the structure of loaded template"""
    required_keys = ['weeks', 'settings']
    if not all(key in template for key in required_keys):
        missing = [key for key in required_keys if key not in template]
        raise TemplateError(f"Invalid template structure. Missing keys: {missing}")
    
    if not isinstance(template['weeks'], dict):
        raise TemplateError("Template weeks should be a dictionary")
    
    for week_key, week_data in template['weeks'].items():
        if not isinstance(week_data, dict) or 'stems' not in week_data:
            raise TemplateError(f"Invalid week structure in {week_key}")
        if not isinstance(week_data['stems'], list):
            raise TemplateError(f"Stems should be a list in {week_key}")

def load_exercise_template():
    """Load the exercise template from YAML"""
    template_path = get_exercise_path() / "weekday_exercises.yaml"
    if not template_path.exists():
        raise FileNotFoundError(f"Template file not found: {template_path}")
        
    with template_path.open('r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def get_week_prompts(template, week):
    """Get prompts for a specific week from the template"""
    week_key = f"week{week}"
    if week_key in template['weeks']:
        return template['weeks'][week_key]['stems']
    return []

def save_response(file_path, prompt, response):
    """Save a single response immediately after input"""
    with file_path.open('a') as f:
        f.write(f"Question: {prompt}\n")
        f.write(f"Response:\n{response}\n\n")

def compile_and_organize_week(week_number):
    """Compile and organize a week's responses"""
    compiled_data = {}

    # Collect all responses for the week
    for day_number in range(1, 6):
        exercise_file = DATA_DIR / f"Week{week_number}_Day{day_number}_exercises.txt"
        if exercise_file.exists():
            with exercise_file.open("r") as f:
                lines = f.read().split('\n\n')
                for block in lines:
                    if not block.strip():
                        continue
                    question, *responses = block.strip().split('\n')
                    compiled_data.setdefault(question, []).extend(responses)

    if not compiled_data:
        print(f"No exercises found for week {week_number}")
        return

    # Save compiled data
    compiled_file = DATA_DIR / f"Week{week_number}_compiled_organized_data.txt"
    with compiled_file.open("w") as f:
        for question, answers in compiled_data.items():
            f.write(question + '\n')
            f.write('\n'.join(answers).replace('Response:', '') + '\n\n')

    print(f"Organized exercises for Week {week_number} created in '{compiled_file}'.")

def present_and_collect_answers(week_number, file_path):
    with open(file_path, 'r') as file:
        lines = file.read().split('\n\n')

    questions = []
    current_question = None
    answers = []

    for line in lines:
        if line.startswith("Question:"):
            if current_question is not None:
                questions.append((current_question, answers))
                answers = []
            current_question = line.strip()
        else:
            answers.append(line.strip())

    assessment_file = DATA_DIR / f"Week{week_number}_assessment.txt"
    with assessment_file.open("w") as f:
        for question, answer_options in questions:
            print(question)
            for i, answer in enumerate(answer_options):
                print(f"{i + 1}. {answer}")

            print("If any of what I have been writing this week is true...")
            f.write(question + "\n")
            for i in range(5):
                response = input(f"{i + 1}. ")
                f.write(response + "\n")
            f.write("\n")

    print(f"Assessment saved in '{assessment_file}'.")

def main():
    try:
        setup_logging()
        logging.info("Starting Sentence Completion Program")
        ensure_data_dir()
        template = load_exercise_template()

        while True:
            try:
                choice = input("[1] Daily Log [2] Weekly Assessment [Q] Quit: ")
                
                if choice == '1':
                    try:
                        week_number = int(input("Enter the week number (1-30): "))
                        if not 1 <= week_number <= 30:
                            print("Invalid week number. Please enter a number between 1 and 30.")
                            continue

                        prompts = get_week_prompts(template, week_number)
                        if not prompts:
                            print(f"No prompts found for Week {week_number}.")
                            continue

                        day_number = int(input("Enter the day number (1-5): "))
                        if not 1 <= day_number <= 5:
                            print("Invalid day number. Please enter a number between 1 and 5.")
                            continue

                        save_file = DATA_DIR / f"Week{week_number}_Day{day_number}_exercises.txt"
                        # Clear the file before starting new entries
                        save_file.write_text("")

                        for prompt in prompts:
                            print(f"\n{prompt}")
                            print("Enter 5 completions:")
                            response = ""
                            for i in range(5):
                                line = input(f"{i+1}: ")
                                if line.strip() == "":
                                    break
                                response += line + "\n"
                            # Save each response immediately
                            save_response(save_file, prompt, response.strip())

                        print("All responses saved.")

                    except ValueError:
                        print("Please enter a valid number.")
                    except (TemplateError, DataError) as e:
                        print(f"Error: {str(e)}")
                        logging.error(str(e))
                
                elif choice == '2':
                    try:
                        week_number = int(input("Enter the week number (1-30): "))
                        if not 1 <= week_number <= 30:
                            print("Invalid week number. Please enter a number between 1 and 30.")
                            continue

                        compile_and_organize_week(week_number)
                        file_path = DATA_DIR / f"Week{week_number}_compiled_organized_data.txt"
                        if file_path.exists():
                            present_and_collect_answers(week_number, str(file_path))

                    except ValueError:
                        print("Please enter a valid number.")
                    except (TemplateError, DataError) as e:
                        print(f"Error: {str(e)}")
                        logging.error(str(e))
                
                elif choice.upper() == 'Q':
                    print("Exiting the program.")
                    break
                
                else:
                    print("Invalid choice. Please enter 1, 2, or Q to quit.")

            except KeyboardInterrupt:
                print("\nOperation cancelled by user.")
                continue
            except Exception as e:
                logging.error(f"Unexpected error in main loop: {str(e)}")
                print("An unexpected error occurred. Please check the logs for details.")
                continue

    except Exception as e:
        logging.critical(f"Critical error: {str(e)}")
        print("A critical error occurred. Please check the logs for details.")
        raise

if __name__ == "__main__":
    main()