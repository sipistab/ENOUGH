# ENOUGH - The Growth Journal

## Overview
ENOUGH is a command-line tool for personal development through structured journaling and reflection exercises, with a particular focus on the Nathaniel Branden sentence completion method. The program provides a structured, consistent approach to self-reflection and personal growth.

Scheduling my notes enables me to stay consistent. Recurring tasks keep me reliable and I yarned for something robust that can quickly pick up on my needs. Like running a journal every day. This shows me that I am expected to think about something. For example at a glance, I can see that today I am supposed to have a daily sentence completion, a summary of my weekend, a workout I will need to log and it is the last Sunday of the month so an end of month revision as well. If I miss some, I expect my calendar to show this, so I can revisit later, and if I fail some of the exercises, I expect my journal to recalculate my deloading ahead of time. This is not simple to set up in most notetaking systems and even if it is possible, it is hard to make changes. I had enough, so I made Enough, it's not perfect, but you know what it is.

## Core Concepts

### 1. Exercise Types
- **Nathaniel Branden Method Exercises**
  - Weekly stem-based sentence completion
  - 6-10 completions per stem
  - Same stem used for 5 consecutive days
  - Weekend reflection on the week's responses

- **Custom Exercises**
  - User-defined prompts and templates
  - Flexible scheduling (daily, weekly, monthly)
  - Support for themed collections

- **Starting Strength Workout Log**
  - To be added later

### 2. Data Structure
```
main/                           # Core program files

templates/                      # Exercise templates
  ├── nathaniel_branden_method/  # Branden's sentence completion
  │   ├── sentence_completion.yaml  # Weekly stems
  ├── custom/                    # User-defined templates
  │   └── daily_note.yaml        # Daily reflection template
  └── starting_strenght/         # Workout tracking
      └── workouts.yaml          # Workout configuration

submissions/                     # User entries
  ├── nathaniel_branden_method/  # Branden method entries
  │   ├── YYYY_MM_DD_1.yaml      # Daily entries
  │   └── YYYY_MM_WW.yaml        # Weekly reflections
  ├── custom/                    # Custom template entries
  │   └── YYYY_MM_DD_1.yaml      # Various custom entries
  └── starting_strength/         # Workout logs
      └── YYYY_MM_DD_1.yaml      # Daily workout logs

maintenance/                    # Maintenance scripts and tools
```

### 3. YAML Structure

#### Progress Tracking (main/progress.yaml)
```yaml
__meta__:
  total_entries: 45
  total_reviews: 102
  first_entry: "2024-03-21"
  last_session: "2024-03-21"
  daily_log:
    "2024-03-21": 3  # Number of entries that day

exercises:
  nathaniel_branden_method:
    sentence_completion:
      entries: 30
      last_entry: "2024-03-21"
    weekend_reflection:
      entries: 12
      last_entry: "2024-03-16"
 
  starting_strength:
    workouts:
      entries: 15
      last_entry: "2024-03-20"
 
  custom:
    daily_note:
      entries: 10
      last_entry: "2024-03-20"
```

#### Branden Method Entry (submissions/nathaniel_branden_method/YYYY_MM_DD_1.yaml)
```yaml
date: "2024-03-21"
time: "07:15:32"
stem: "If I bring more awareness to my life today…"
completions:
  - "First completion"
  - "Second completion"
  # ... 6-10 completions total
duration: 240  # seconds
tags: ["week1"]
```

#### Weekend Reflection (submissions/nathaniel_branden_method/YYYY_MM_DD_weekend.yaml)
```yaml
date: "2024-03-23"
time: "09:30:15"
stem: "If any of what I have been writing this week is true…"
reflection: |
  Detailed reflection on the week's insights...
duration: 480  # seconds
tags: ["weekend", "week1"]
```

#### Workout Log (submissions/starting_strength/YYYY_MM_DD_1.yaml)
```yaml
date: "2024-03-21"
time: "16:45:22"
workout_type: "week_A"
bodyweight: 75.5  # kg
duration: 65  # minutes

exercises:
  squat:
    warmup:
      - {weight: 30, reps: 5, outcome: "pass"}
    working_sets:
      - {weight: 60, reps: 5, outcome: "pass"}
    notes: "Form notes"

  # ... other exercises ...

total_volume: 6475  # kg
notes: "Session notes"
```

