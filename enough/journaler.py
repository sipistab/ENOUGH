#!/usr/bin/env python3
"""
ENOUGH - Nathaniel Branden Sentence Completion Journal
Main application logic
"""

import os
import yaml
import json
import time
from datetime import datetime, date, timedelta
from typing import List, Dict, Optional
import calendar


class ProgressTracker:
    def __init__(self, progress_file: str = "progress.json"):
        self.progress_file = progress_file
        self.progress = self.load_progress()
    
    def load_progress(self) -> Dict:
        if os.path.exists(self.progress_file):
            try:
                with open(self.progress_file, 'r') as f:
                    return json.load(f)
            except:
                pass
        return {
            "current_week": 1,
            "current_day": 1,
            "start_date": None,
            "is_new_user": True
        }
    
    def save_progress(self):
        with open(self.progress_file, 'w') as f:
            json.dump(self.progress, f, indent=2)
    
    def update_progress(self, week: int, day: int):
        self.progress["current_week"] = week
        self.progress["current_day"] = day
        self.progress["is_new_user"] = False
        self.save_progress()


class Journaler:
    def __init__(self):
        self.tracker = ProgressTracker()
        self.exercises = self.load_exercises()
        self.submissions_dir = "submissions"
        os.makedirs(self.submissions_dir, exist_ok=True)
    
    def clear_terminal(self):
        """Clear terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def load_exercises(self) -> List[Dict]:
        """Load all exercises from journals directory"""
        exercises = []
        journals_dir = "journals"
        
        if not os.path.exists(journals_dir):
            print(f"❌ Journals directory '{journals_dir}' not found!")
            return exercises
        
        # Load all .yaml files from journals directory
        for filename in os.listdir(journals_dir):
            if filename.endswith('.yaml'):
                filepath = os.path.join(journals_dir, filename)
                
                try:
                    with open(filepath, 'r') as f:
                        data = yaml.safe_load(f)
                        
                        if data.get('type') == 'branden':
                            # This is a multi-week exercise
                            exercise = {
                                'name': data['name'],
                                'description': data.get('description', ''),
                                'type': 'branden',
                                'weeks': data['total_weeks'],
                                'stems_per_day': data['stems_per_day'],
                                'weeks_data': data['weeks']
                            }
                            exercises.append(exercise)
                            
                        elif data.get('type') == 'custom':
                            # This is a custom exercise
                            exercise = {
                                'name': data['name'],
                                'description': data.get('description', ''),
                                'type': 'custom',
                                'time': data['time'],
                                'stems': data['stems'],
                                'stems_per_day': data['stems_per_day']
                            }
                            exercises.append(exercise)
                            
                except Exception as e:
                    print(f"❌ Failed to load {filename}: {e}")
        
        return exercises
    
    def get_current_exercise(self) -> Optional[Dict]:
        """Get current exercise based on progress"""
        if not self.exercises:
            return None
        
        current_week = self.tracker.progress["current_week"]
        
        # Check if we have a start date to calculate proper week
        if self.tracker.progress.get("start_date"):
            start_date = datetime.strptime(self.tracker.progress["start_date"], "%Y-%m-%d")
            today = datetime.now()
            days_since_start = (today - start_date).days
            calculated_week = (days_since_start // 7) + 1
            
            # Use calculated week if it's different from stored week
            if calculated_week != current_week:
                self.tracker.progress["current_week"] = calculated_week
                self.tracker.save_progress()
                current_week = calculated_week
        
        # Find the current branden exercise (assuming it's the first one)
        branden_exercise = None
        for exercise in self.exercises:
            if exercise.get('type') == 'branden':
                branden_exercise = exercise
                break
        
        if not branden_exercise:
            return None
        
        # Find the week data
        for week_data in branden_exercise['weeks_data']:
            if week_data['week'] == current_week:
                return {
                    'week': current_week,
                    'stems': week_data['stems']
                }
        
        # If no exercise found for current week, check if we're beyond the program
        if current_week > branden_exercise['weeks']:
            return None
        
        return None
    
    def handle_first_time_user(self):
        """Handle first-time user setup"""
        print("\n=========================================")
        print("        ENOUGH - Minimal Journal")
        print(" Inspired by Nathaniel Branden's Work")
        print("=========================================")
        print()
        print("No prior journal found for this exercise.")
        print()
        print("Would you like to:")
        print("1. Start from Week 1 | Day 1 (beginner)")
        print("2. Choose a specific week and day")
        print("3. Go back")
        print()
        
        while True:
            choice = input("Enter your choice (1-3): ").strip()
            
            if choice == "1":
                # Start from Week 1, Day 1
                today = datetime.now()
                
                if today.weekday() >= 5:  # Weekend
                    print(f"\nYou chose to start from Week 1 | Day 1.")
                    print(f"Today is {today.strftime('%A')}. Exercises begin on Mondays.")
                    print("Come back on Monday to begin Week 1 | Day 1.")
                    return False
                else:
                    # Calculate the start date for Week 1 (go back to Monday of this week)
                    days_since_monday = today.weekday()
                    start_date = today - timedelta(days=days_since_monday)
                    
                    self.tracker.progress["start_date"] = start_date.strftime("%Y-%m-%d")
                    self.tracker.progress["current_week"] = 1
                    self.tracker.progress["current_day"] = 1
                    self.tracker.save_progress()
                    return True
                    
            elif choice == "2":
                print("\nWhat week are you currently on? (1-30): ")
                try:
                    week = int(input().strip())
                    if week < 1 or week > 30:
                        print("Please enter a week between 1 and 30.")
                        continue
                    
                    # Calculate the appropriate start date
                    today = datetime.now()
                    
                    # Calculate how many weeks back we need to go
                    weeks_back = week - 1
                    days_back = weeks_back * 7  # Convert to days
                    
                    # Calculate the start date
                    start_date = today - timedelta(days=days_back)
                    
                    # Adjust to Monday of that week
                    days_since_monday = start_date.weekday()
                    start_date = start_date - timedelta(days=days_since_monday)
                    
                    print(f"\nStarting from custom week {week}")
                    print(f"Start date calculated: {start_date.strftime('%Y-%m-%d')} (Monday)")
                    
                    self.tracker.progress["start_date"] = start_date.strftime("%Y-%m-%d")
                    self.tracker.progress["current_week"] = week
                    self.tracker.progress["current_day"] = 1
                    self.tracker.save_progress()
                    return True
                    
                except ValueError:
                    print("Please enter valid numbers.")
                    continue
            elif choice == "3":
                return False
            else:
                print("Please enter '1', '2', or '3'.")
    
    def check_and_setup_user(self):
        """Check if user needs setup and handle it"""
        # Check if there are any existing submissions for this exercise
        current_week = self.tracker.progress["current_week"]
        exercise_name = f"branden_week_{current_week}"
        
        # Check if any submission files exist for this exercise
        has_existing_submissions = False
        for filename in os.listdir(self.submissions_dir):
            if filename.startswith(f"{exercise_name}_") and filename.endswith(".yaml"):
                has_existing_submissions = True
                break
        
        if not has_existing_submissions:
            return self.handle_first_time_user()
        return True
    
    def save_submission(self, exercise_name: str, date_str: str, stem: str, completions: List[str]):
        """Save submission in standard format: exercisename_datelike210431"""
        filename = f"{exercise_name}_{date_str}.yaml"
        filepath = os.path.join(self.submissions_dir, filename)
        
        data = {
            "journal": exercise_name,
            "date": date_str,
            "week": self.tracker.progress["current_week"],
            "day": self.tracker.progress["current_day"],
            "session": {
                "started_at": datetime.now().isoformat(),
                "ended_at": None,
                "duration_minutes": 0
            },
            "submissions": {
                stem: completions
            }
        }
        
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                existing_data = yaml.safe_load(f) or {}
                if "submissions" not in existing_data:
                    existing_data["submissions"] = {}
                existing_data["submissions"][stem] = completions
                data = existing_data
        
        with open(filepath, 'w') as f:
            yaml.dump(data, f, default_flow_style=False)
    
    def get_week_submissions(self, exercise_name: str, week_start: str) -> Dict[str, List[str]]:
        """Get all submissions for a week"""
        submissions = {}
        for i in range(7):
            current_date = datetime.strptime(week_start, "%Y-%m-%d") + timedelta(days=i)
            date_str = current_date.strftime("%Y%m%d")
            filename = f"{exercise_name}_{date_str}.yaml"
            filepath = os.path.join(self.submissions_dir, filename)
            
            if os.path.exists(filepath):
                with open(filepath, 'r') as f:
                    data = yaml.safe_load(f)
                    if data and "submissions" in data:
                        submissions.update(data["submissions"])
        
        return submissions
    
    def show_menu(self):
        """Show dynamic menu based on available exercises"""
        print("=========================================")
        print("        ENOUGH - Minimal Journal")
        print(" Inspired by Nathaniel Branden's Work")
        print("=========================================")
        print()
        print("Choose your exercise:")
        
        # List all exercises dynamically
        for i, exercise in enumerate(self.exercises, 1):
            print(f"{i}. {exercise['name']}")
        
        print("X. Analytics & Progress Overview")
        print()
    
    def handle_analytics(self):
        """Show analytics and progress overview"""
        print("=========================================")
        print("            Analytics & Progress")
        print("=========================================")
        print()
        
        # Get basic stats
        total_sessions = 0
        total_stems = 0
        current_streak = 0
        
        # Count submissions
        for filename in os.listdir(self.submissions_dir):
            if filename.endswith('.yaml'):
                total_sessions += 1
                filepath = os.path.join(self.submissions_dir, filename)
                with open(filepath, 'r') as f:
                    data = yaml.safe_load(f)
                    if data and "submissions" in data:
                        total_stems += len(data["submissions"])
        
        print(f"Journal: Nathaniel Branden - Sentence Completion Exercises")
        print()
        print(f"Total Sessions Completed: {total_sessions}")
        print(f"Total Sentence Stems Completed: {total_stems}")
        print(f"Current Streak: {current_streak} weeks (6 days/week target)")
        
        if self.tracker.progress.get("start_date"):
            last_completed = self.tracker.progress.get("last_completed", "Never")
            print(f"Last Completed: Week {self.tracker.progress['current_week']} | Day {self.tracker.progress['current_day']} ({last_completed})")
        
        print()
        print("Recent Session Summary:")
        if total_sessions > 0:
            print("- Last Session: Today")
            print("- Start Time: Recent")
            print("- Duration: Variable")
        
        # Show current month calendar
        print()
        print("-----------------------------------------")
        current_month = datetime.now().month
        current_year = datetime.now().year
        print(f"{calendar.month_name[current_month]} {current_year} Activity")
        print()
        
        # Simple calendar representation
        cal = calendar.monthcalendar(current_year, current_month)
        print("Mon  Tue  Wed  Thu  Fri  Sat  Sun")
        for week in cal:
            for day in week:
                if day == 0:
                    print("     ", end="")
                else:
                    # Check if there's a submission for this day
                    date_str = f"{current_year:04d}{current_month:02d}{day:02d}"
                    has_submission = any(f"_{date_str}.yaml" in f for f in os.listdir(self.submissions_dir))
                    if has_submission:
                        print("  x  ", end="")
                    else:
                        print(f"  {day:2d} ", end="")
            print()
        
        print()
        print("Legend:")
        print("- x = Completed session")
        print("- (blank) = No activity")
        print("- 6 sessions per week required to maintain streak")
        print()
        input("Press Enter to continue...")
    
    def get_user_completions(self, stem: str) -> List[str]:
        """Get user completions with proper UX"""
        completions = []
        print(f"\n{stem}")
        print("Enter at least 6 responses (or type 'submit' to continue when ready):")
        
        # Wait 2 seconds, then clear terminal
        time.sleep(2)
        self.clear_terminal()
        
        print(f"\n{stem}")
        print("Enter at least 6 responses (or type 'submit' to continue when ready):")
        
        while len(completions) < 10:
            completion = input(f"{len(completions) + 1}. ").strip()
            
            if completion.lower() == "submit":
                if len(completions) >= 6:
                    break
                else:
                    print("Must submit at least 6 endings")
                    continue
            
            if completion:
                completions.append(completion)
        
        print("✔️ Submission accepted. Proceeding to next sentence stem...")
        time.sleep(2)
        self.clear_terminal()
        
        return completions
    
    def handle_weekend_reflection(self, exercise: Dict, week_start: str):
        """Handle weekend reflection - one of the main features"""
        print("\nWeek 1 | Day 6")
        print()
        print("Reflect on this weeks submissions.")
        print("Enter at least 6 responses (or type 'submit' to continue when ready):")
        
        # Wait 2 seconds, then clear terminal
        time.sleep(2)
        self.clear_terminal()
        
        current_week = self.tracker.progress["current_week"]
        exercise_name = f"branden_week_{current_week}"
        
        submissions = self.get_week_submissions(exercise_name, week_start)
        
        for stem, completions in submissions.items():
            print(f"\nWeek 1 | Day 6 - Reflect")
            print()
            print(f'"{stem}"')
            print()
            
            # Show their submissions for this week
            for i, completion in enumerate(completions, 1):
                print(f"{i}. {completion}")
            
            print()
            reflection_stem = "If any of what I have been writing this week is true..."
            print(f'"{reflection_stem}"')
            print()
            reflection_completions = self.get_user_completions(reflection_stem)
            
            # Save weekend reflection
            current_date = datetime.now().strftime("%Y%m%d")
            self.save_submission(exercise_name, current_date, reflection_stem, reflection_completions)
    
    def run_custom_exercise(self, exercise: Dict):
        """Run a custom exercise"""
        print(f"\n{exercise['name']}")
        print("=" * 50)
        
        exercise_name = f"custom_{exercise['time']}"
        current_date = datetime.now().strftime("%Y%m%d")
        
        # Run all stems for custom exercises
        for i, stem in enumerate(exercise["stems"], 1):
            print(f"\nStem {i}: {stem}")
            completions = self.get_user_completions(stem)
            
            # Save submission
            self.save_submission(exercise_name, current_date, stem, completions)
        
        print(f"\n✅ Completed {exercise['name']}")

    def run_exercise(self, exercise: Dict):
        """Run the main branden exercise"""
        current_week = self.tracker.progress["current_week"]
        current_day = self.tracker.progress["current_day"]
        
        print(f"\nWeek {current_week} | Day {current_day}")
        
        # Generate exercise name based on week
        exercise_name = f"branden_week_{current_week}"
        
        # Check if it's weekend
        today = datetime.now()
        if today.weekday() >= 5:  # Saturday = 5, Sunday = 6
            week_start = (today - timedelta(days=today.weekday())).strftime("%Y-%m-%d")
            self.handle_weekend_reflection(exercise, week_start)
            return
        
        # Handle regular weekday
        stems = exercise["stems"]
        current_stem_index = (current_day - 1) % len(stems)
        
        if current_stem_index < len(stems):
            stem = stems[current_stem_index]
            completions = self.get_user_completions(stem)
            
            # Save submission
            current_date = datetime.now().strftime("%Y%m%d")
            self.save_submission(exercise_name, current_date, stem, completions)
            
            # Update progress
            if current_stem_index == len(stems) - 1:
                # Move to next week
                self.tracker.update_progress(current_week + 1, 1)
            else:
                # Move to next day
                self.tracker.update_progress(current_week, current_day + 1)
    
    def main(self):
        """Main application loop"""
        while True:
            self.show_menu()
            choice = input("Enter your choice: ").strip().upper()
            
            if choice == "X":
                self.handle_analytics()
                continue
            
            try:
                choice_num = int(choice)
                if 1 <= choice_num <= len(self.exercises):
                    selected_exercise = self.exercises[choice_num - 1]
                    
                    if selected_exercise.get('type') == 'branden':
                        # Check if user needs setup for this specific exercise
                        if not self.check_and_setup_user():
                            continue
                        
                        exercise = self.get_current_exercise()
                        if exercise:
                            self.run_exercise(exercise)
                        else:
                            print("No exercise found for current week")
                    else:
                        # Custom exercise
                        self.run_custom_exercise(selected_exercise)
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid choice. Please try again.")


def main():
    journaler = Journaler()
    journaler.main()


if __name__ == "__main__":
    main() 