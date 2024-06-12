def add_task(task, task_list):
    task_list.append({"task": task, "completed": False})
    print("Task added successfully!")

def view_tasks(task_list):
    if task_list:
        print("Your to-do list:")
        for index, task in enumerate(task_list, start=1):
            status = "✓" if task["completed"] else " "
            print(f"{index}. [{status}] {task['task']}")
    else:
        print("Your to-do list is empty.")

def mark_complete(task_index, task_list):
    if 0 < task_index <= len(task_list):
        task_list[task_index - 1]["completed"] = True
        print("Task marked as complete!")
    else:
        print("Invalid task index.")
        
def delete_task(task_index, task_list):
    if 0 < task_index <= len(task_list):
        del task_list[task_index - 1]
        print("Task deleted successfully!")
    else:
        print("Invalid task index.")

# Main function
def main():
    tasks = []

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(task, tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            task_index = int(input("Enter the task index to mark as complete: "))
            mark_complete(task_index, tasks)
        elif choice == "4":
            task_index = int(input("Enter the task index to delete: "))
            delete_task(task_index, tasks)
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
