# ENOUGH - A Mindful Journaling Tool

[![PyPI version](https://badge.fury.io/py/enough-journal.svg)](https://badge.fury.io/py/enough-journal)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)

A flexible command-line journaling system for personal growth and self-reflection, supporting customizable prompts, scheduled exercises, and structured reviews.

## Features

🎯 **Focused Journaling**
- Custom prompt scheduling (daily, weekly, monthly)
- Follow-up questions and response tracking
- Progress visualization

📝 **Flexible Templates**
- YAML-based template system
- Tag-based organization
- Multiple response formats

🔍 **Review & Reflect**
- Weekly review system
- Progress tracking
- Export capabilities

## Quick Start

```bash
# Install from PyPI
pip install enough-journal

# Start journaling
enough
```

## Installation

### PyPI (All Platforms)
```bash
pip install enough-journal
```

### Manual Installation
```bash
git clone https://github.com/sipistab/ENOUGH.git
cd ENOUGH
pip install -e .
```

## Usage

1. **Start a New Journal Entry**
   ```bash
   enough
   ```
   Select "Start Journaling Session" from the menu.

2. **Review Past Entries**
   ```bash
   enough
   ```
   Select "Review Past Entries" from the menu.

3. **Create Custom Templates**
   ```bash
   enough
   ```
   Select "Manage Exercise Templates" from the menu.

## Template Format

Templates use YAML format:

```yaml
name: "Daily Reflection"
frequency: "daily"

prompts:
  p_000:
    prompt: "What's on my mind right now..."
    tags: ["reflection"]
    answers_required: 3
    
  p_001:
    prompt: "What am I grateful for today?"
    tags: ["gratitude"]
    follow_up: "p_002"
    
  p_002:
    prompt: "How can I express this gratitude?"
    tags: ["action", "gratitude"]
```

## License

This work is released under [CC0 1.0 Universal (CC0 1.0) Public Domain Dedication](https://creativecommons.org/publicdomain/zero/1.0/).

You can copy, modify, distribute and perform the work, even for commercial purposes, all without asking permission.
