# daily_reminder.py
# A simple program to give a customized reminder for one task.

# Prompt user for details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match-case handles priority levels
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"Reminder: '{task}' has an unspecified priority"

# Check if time-sensitive
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    # Add a relaxed note for non-time-bound tasks
    if priority == "low":
        message += ". Consider completing it when you have free time."

print(message)