#### Daily Note (submissions/custom/YYYY_MM_DD_daily_note.yaml)
```yaml
date: "2024-03-21"
time: "06:30:00"
template: "daily_note"

entries:
  gratitude:
    - "Entry 1"
    - "Entry 2"
    - "Entry 3"

  priorities:
    - "Priority 1"
    - "Priority 2"

  reflection: |
    Daily reflection text...

  mood_rating: 8
  energy_level: 7
  sleep_hours: 7.5

duration: 180  # seconds
tags: ["morning_routine", "daily"]
```

## Progress Tracking

```yaml
#Progress is stored in the progress.yaml file with the following structure:
__meta__:
  total_entries: 45
  total_reviews: 102
  first_entry: "2024-03-21"
  last_session: "2024-03-21"
  daily_log:
    "2024-03-21": 3

exercises:
  
  nathaniel_branden_method:
	weekday_stems.yaml:
      entries: 30
      last_entry: "2024-03-21"
    weekend_reflection.yaml:
      entries: 12
      last_entry: "2024-03-16"
 
  starting_strenght:
    workouts.yaml:
      entries: 15
      last_entry: "2024-03-20"
 
 custom:
    daily.yaml:
      entries: 10
      last_entry: "2024-03-20"
    monthly_budget.yaml:
      entries: 5
      last_entry: "2024-03-01"
```

3 types of exercises in A, B, and C folders as such:
#### A. Branden
```
weekday_stems.yaml
```
```yaml
name: "Nathaniel Branden's Sentence Completion Method"
description: "The original sentence completion practice from The Six Pillars of Self-Esteem. Each stem is practiced for a full week (Mon-Fri) with 6-10 different endings each day. Weekend reflection focuses on insights from that week's practice."

defaults:
  log_path: "submissions/nathaniel_branden_method"    # This is also where submissions are gathered from, must be the same
  compilation:                                        # This will compile ANSWERS given in timeframe and put stem_tag beforeit
	type: month, week, day                            # The time frame of how many files to fetch, everything from last day..so on
	frequency:                                        # Define when compilation runs on a given month, week day
		day: [6]									  # Run it on every Saturday
	stem_tags: "weekend"                              # For every tag it finds under this, it will compile all answers, if it finds 100 tags, it will ask you 100 questions and compile the answer under each, I recommend only using 1 tag like that.
  answers_required: 6   # Minimum 6 completions per stem
  min_characters: 10    # Minimum word count - completions can't be short
  max_time: 300         # 5 minutes per session
  start_date: "2024-03-20"

# Nathaniel Branden Stems

q_000:
  stem: "If I bring more awareness to my life today…"
  tags: [week1]

q_001:
  stem: "If I take more responsibility for my choices and actions today…"
  tags: [week1]
u

q_004:
  stem: "If I bring 5 percent more awareness to my important relationships…"
  tags: [week2]

q_005:
  stem: "If I bring 5 percent more awareness to my insecurities…"
  tags: [week2]

q_006:
  stem: "If I bring 5 percent more awareness to my deepest needs and wants…"
  tags: [week2]

q_007:
  stem: "If I bring 5 percent more awareness to my emotions…"
  tags: [week2]

q_008:
  stem: "If I treat listening as a creative act…"
  tags: [week3]

q_009:
  stem: "If I notice how people are affected by the quality of my listening…"
  tags: [week3]

q_010:
  stem: "If I bring more awareness to my dealings with people today…"
  tags: [week3]

q_011:
  stem: "If any of what I have been writing this week is true…"
  tags: [weekend]
yaml```


#### B. Custom

