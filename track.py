import os , json ,time 
from datetime import datetime

print("Loading Menu.......")
time.sleep(10)

print("T-A-S-K- T-R-A-C-K-E-R  M-E-N-U")

def add():
        try: 
           print("Add a task:\n")
           now = datetime.now()
           title = input("Task Name: ").lower()
           description = input("Description: ").lower()
           status = input("Status ( Inprogress  / Completed ): ").lower()
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

           print("Adding tasks.....")
           time.sleep(10)

           print("\nTask added successfully!")
           time.sleep(3)
           Menu()
        except Exception as e:
            print(f"Unable to add task: {e}")
            

def edit_task():
    try:
        with open("Tasks.json", "r") as file:
            Tasks = json.load(file)

        Edit = input("Enter the task name to edit: ").lower()
        found = False

        for task in Tasks:
            if task["ID"] == Edit:
                found = True
                now = datetime.now()
                
                task["ID"] = input("New name: ").lower()
                task["DESCRIPTION"] = input("Description: ").lower()
                task["STATUS"] = input("Status: ").lower()
                task["UPDATEDAT"] = now.strftime("%Y-%m-%d %H:%M:%S").lower()
                break

        if not found:
            print("Task not found.")
        else:
            with open("Tasks.json", "w") as file:
                json.dump(Tasks, file, indent=3)
            print("\n Task updated successfully.")
            time.sleep(3)
            Menu()
    except Exception as e:
        print(f"Unable to edit task: {e}")


def delete_task():
    try:
        with open("Tasks.json", "r") as file:
            tasks = json.load(file)

        if not tasks:
            print("No tasks to delete.")
            return

        delete_option = input("Choose Option (clear/delete): ").lower()

        if delete_option == "delete":
            delete_name = input("Enter the task name to delete: ").lower()
            found = False
            for i, task in enumerate(tasks):
                if task["ID"] == delete_name:
                    found = True
                    tasks.pop(i)
                    print("deleting task.....")
                    time.sleep(10)
                    print("Task deleted successfully.")
                    break

            if not found:
                print("Task not found.")

        elif delete_option == "clear":
            tasks.clear() 
            print("Inprogess.....")
            time.sleep(5)
            print("All tasks cleared successfully.")
        else:
            print("Invalid option. Please choose 'clear' or 'delete'.")

        with open("Tasks.json", "w") as file:
            json.dump(tasks, file, indent=3)
            time.sleep(3)
        Menu()
    except FileNotFoundError:
        print("Tasks.json file not found.")
    except json.JSONDecodeError:
        print("Error reading Tasks.json file. File may be corrupted.")
    except Exception as e:
        print(f"Unable to delete task: {e}")



def list_tasks ():
    try: 
        print("\nListing task..... ")

        time.sleep(10)
  
        with open('Tasks.json','r') as file :
            tasks = json.load(file)
            if tasks == [] :
              print("List empty\n")
              Menu()
            else:
              for task in tasks :
                  print (task)
                  time.sleep(3)
                  Menu()
    except FileNotFoundError:
        print("Tasks.json file not found ")
    except Exception as e :
        print(f"Unable to list tasks {e}")



def list_completed():
    try: 
        print("\nListing Completed  tasks..... ")
        time.sleep(10)
        with open('Tasks.json','r') as file:
            tasks = json.load(file)
            for task in tasks :
                if task["STATUS"] == "completed":
                    print(task)
                    time.sleep(3)
            Menu()
    except Exception as e:
        print(f"Unable to list_completed tasks{e}")


def list_Ongoing_task():
    try: 
        print("\nListing tasks inprogess..... ")
        time.sleep(10)
        with open('Tasks.json','r') as file:
            tasks = json.load(file)
            for task in tasks :
                if task["STATUS"] == "inprogress":
                    print(task)
                    time.sleep(3)
        Menu()
    except Exception as e:
        print(f"Unable to list_completed tasks{e}")

def Menu():
    try: 
    
        menu_option = ["Add task", "list task","edit task", "delete task","inprogress tasks ","completed tasks"]
    
        for menu in menu_option:
            print(f"{menu}")
        user_option = input("\nEnter Option : ").lower()
        
        if user_option.lower() == "add task":
           add()
        elif user_option.lower() == "list task":
            list_tasks()
        elif user_option.lower() == "edit task":
            edit_task()
        elif user_option.lower() == "inprogress tasks":
            list_Ongoing_task()

        elif user_option.lower() == "delete task":
            delete_task()

        elif user_option.lower() == "completed tasks":
            list_completed()
        
        else:
            print("invalid option ,,,")

    except Exception as e :
        print(f"An error Ocurred {e}")

Menu()
