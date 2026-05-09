tasks = [] # This is a List (like a array in C but dynamic)

def is_list_empty():
    if len(tasks) == 0: 
        print("List is empty nothing to show/delet")
        return True
    return False

while True: 
    print("\n --- TO-DO List ---")
    print("\n 1. Show Tasks")
    print("\n 2. Add Task")
    print("\n 3. Remove Task")
    print("\n 4. Exit")

    choice = input ("Choose an option: ")

    if choice == "1":
        if not is_list_empty():
            for i, task in enumerate(tasks):
                print(f"{i+1}.{task}")

    elif choice == "2":
        new_task = input("What do you want to do? ")
        tasks.append(new_task)

    elif choice == "3":
        if not is_list_empty():
            try:
                rm_task_index = input(f"Which task sould be deleted? available tasks 1 - {len(tasks)}: ")
                tasks.pop(int(rm_task_index) - 1)
            except (ValueError, IndexError):
                print("Invalide number. Pick a number from list.")

    elif choice == "4":
        break
    
    else:
        print("Invalid choice!")
