todos = []
while True:
    action = input("Type add, show, edit or exit: ")

    if action.startswith("add") or action.startswith("new"):
        todo = input("Enter a todo: ")
        todos.append(todo)
    elif 'show' == action.strip().lower():
        for index, item in enumerate(todos):
            row = f"{index}{item}"
            print(row)
    elif 'edit' in action.strip().lower():
        number = int(input("Enter the number of the todo to edit: "))
        if 0 < number <= len(todos):
            new_todo = input("Enter the new todo: ")
            todos[number - 1] = new_todo
        else:
            print("Invalid number.")
    elif 'complete' in action.strip().lower():
        try:
            number = int(input("Enter the number of the todo to complete: "))
            if 0 < number <= len(todos):
                todos.pop(number - 1)
            else:
                print("Invalid number.")
        except ValueError:
            print("Your command is not valid.")
            continue
    elif 'exit' == action.strip().lower():
        break
    else:
        print("Command not valid.")
print("Bye!")