```yaml
name: "Template Name"          # Required: Template identifier
description: "Purpose"         # Optional: Template description
frequency: "daily"            # Required: daily, weekly, monthly, or custom
log_path: "submissions/custom"

# For custom frequency, specify schedule
schedule:
  days: [1, 3, 5]            # 1=Every Monday of every week, 7=Sunday
  weeks: [1, 3]              # Week numbers in a month
  months: [1, 6, 12]         # 1=January, 12=December

strict occurrence shedule:   #using ! with a  number will apply strict occurrance
  days: [1!, 3!, 5!]         # 1!=Only first Monday, 7=Sunday
  #or, for days only
   days: [1-!, 3-!, 5-!]     # 1!=Only last Monday, 7= last Sunday in month
  weeks: [1!, 3!]            # 1!=of every Week, 3!=of every 3th week
  months: [1!, 6, 12!]       # 1!=of every month, 12!=of every year
#must choose between strict months or strict weeks, except 12!
#example 1:
budget every half year
schedule:
  days: [1!]              # First Monday
  months: [6, 12]         # of every June and December only, once each
#example 2:
schedule:
  days: [5-!]            #5-!= last Friday,
  months: [1!]           #of every month
# Be careful with these, if you mix and match it too much you can break it, but I added a roboust error handling that should catch if you are abusing it.

#maybe add some common short like "biweekly" "every_6_months" and so..

# Global defaults for all prompts
defaults:
  answers_required: 1         # Number of responses required
  min_words: 0               # Minimum words per response
  max_time: 300              # Maximum time in seconds, 0 if infinite

# The actual prompts
prompts:
  p_000:                     # Unique prompt ID (required)
    prompt: "Question text"  # The actual question (required)
    tags: ["reflection"]     # Categories for organization
    answers_required: 3      # Override global default
    min_words: 50           # Override global default
    max_time: 600           # Override global default
    follow_up: "p_001"      # ID of follow-up question, think of it as "Every time I am asked about this, also ask that right away too" out of line
    
  p_001:
    prompt: "Follow-up question"
    tags: ["reflection", "deep"]
```

### Response Requirements
```yaml
defaults:
  answers_required: 1  # Number of answers needed
  min_words: 0        # Minimum word count
  max_time: 300       # Time limit in seconds
  strict: false       # Fuzzy matching tolerance
```

#### C. Starting Strenght
```yaml

name: "Starting Strength Program"
description: "Classic Starting Strength linear progression with hard-coded Week A/B workouts and default warmup scheme."

defaults:
  frequency: "custom"
  schedule:
    days: [2, 4, 7]  # Tue/Thu/Sun
  log_path: "submissions/starting_strength"
  increment_on_success: true
  deload_on_fail: true
  deload_percent: 10
  cycle: ["week_A", "week_B"]
    next_workout: "week_A"


  warmup_scheme:
    method: "linear"
    sets: 3
    scheme:
      - { percent: 50, reps: 5 } #Rounds to closes 2.5 increment
      - { percent: 70, reps: 3 }
      - { percent: 90, reps: 1 }

# Workout Groups
groups:
  week_A:
    exercises: ["squat", "bench_press", "deadlift", "deadlift", "atlas_curl", "neck_curl", "hanging_leg_raise"]

  week_B:
    exercises: ["squat", "overhead_press", "power_clean", "atlas_curl", "neck_curl", "hanging_leg_raise"]

# Exercises
exercises:
  squat:
    starting_weight: 60
    progression: 2.5
    sets: 3
    reps: 5

  bench_press:
    starting_weight: 50
    progression: 2.5
    sets: 3
    reps: 5

  overhead_press:
    starting_weight: 40
    progression: 2.5
    sets: 3
    reps: 5

  deadlift:
    starting_weight: 80
    progression: 5
    sets: 1
    reps: 5

  power_clean:
    starting_weight: 40
    progression: 2.5
    sets: 5
    reps: 3

atlas_curl:
    starting_weight: bodyweight
    progression: 0
    sets: 2
    reps: 10
    no_warmup: true

  neck_curl:
    starting_weight: 5
    progression: 1
    sets: 3
    reps: 15
    no_warmup: true

  hanging_leg_raise:
    starting_weight: bodyweight
    progression: 0
    sets: 3
    reps: 10
    no_warmup: true
```
## Technical Design

### 1. main Components

#### Template Manager
- Loads and validates template files
- Tracks progress and completion
- Manages template scheduling
- Handles response storage

#### Template System
- YAML-based template definition
- Validation of template structure
- Support for custom template types
- Template inheritance for common patterns

#### Progress Tracking
- Track completion streaks
- Store historical responses
- Generate progress reports
- Export functionality for backup/review

### 2. User Interface

#### Command Line Interface

