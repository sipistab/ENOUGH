# ENOUGH - The Growth Journal

A command-line tool for personal development through structured journaling and reflection exercises, with a particular focus on the Nathaniel Branden sentence completion method.

## Features

- **Nathaniel Branden Method**: Daily sentence completion exercises with weekly reflection
- **Custom Templates**: Create your own structured journaling templates
- **Starting Strength**: Track your workouts with automatic progression and deloading
- **Progress Tracking**: Monitor your consistency and growth over time
- **Clean Interface**: Distraction-free, focused journaling environment

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Quick Install

1. Clone the repository:
   ```bash
   git clone https://github.com/sipistab/enough.git
   cd enough
   ```

2. Run the installation script:
   - On Unix/Linux/macOS:
     ```bash
     chmod +x install.sh
     ./install.sh
     ```
   - On Windows:
     ```cmd
     install.bat
     ```

### Manual Installation

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Unix/Linux/macOS
   venv\Scripts\activate     # On Windows
   ```

2. Install in development mode:
   ```bash
   pip install -e .
   ```

## Usage

Start the program:
```bash
enough start
```

This will present you with a menu of available exercises for the day. Choose an exercise to begin your journaling session.

### Available Commands

- `enough start`: Begin today's exercises
- `enough calendar`: View your submission history
- `enough stats`: View progress statistics

## Template Types

### 1. Nathaniel Branden Method

The Sentence Completion Method is a powerful tool for self-discovery developed by Dr. Nathaniel Branden. Each week focuses on a specific theme through sentence stems:

- Monday through Friday: Complete 6-10 different endings for the same stem
- Weekend: Reflect on the week's responses
- Automatic progression through stems
- Weekly compilation of insights

### 2. Custom Templates

Create your own structured templates with:

- Multiple prompt types
- Flexible scheduling (daily, weekly, monthly)
- Customizable response requirements
- Support for metrics tracking

### 3. Starting Strength

Track your workouts following the Starting Strength program:

- Automatic warmup calculation
- Linear progression tracking
- Intelligent deloading
- Volume and PR tracking
- A/B workout rotation

## Directory Structure

```
ENOUGH/
├── templates/                      # Exercise templates
│   ├── nathaniel_branden_method/   # Branden's sentence completion
│   ├── custom/                     # User-defined templates
│   └── starting_strength/          # Workout tracking
├── submissions/                    # User entries
│   ├── nathaniel_branden_method/   # Branden method entries
│   ├── custom/                     # Custom template entries
│   └── starting_strength/          # Workout logs
└── main/                          # Core program files
    └── progress/                  # Progress tracking data
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[CC0 1.0 Universal](LICENSE)

To the extent possible under law, Sipos Istvan | Stephen Piper has waived all copyright and related or neighboring rights to ENOUGH.

This work is published from: Hungary. 