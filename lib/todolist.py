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