Main Menu:
```
enough
  ├── start           # View today's exercises
  ├── review calendar # Review past responses in a list-like calendar format
  ├── stats           # View statistics
  
  Pick [1-3] --> Alternatively, just start the program with python -m enough start
  Enter "quit" whenever you want to close the program - Your progress is saved automatically on each enter submittion into their yaml file.
  
```

##### Start page | 1:
```
==============================
       TODAY'S ENTRIES
==============================

[1] Morning Routine - Custom Exercise
[2] Nathaniel Branden - Sentence Completion
[3] Starting Strength Workout
[4] Half Year Budget Evaluation

Pick one to run [1-4]:
```
[1] Morning Routine - Custom Exercise
```
==============================
    SENTENCE COMPLETION
==============================

"If I bring more awareness to my choices today…"
I would... #users answer, they need to submit 6-10 if they did, clear screen and go to next question, like:

_________________________________

==============================
    SENTENCE COMPLETION
==============================

"If I bring more awareness to how I deal with people today…"
I would... #so on until all questions are met for that week. / if it's a saturay, they make the compilation in a similar manner

```
[3] Starting Strength Workout
```
==============================
  STARTING STRENGTH WORKOUT
==============================

Week: A

Exercises for Today:

  • Squat ............. 3 sets x 5 reps  @ 60 kg
  • Bench Press ....... 3 sets x 5 reps  @ 40 kg
  • Deadlift .......... 1 set  x 5 reps  @ 80 kg
  • Atlas Curls ....... 3 sets x 10 reps @ 20 kg
  • Neck Curls ........ 2 sets x 12 reps @ Bodyweight
  • Hanging Leg Raises. 3 sets x 10 reps @ Bodyweight

Press enter to start...  #After starting Each warmup is calculated, entries come one by one like so:

2025-07-10 14:23:45

Squat warmup set 50%
5 reps  @ 30 kg

Outcome? [Pass/Fail]: Pass
#Clear to title

Squat warmup set 70%
3 reps  @ 42.5 kg

Outcome? [Pass/Fail]: Pass
#Clear to title

Squat warmup set 90%
2 reps  @ 50 kg

Outcome? [Pass/Fail]: Pass
#Clear to title

Squat ............. 3 sets x 5 reps  @ 60 kg
Set 1
Outcome? [Pass/Fail]: Fail

#Fail a lift 3 sessions in a row, 3 sessions not 3 sets and we deload by 10% rounded up to next 2.5

Squat ............. 3 sets x 5 reps  @ 60 kg
Set 2
Outcome? [Pass/Fail]: Fail

Squat ............. 3 sets x 5 reps  @ 60 kg
Set 3
Outcome? [Pass/Fail]: Fail



2025-07-10 14:28:31

Bench Press warmup set 50%
5 reps  @ 25 kg

Outcome? [Pass/Fail]: Pass #so on...

```

```
==============================
         CALENDAR LOG
==============================

DATE         | ENTRIES
-------------------------------------------
2025-07-10   | ✔ Morning Routine, ✔ Nathaniel Branden, ✗ Starting Strength, ✔ Half Year Budget
2025-07-09   | ✔ Morning Routine, ✔ Nathaniel Branden, ✔ Starting Strength
2025-07-08   | ✔ Morning Routine, ✔ Nathaniel Branden, ✔ Starting Strength
2025-07-07   | ✔ Morning Routine, ✔ Nathaniel Branden, ✔ Starting Strength
2025-07-06   | ✔ Morning Routine, ✔ Nathaniel Branden, ✔ Reflection
-------------------------------------------

Legend: ✔ = Done   ✗ = Skipped fully, no submission for that date, no file

```

