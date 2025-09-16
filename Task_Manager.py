import json
import os
from datetime import datetime
import sys, io

                                                                                      #Used for Force UTF-8 output in Windows console
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

                                                                                       # Global lists to store tasks
checklist = []
completed_tasks = []
incomplete_tasks = []

def save_tasks():
    """Save all tasks to a file"""
    data = {
        'checklist': checklist,
        'completed_tasks': completed_tasks,
        'incomplete_tasks': incomplete_tasks
    }
    with open('my_tasks.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print("✅ Tasks saved!")

def load_tasks():
    """Load tasks from file if it exists"""
    global checklist, completed_tasks, incomplete_tasks
    
    if os.path.exists('my_tasks.json'):
        with open('my_tasks.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            checklist = data.get('checklist', [])
            completed_tasks = data.get('completed_tasks', [])
            incomplete_tasks = data.get('incomplete_tasks', [])
        print("📂 Previous tasks loaded!")

def add_tasks():
    """Add tasks to daily checklist"""
    print("\n--- ADD TASKS TO YOUR CHECKLIST ---")
    print("Type your tasks one by one. Type 'done' when finished.")
    
    while True:
        task = input("Enter a task: ")
        
        if task.lower() == 'done':
            break
        
        if task:                                                                         # Check if task is not empty
            checklist.append(task)
            print(f"✅ Added: {task}")
        else:
            print("Please enter a task!")

def show_checklist():
    """Show current checklist"""
    print("\n--- TODAY'S CHECKLIST ---")
    
    if not checklist:
        print("No tasks in checklist.")
        return
    
    for i, task in enumerate(checklist, 1):
        print(f"{i}. {task}")

def review_tasks():
    """Review tasks and mark them as completed or incomplete"""
    if not checklist:
        print("No tasks to review!")
        return
    
    print("\n--- REVIEW YOUR TASKS ---")
    today = datetime.now().strftime('%Y-%m-%d')
    
    for task in checklist:
        print(f"\nTask: {task}")
        
        while True:
            answer = input("Did you complete this task? (y/n): ").lower()
            
            if answer == 'y':
                completed_tasks.append({
                    'task': task,
                    'date': today
                })
                print(f"✅ Great! '{task}' marked as completed!")
                break
            
            elif answer == 'n':
                incomplete_tasks.append({
                    'task': task,
                    'date': today
                })
                print(f"❌ '{task}' marked as incomplete. You can try again tomorrow!")
                break
            
            else:
                print("Please type 'y' for yes or 'n' for no.")
    
    
    checklist.clear()
    print("\n🎉 Review complete!")

def show_completed():
    """Show all completed tasks"""
    print("\n--- COMPLETED TASKS ---")
    
    if not completed_tasks:
        print("No completed tasks yet.")
        return
    
    for i, task_info in enumerate(completed_tasks, 1):
        print(f"{i}. ✅ {task_info['task']} (Date: {task_info['date']})")

def show_incomplete():
    """Show all incomplete tasks"""
    print("\n--- INCOMPLETE TASKS ---")
    
    if not incomplete_tasks:
        print("No incomplete tasks. Great job!")
        return
    
    for i, task_info in enumerate(incomplete_tasks, 1):
        print(f"{i}. ❌ {task_info['task']} (Date: {task_info['date']})")

def move_incomplete_to_today():
    """Move incomplete tasks to today's checklist"""
    if not incomplete_tasks:
        print("No incomplete tasks to move!")
        return
    
    print("\n--- MOVE INCOMPLETE TASKS TO TODAY ---")
    print("Which incomplete tasks do you want to work on today?")
    
    for i, task_info in enumerate(incomplete_tasks, 1):
        task = task_info['task']
        print(f"\n{i}. {task}")
        
        answer = input("Add this to today's checklist? (y/n): ").lower()
        
        if answer == 'y':
            checklist.append(task)
            print(f"✅ Added '{task}' to today's checklist!")

def show_summary():
    """Show summary of all tasks"""
    print("\n--- TASK SUMMARY ---")
    print(f"📝 Tasks in today's checklist: {len(checklist)}")
    print(f"✅ Total completed tasks: {len(completed_tasks)}")
    print(f"❌ Total incomplete tasks: {len(incomplete_tasks)}")

def show_menu():
    """Show main menu"""
    print("\n" + "="*40)
    print("       📋 DAILY TASK MANAGER")
    print("="*40)
    print("1. Add tasks to checklist")
    print("2. Show my checklist")
    print("3. Review tasks (mark complete/incomplete)")
    print("4. Show completed tasks")
    print("5. Show incomplete tasks")
    print("6. Move incomplete tasks to today")
    print("7. Show summary")
    print("8. Save and exit")
    print("="*40)

def main():
    """Main program"""
    print("🌟 Welcome to Daily Task Manager!")
    print(f"📅 Today is: {datetime.now().strftime('%Y-%m-%d')}")
    load_tasks()
    
    while True:
        show_menu()
        choice = input("Choose an option (1-8): ")
        
        if choice == '1':
            add_tasks()
        
        elif choice == '2':
            show_checklist()
        
        elif choice == '3':
            review_tasks()
        
        elif choice == '4':
            show_completed()
        
        elif choice == '5':
            show_incomplete()
        
        elif choice == '6':
            move_incomplete_to_today()
        
        elif choice == '7':
            show_summary()
        
        elif choice == '8':
            save_tasks()
            print("👋 Thanks for using Task Manager! Have a great day!")
            break
        
        else:
            print("❌ Invalid choice! Please choose 1-8.")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
