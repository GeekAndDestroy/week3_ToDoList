class Task:
    id_counter = 1

    def __init__(self, memo, priority):
        self.id = Task.id_counter
        Task.id_counter += 1
        self.complete = False
        self.complete_str = "_"
        self.memo = memo
        self.priority = priority
        self.priority_memo = f"{self.priority}{memo}\033[0m"

    def __str__(self):
        return self.memo

    
class ToDoList:
    num_tasks = 0
    tasks_completed = 0
    task_list = []

    def view_list(self):
        print("\n\n")
        print("+" + "-"*75 + "+")
        print("|{:^75}|".format("To-Do List"))
        print("+" + "-"*75 + "+")
        if self.num_tasks == 0:
            print("|{:_^5}|{:^69}|".format("_", "There are no tasks on your list yet."))
        else:
            for task in self.task_list: 
                print("|{:_^5}|{:^5}{:^75}|".format(task.complete_str,task.id, task.priority_memo)) 
        if self.num_tasks < 15: # prints out empty rows to make final list look nice, and encourage more tasks to be added
            for i in range(15 - self.num_tasks):
                print("|{:_^5}|{:^69}|".format("_", " "))
        print("+" + "-"*75 + "+")
        print("Priority: \033[0;32mlow\033[0m - \033[1;33mmedium\033[0m - \033[0;31mhigh\033[0m\n\n")

    def add_task(self):
        while True:
            memo = input("What do you need to do? (type 'back' to return to main menu) ").title()
            if memo.lower() == 'back':
                break
            else:
                while True:
                    priority_ask = input(f"\n1. \033[0;32mlow\033[0m\n2. \033[1;33mmedium\033[0m\n3. \033[0;31mhigh\033[0m\n\nPlease enter a number to set the priority of this task: ")
                    if priority_ask == '1':
                        priority = "\033[0;32m"
                        break
                    elif priority_ask == '2':
                        priority = "\033[1;33m"
                        break
                    elif priority_ask == '3':
                        priority = "\033[0;31m"
                        break
                    else:
                        print("\033[0;31mInvalid response. Please try again.\033[0m")  
                new_task = Task(memo, priority)
                self.task_list.append(new_task)
                ToDoList.num_tasks += 1
                break


    def set_complete(self):
        task_id = int(input("Enter the number for the task to mark as complete: "))
        for task in self.task_list:
            if task.id == task_id:
                task.complete = True
                task.complete_str = "√"
                task.priority = "\033[0m"
                self.tasks_completed += 1
                break
        else:
            print("\033[0;31mTask ID not found.\033[0m")

    def delete_task(self):
        task_id = int(input("Enter the number of the task to delete: "))
        for task in self.task_list:
            if task.complete == True:
                self.tasks_completed -= 1
            if task.id == task_id:
                self.task_list.remove(task)
                self.num_tasks -= 1
                break
        else:
            print("\033[0;31mTask ID not found.\033[0m")
