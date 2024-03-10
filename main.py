from wrapper import ToDoList

def run_todo():
    client = ToDoList()
    print("\n\nWelcome to your To Do List!")
    client.view_list()
    print("\n\nIt appear there is nothing on your list yet. Let's get started!\n\n")
    while True:
        prompt = input("What would you like to do?\n1. Add new task\n2. Set task to complete\n3. Delete task\n4. Show list\n5. Quit\n\nEnter number for your choice:  ")
        if prompt == '1':
            client.add_task()
        elif prompt == '2':
            client.set_complete()
        elif prompt == '3':
            client.delete_task()
        elif prompt == '4':
            client.view_list()
        elif prompt == '5':
            client.view_list()
            break
        else:
            print("\033[0;31mInvalid response. Please enter a number: \033[0m")
        





run_todo()