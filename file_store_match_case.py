while True:
    action = input("Type add, show, edit or exit: ")
    match action.strip():
        case 'add':
            todo = input("Enter a todo: ") + "\n"
            file = open("files/todos.txt", "r")
            todos = file.readlines()
            file.close()

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            file = open("todos.txt", "w")
            file.writelines(todos)
            file.close()

            with open('files/todos.txt', 'a') as file:
                file.writelines(todos)

        case 'show' | 'display':
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            #new_todos = [item.strip("\n") for item in todos]

            #for item in todos:
            #    new_item = item.strip("\n")
            #    new_todos.append(new_item)

            #todos = new_todos

            for index, item in enumerate(todos):
                row = f"{index}-{item.strip("\n")}"
                print(row)
        case 'edit':
            number = int(input("Enter the number of the todo to edit: "))
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            if 0 < number <= len(todos):
                new_todo = input("Enter the new todo: ")
                todos[number - 1] = new_todo + "\n"
                with open('files/todos.txt', 'w') as file:
                    file.writelines(todos)
            else:
                print("Invalid number.")
        case 'complete':
            number = int(input("Enter the number of the todo to complete: "))
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            if 0 < number <= len(todos):
                index = number - 1
                completed_todo = todos[index].strip("\n")
                todos.pop(index)
                with open('files/todos.txt', 'w') as file:
                    file.writelines(todos)

                message = f"{completed_todo}Todo completed."
                print(message)
            else:
                print("Invalid number.")
        case 'exit' | 'x':
            break
print("Bye!")