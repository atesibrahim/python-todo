todos = []
while True:
    action = input("Type add, show, edit or exit: ")
    match action.strip():
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 'display':
            for index, item in enumerate(todos):
                row = f"{index}{item}"
                print(row)
        case 'edit':
            number = int(input("Enter the number of the todo to edit: "))
            if 0 < number <= len(todos):
                new_todo = input("Enter the new todo: ")
                todos[number - 1] = new_todo
            else:
                print("Invalid number.")
        case 'complete':
            number = int(input("Enter the number of the todo to complete: "))
            if 0 < number <= len(todos):
                todos.pop(number - 1)
            else:
                print("Invalid number.")
        case 'exit':
            break
print("Bye!")