import os
a= "tasks.txt"
def l():
    if not os.path.exists(a):
        return []
    with open(a, "r") as file:
        return [line.strip() for line in file.readlines()]

def save(t):
    with open(a, "w") as file:
        for task in t:
            file.write(task + "\n")

def add(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        save(tasks)
        print("Task added successfully")
    else:
        print("Task cannot be empty.")

def remove(tasks):
    view(tasks)
    try:
        task_num=int(input("Enter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save(tasks)
            print("Removed task:{}".format(removed))
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number. try agine")

def view(tasks):
    if not tasks:
        print("No tasks to show here.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def main():
    tasks = l()
    while True:
        print("=" * 60)
        print("\tTo-do-list-daily")
        print("=" * 60)
        print("\t1.add list")
        print("\t2.remove list")
        print("\t3.view list")
        print("\t4.exit list")
        print("="*60)
        c=input("Choose an  one option: ")

        if c=="3":
            view(tasks)
        elif c=="1":
            add(tasks)
        elif c=="2":
            remove(tasks)
        elif c=="4":
            print("your Tasks will be  saved successfully")
            break
        else:
            print("Invalid input choice  Try again.")

if __name__ == "__main__":
        main()
