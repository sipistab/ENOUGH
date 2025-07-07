"""Command-line interface for the sentence completion program."""
import sys
from typing import Dict, List
from pathlib import Path
import click
from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.panel import Panel
from rich.table import Table
from ..core.exercise_manager import ExerciseManager

console = Console()

def print_welcome() -> None:
    """Display welcome message and program information."""
    console.print(Panel.fit(
        "[bold blue]Welcome to the Sentence Completion Program[/bold blue]\n\n"
        "Based on Nathaniel Branden's sentence completion exercises\n"
        "Use this program for daily self-reflection and personal growth.",
        title="Welcome",
        border_style="blue"
    ))

def get_week_number() -> int:
    """Get week number from user input.
    
    Returns:
        int: Week number between 1 and 30
    """
    while True:
        try:
            week = int(Prompt.ask("Enter week number", default="1"))
            if 1 <= week <= 30:
                return week
            console.print("[red]Week must be between 1 and 30[/red]")
        except ValueError:
            console.print("[red]Please enter a valid number[/red]")

def get_day_number() -> int:
    """Get day number from user input.
    
    Returns:
        int: Day number between 1 and 5
    """
    while True:
        try:
            day = int(Prompt.ask("Enter day number", default="1"))
            if 1 <= day <= 5:
                return day
            console.print("[red]Day must be between 1 and 5[/red]")
        except ValueError:
            console.print("[red]Please enter a valid number[/red]")

def collect_responses(prompts: List[str]) -> Dict[str, List[str]]:
    """Collect user responses for each prompt.
    
    Args:
        prompts: List of exercise prompts
        
    Returns:
        Dictionary mapping prompts to lists of responses
    """
    responses = {}
    
    for prompt in prompts:
        console.print(f"\n[bold green]{prompt}[/bold green]")
        console.print("Enter 5 completions (press Enter twice to finish):")
        
        prompt_responses = []
        empty_lines = 0
        
        while len(prompt_responses) < 5 and empty_lines < 2:
            response = Prompt.ask(f"{len(prompt_responses) + 1}")
            if response.strip():
                prompt_responses.append(response)
                empty_lines = 0
            else:
                empty_lines += 1
                
        responses[prompt] = prompt_responses
        
    return responses

def display_weekly_summary(compiled_data: Dict[str, List[str]]) -> None:
    """Display compiled weekly responses in a table.
    
    Args:
        compiled_data: Dictionary mapping prompts to lists of responses
    """
    table = Table(title="Weekly Summary", show_header=True, header_style="bold magenta")
    table.add_column("Prompt", style="cyan", no_wrap=True)
    table.add_column("Responses", style="green")
    
    for prompt, responses in compiled_data.items():
        table.add_row(prompt, "\n".join(responses))
        
    console.print(table)

@click.group()
def cli():
    """Sentence Completion Program CLI."""
    pass

@cli.command()
def daily():
    """Complete daily exercises."""
    print_welcome()
    
    manager = ExerciseManager()
    week = get_week_number()
    day = get_day_number()
    
    try:
        exercises = manager.get_daily_exercises(week, day)
        responses = collect_responses(exercises)
        manager.save_responses(week, day, responses)
        
        console.print("[green]Responses saved successfully![/green]")
        
        if Confirm.ask("Would you like to create a backup?"):
            manager.backup_data()
            console.print("[green]Backup created successfully![/green]")
            
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        sys.exit(1)

@cli.command()
def weekly():
    """Complete weekly assessment."""
    print_welcome()
    
    manager = ExerciseManager()
    week = get_week_number()
    
    try:
        compiled_data = manager.compile_week(week)
        display_weekly_summary(compiled_data)
        
        console.print("\n[bold]Weekly Assessment[/bold]")
        console.print("Reflect on your responses and complete the assessment:")
        
        assessment = collect_responses(list(compiled_data.keys()))
        manager.save_assessment(week, assessment)
        
        console.print("[green]Assessment saved successfully![/green]")
        
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        sys.exit(1)

@cli.command()
@click.argument('export_file', type=click.Path())
def export(export_file):
    """Export all data to a JSON file."""
    manager = ExerciseManager()
    
    try:
        manager.file_handler.export_data(export_file)
        console.print(f"[green]Data exported successfully to {export_file}![/green]")
        
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        sys.exit(1)

if __name__ == "__main__":
    cli() 