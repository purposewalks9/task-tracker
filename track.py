import os , json ,time 
from datetime import datetime

print("Loading Task Tracker Menu...")
time.sleep(10)

print("\n" + "="*40)
print("         T A S K   T R A C K E R")
print("="*40 + "\n")

def add():
        try: 
           print("\n--- Add New Task ---\n")
           now = datetime.now()
           title = input("Enter Task Title        : ").lower()
           description = input("Enter Task Description  : ").lower()
           status = input("Enter Task Status (Inprogress / Completed): ").lower()
           created_at = now.strftime("%Y-%m-%d %H:%M:%S").lower()
           updated_at = ("").lower()
       
           new_task = {
               "ID": title.strip(),
               "DESCRIPTION": description.strip(),
               "STATUS": status.strip(),
               "CREATEDAT": created_at.strip(),
               "UPDATEDAT": updated_at.strip()
           }   

           if os.path.exists("Tasks.json"):
               with open("Tasks.json", "r") as file:
                try:
                   tasks = json.load(file)         
                except:
                   tasks = []
       
           tasks.append(new_task)
       
           with open("Tasks.json", "w") as file:
               json.dump(tasks, file, indent=3)

           print("\nSaving new task...")
           time.sleep(10)

           print("\n✅ Task added successfully!")
           time.sleep(3)
           Menu()
        except Exception as e:
            print(f"❌ Unable to add task: {e}")
            

def edit_task():
    try:
        with open("Tasks.json", "r") as file:
            Tasks = json.load(file)

        Edit = input("\nEnter the task title to edit: ").lower()
        found = False

        for task in Tasks:
            if task["ID"] == Edit:
                found = True
                now = datetime.now()
                
                print("\n--- Update Task ---\n")
                task["ID"] = input("New Task Title       : ").lower()
                task["DESCRIPTION"] = input("New Description      : ").lower()
                task["STATUS"] = input("New Status           : ").lower()
                task["UPDATEDAT"] = now.strftime("%Y-%m-%d %H:%M:%S").lower()
                break

        if not found:
            print("❌ Task not found.")
        else:
            with open("Tasks.json", "w") as file:
                json.dump(Tasks, file, indent=3)
            print("\n✅ Task updated successfully.")
            time.sleep(3)
            Menu()
    except Exception as e:
        print(f"❌ Unable to edit task: {e}")


def delete_task():
    try:
        with open("Tasks.json", "r") as file:
            tasks = json.load(file)

        if not tasks:
            print("⚠️ No tasks available to delete.")
            return

        delete_option = input("\nChoose an option (clear / delete): ").lower()

        if delete_option == "delete":
            delete_name = input("Enter the task title to delete: ").lower()
            found = False
            for i, task in enumerate(tasks):
                if task["ID"] == delete_name:
                    found = True
                    tasks.pop(i)
                    print("\nDeleting task...")
                    time.sleep(10)
                    print("✅ Task deleted successfully.")
                    break

            if not found:
                print("❌ Task not found.")

        elif delete_option == "clear":
            tasks.clear() 
            print("\nClearing all tasks...")
            time.sleep(5)
            print("✅ All tasks cleared successfully.")
        else:
            print("❌ Invalid option. Please choose 'clear' or 'delete'.")

        with open("Tasks.json", "w") as file:
            json.dump(tasks, file, indent=3)
            time.sleep(3)
        Menu()
    except FileNotFoundError:
        print("❌ Tasks.json file not found.")
    except json.JSONDecodeError:
        print("❌ Error reading Tasks.json file. File may be corrupted.")
    except Exception as e:
        print(f"❌ Unable to delete task: {e}")



def list_tasks():
    try: 
        print("\n📋 Listing all tasks...")

        time.sleep(10)
  
        with open('Tasks.json','r') as file:
            tasks = json.load(file)
            if tasks == []:
                print("⚠️ No tasks found.\n")
                Menu()
            else:
                for task in tasks:
                    print("\n-----------------------------")
                    for key, value in task.items():
                        print(f"{key.capitalize()} : {value}")
                    print("-----------------------------")
                    time.sleep(3)
                Menu()
    except FileNotFoundError:
        print("❌ Task file not found.")
    except Exception as e:
        print(f"❌ Unable to display tasks: {e}")



def list_completed():
    try: 
        print("\n✅ Displaying completed tasks...")
        time.sleep(10)
        with open('Tasks.json','r') as file:
            tasks = json.load(file)
            for task in tasks:
                if task["STATUS"] == "completed":
                    print("\n-----------------------------")
                    for key, value in task.items():
                        print(f"{key.capitalize()} : {value}")
                    print("-----------------------------")
                    time.sleep(3)
            Menu()
    except Exception as e:
        print(f"❌ Unable to display completed tasks: {e}")


def list_Ongoing_task():
    try: 
        print("\n🔄 Displaying in-progress tasks...")
        time.sleep(10)
        with open('Tasks.json','r') as file:
            tasks = json.load(file)
            for task in tasks:
                if task["STATUS"] == "inprogress":
                    print("\n-----------------------------")
                    for key, value in task.items():
                        print(f"{key.capitalize()} : {value}")
                    print("-----------------------------")
                    time.sleep(3)
        Menu()
    except Exception as e:
        print(f"❌ Unable to display in-progress tasks: {e}")

def Menu():
    try: 
    
        menu_option = ["Add Task", "List Task", "Edit Task", "Delete Task", "Inprogress Tasks", "Completed Tasks"]
    
        print("\n" + "="*40)
        print("             M A I N   M E N U")
        print("="*40)
        
        for menu in menu_option:
            print(f"➡️  {menu}")
        user_option = input("\nSelect an option: ").lower()
        
        if user_option == "add task":
           add()
        elif user_option == "list task":
            list_tasks()
        elif user_option == "edit task":
            edit_task()
        elif user_option == "inprogress tasks":
            list_Ongoing_task()
        elif user_option == "delete task":
            delete_task()
        elif user_option == "completed tasks":
            list_completed()
        else:
            print("❌ Invalid option. Please try again.")

    except Exception as e:
        print(f"❌ An error occurred: {e}")

Menu()


# I Enhanced texts with AI