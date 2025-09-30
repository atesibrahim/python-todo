import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    action = input("Type add, show, edit or exit: ")
    action = action.strip()

    if action.startswith("add") or action.startswith("new"):
        todo = input("Enter a todo: ") + "\n"
        todos = functions.get_todos()
        todos.append(todo)

        functions.write_todos(todos)

    elif action.startswith('show') or action.startswith('display'):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            row = f"{index + 1}-{item.strip()}"
            print(row)

    elif 'edit' in action:
        try:
            todos = functions.get_todos()
            number = int(input("Enter the number of the todo to edit: "))
            if 0 < number <= len(todos):
                new_todo = input("Enter the new todo: ") + "\n"
                functions.edit_todo(todos, number - 1, new_todo)
            else:
                print("Invalid number.")
        except ValueError:
            print("Your command is not valid.")
            continue

    elif 'complete' in action:
        try:
            todos = functions.get_todos()
            number = int(input("Enter the number of the todo to complete: "))
            if 0 < number <= len(todos):
                functions.remove_todo(number - 1)
            else:
                print("Invalid number.")
        except ValueError:
            print("Your command is not valid.")
            continue

    elif 'exit' == action:
        break

    else:
        print("Command not valid.")