```
==============================
          STATISTICS
==============================

What do you want to see?

 [1] Global Entries Stats (all)
 [2] Nathaniel Branden Method
 [3] Starting Strength Progress
 [4] Return to Main Menu

Pick an option [1-4]:

==============================
     GLOBAL ENTRIES STATS
==============================

Total Entries:             132
Total Characters Typed:    18,473
Average Entries/Day:       4.2
Average Characters/Entry:  140
Average Session Duration:  04:10 min
Most Active Day:           Thursday
Longest Streak:            21 days

Press [Q] to return.


==============================
  NATHANIEL BRANDEN METHOD
==============================

Current Week:              week3
Longest Streak:            21 days

Total Submissions:         19
Missed Sessions:           1
Total Stems Completed:     42
Average Endings per Stem:  7.1
Average Words per Ending:  37

Last Completed:            2025-07-10  07:45:32

Press [Q] to return.



==============================
  STARTING STRENGTH PROGRESS
==============================

Total Workouts:            36
Missed Workouts:           2
Average Workout Duration:  47 min
Last Workout:              2025-07-10  18:32:10
Next Scheduled:            2025-07-12  (Week B)

Progress:
  Squat:       60 ➜ 87.5 kg (+27.5 kg)
    Current PR:         1 x 140 kg  (2025-07-03)
    Last Best Set:      3 x 5 @ 87.5 kg
    Next Target:        90 kg
    Failed Attempts:    1
    Stalled:            X No

  Bench Press: 40 ➜ 55 kg (+15 kg)
    Current PR:         1 x 75 kg  (2025-06-28)
    Last Best Set:      3 x 5 @ 55 kg
    Next Target:        57.5 kg
    Failed Attempts:    2
    Stalled:            ✔ Yes

  Overhead Press: 30 ➜ 42.5 kg (+12.5 kg)
    Current PR:         1 x 50 kg  (2025-07-01)
    Last Best Set:      3 x 5 @ 42.5 kg
    Next Target:        45 kg
    Failed Attempts:    0
    Stalled:            X No

  Deadlift:    80 ➜ 110 kg (+30 kg)
    Current PR:         1 x 150 kg  (2025-06-20)
    Last Best Set:      1 x 5 @ 110 kg
    Next Target:        115 kg
    Failed Attempts:    0
    Stalled:            X No

  Power Clean: 40 ➜ 52.5 kg (+12.5 kg)
    Current PR:         1 x 70 kg  (2025-07-05)
    Last Best Set:      5 x 3 @ 52.5 kg
    Next Target:        55 kg
    Failed Attempts:    0
    Stalled:            X No

Total Volume Moved:       45,700 kg

Warmup Sets Logged:       108
Work Sets Logged:         98
Failed Sets:              3

Press [Q] to return.

```

#### Interactive Flow
1. Daily prompt selection
2. Response collection
3. Progress feedback
4. Review options

### 3. Data Storage
- Local file system storage
- Plain text format for longevity
- Simple directory structure
- No encryption (keep it simple)

## Implementation Guidelines

### 1. Dependencies
- PyYAML: YAML file handling
- Click: CLI framework
- Rich: Terminal formatting
- pytest: Testing framework

### 2. Installation

### From PyPI
```bash
pip install enough-journal
```

### Manual Installation
```bash
git clone https://github.com/sipistab/ENOUGH.git
cd ENOUGH
pip install -e .
```

### 3. Development Setup
```bash
# Clone repository
git clone https://github.com/username/enough.git
cd enough

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .
```


## Development Principles
1. **Simplicity First**: Focus on core functionality
2. **Data Ownership**: Local storage, plain text
3. **Flexibility**: Extensible template system
4. **Reliability**: Thorough testing, error handling
5. **Privacy**: No tracking, no cloud dependency

## Implementation Details

### Template System
- Flexible YAML-based templates
- Support for follow-up questions
- Custom response requirements
- Tag-based organization

### Review System
- Daily and weekly review cycles
- Progress tracking and statistics
- Tag-based filtering
- Export capabilities

### Data Management
- Secure local storage
- Automatic backup system
- Platform-independent data location
- Clean data structure

## Why I Created This

While many journaling applications exist, they often emphasize features over function, creating unnecessary friction between thought and expression. ENOUGH was created to provide a distraction-free environment for self-reflection, where the interface disappears and allows focus on what matters - your thoughts and insights.

Initially built for personal use, particularly to maintain a consistent journaling practice of Nathaniel Branden without the overhead of traditional applications. The tool is intentionally minimal yet complete in its essential functions. You are free to use it, modify it, and share it as you see fit.

— Stephen

## License

[CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, Sipos Istvan | Stephen Piper has waived all copyright and related or neighbouring rights to ENOUGH.

This work is published from: Hungary.
```
