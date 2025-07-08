# Personal Growth Journal

A flexible journaling system supporting various self-reflection exercises, including Nathaniel Branden's sentence completion method.

## Project Structure

```
Project Root/
├── Core/                           # Core program functionality
│   ├── Data/                      # User data and responses
│   ├── Maintenance/              # Project maintenance files
│   ├── sentence_completion/      # Main program modules
│   ├── SentenceCompletion.py    # Main program file
│   └── SentenceCompletionStartup.{bat,sh}  # Startup scripts
│
├── Exercises/                      # Exercise templates
│   ├── Nathanial Branden - Sentence Completion/
│   │   ├── weekday_exercises.yaml
│   │   └── weekend_reflections.yaml
│   └── Custom Sentence Completion/
│       └── self_awareness.yaml
│
├── README.md                      # This file
└── progress.yaml                  # Progress tracking
```

## Features

### Current Features
- Nathaniel Branden's Sentence Completion exercises
- Custom exercise templates
- Immediate response saving
- Progress tracking

### Upcoming Features
- **Flexible Exercise Templates**
  - Create custom YAML templates
  - Configure exercise frequency
  - Set custom journaling periods
  - Define your own prompts

- **Smart Calendar System**
  - Track exercise completion
  - View progress history
  - Automatic date handling
  - Exercise scheduling

- **Intelligent Menu**
  - Automatic day/progress detection
  - Smart exercise suggestions
  - Progress visualization

## Creating Custom Exercises

### Template Structure (Coming Soon)
```yaml
name: "My Custom Exercise"
frequency:
  type: "daily" | "weekly" | "custom"
  days: [1, 3, 5]  # Example: Monday, Wednesday, Friday
  
prompts:
  morning:
    - "Today I am grateful for..."
    - "My main focus today is..."
  evening:
    - "Today I learned..."
    - "Tomorrow I will..."

reflection:
  frequency: "weekly"
  prompts:
    - "This week's biggest insight was..."
    - "Next week I want to focus on..."
```

## Getting Started

1. Choose an exercise type from the `Exercises` directory
2. Run the appropriate startup script from the `Core` directory
3. Follow the daily prompts
4. Complete reflections when scheduled

## Data Management

- All responses saved immediately
- Local storage in Core/Data
- Progress tracking in progress.yaml

## Contributing

To add new exercise templates:
1. Create a new YAML file in the appropriate directory
2. Follow the template structure
3. Test thoroughly before use

## License

Personal use only. Do not distribute without permission.
Nathaniel Branden's method is based on his original work - please support by purchasing his books.

# Preface

I have only shared this project directly with the ones I most respect. I hold your presence in high esteem. My hope is that this work proves valuable to you, aiding your personal journey. Please use it as you see fit, for your benefit and growth.

I was inspired by the concepts presented in "The Six Pillars of Self-Esteem" book. While I highly recommend reading it, it is not essential for the exercises to be effective.

You can read more about the original work here: https://nathanielbranden.com/sentence-completion-i/

Please note that this is only a passion project of mine as I learn how to develop applications, I did not request the author's premission to use his work and neither is this a commercial application. Please do not distribute this application without my premission. Nathanial dedicated a lifetime to creating this masterpiece. His family receives royalties from the sold copies, so if you enjoy his work, please consider purchasing the book.

# Sentence Completion Compiler

## Purpose
This Python application offers a solitary path into the depths of self-awareness through Nathaniel Branden's sentence completion exercises. It provides a focused, distraction-free environment for daily introspection, eliminating the complexities of physical paperwork. The program is designed to be used daily, with sentence completion exercises during weekdays and assessments on weekends.

## Features
- Daily sentence completion exercises
- Weekly progress assessments
- Secure storage of personal responses
- Automatic data backup
- Progress tracking
- Cross-platform compatibility

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Setup
1. Clone or download this repository
2. Navigate to the project directory
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Program
- **Windows**: Double-click `SentenceCompletionStartup.bat`
- **macOS/Linux**: Run `./SentenceCompletionStartup.sh`
- **Manual Start**: Run `python SentenceCompletion.py`

## Usage Guide

### Daily Exercises (Option 1)
1. Select option [1] for Daily Log
2. Enter the week number (1-30)
3. Enter the day number (1-5)
4. Complete the sentence stems provided
5. Your responses are automatically saved and encrypted

### Weekly Assessment (Option 2)
1. Select option [2] for Weekly Assessment
2. Enter the week number to review
3. Review your responses from the week
4. Complete the assessment questions
5. Results are saved for future reference

### Data Management
- All responses are automatically encrypted
- Weekly backups are created automatically
- Export functionality available for data portability
- Data is stored locally on your system only

## Security Features
- Local data storage only - no cloud or external servers
- Optional file encryption for sensitive data
- Regular backup reminders
- Data export capabilities

## File Structure
```
sentence-completion/
├── README.md
├── requirements.txt
├── SentenceCompletion.py
├── SentenceCompletion.txt
├── SentenceCompletionStartup.bat
└── SentenceCompletionStartup.sh
```

## Troubleshooting
- **Program won't start**: Ensure Python is installed and in your system PATH
- **File access errors**: Check file permissions in your user directory
- **Backup issues**: Ensure sufficient disk space and write permissions

## Support
For technical support or questions, please open an issue in the repository or contact the developer directly.

## Privacy Notice
This application:
- Stores all data locally on your device
- Never transmits data over the internet
- Provides optional encryption for sensitive information
- Allows complete data deletion at any time

## Future Development
- Web-based version with secure authentication
- Mobile application support
- Enhanced progress visualization
- Integration with journaling features

## License
This is a personal project shared with select individuals. Please do not distribute without permission. The sentence completion method is based on Nathaniel Branden's work - please support the original author by purchasing his books.

## Acknowledgments
- Nathaniel Branden for the original sentence completion methodology
- All users who have provided valuable feedback
- The Python community for excellent libraries and tools





