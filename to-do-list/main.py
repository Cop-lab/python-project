# create a to-do-list where user can add, view, update and delete an items 
tasks = []

while True:
    print("\n**To-Do-List**")
    
    try:
        choice = int(input("1. Add Task\n"
                       "2. View Task\n"
                       "3. Update Task\n"
                       "4. Delete Task\n"
                       "5. Exit\n"
                       "\nEnter Your Choice: "))
        if choice == 1:
            task = input("Enter Your Task: ").capitalize()
            tasks.append(task)
            print(f"{task} successfully added")
        elif choice == 2:
            if len(tasks) == 0:
                print("Your task list is empty!")
            else:
                print("Here Is Your Tasks")
                for i in range(len(tasks)):
                    print(f"{i + 1}. {tasks[i]}")
        elif choice == 3:
            if len(tasks) == 0:
                print("No task to edit in list!")
            else:
                print("Which task number to edit?")
                for i in range(len(tasks)):
                    print(f"{i + 1}. {tasks[i]}")    
                num = int(input("\nEnter The Task Number: "))
                if num >= 1 and num <= len(tasks):
                    new_task = input("Enter Your Task: ").capitalize()
                    tasks[num - 1] = new_task
                    print("\nChanged succesfully")
                else:
                    print("Wrong number!")
        elif choice == 4:
            if len(tasks) == 0:
                print("No task to edit in list!")
            else:
                print("Which task number to edit")
                for i in range(len(tasks)):
                    print(f"{i + 1}. {tasks[i]}")
                print("0. To clear\n")
                num = int(input("Which Task To Remove?: "))
                if num == 0:
                    removed = tasks.clear()
                    print("Successfully clear") 
                elif num >= 1 and num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    print(f"{removed} successfully removed")
                else:
                    print("Wrong Number!")
        elif choice == 5:
            print("Exiting Program!!")
            exit()
        else:
            print("Incorrect task number")
    except ValueError:
        print("Invalid input.")
        
          
