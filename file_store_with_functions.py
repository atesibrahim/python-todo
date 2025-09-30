def get_todos(filepath="files/todos.txt"):
    """
    Read a text file and return the list of to-do items.
    :param filepath: Path to the text file
    :return: List of to-do items
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local

print(help(get_todos))

def write_todos(todos_local, filepath="files/todos.txt"):
    with open(filepath, 'w') as file:
        file.writelines(todos_local)

while True:
    action = input("Type add, show, edit or exit: ")
    match action.strip():
        case 'add':
            todo = input("Enter a todo: ")
            file = open("files/todos.txt", "r")
            todos = file.readlines()
            file.close()

            todos = get_todos()

            todos.append(todo + "\n")

            write_todos(todos)

        case 'show' | 'display':
            todos = get_todos()

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
            todos = get_todos()

            if 0 < number <= len(todos):
                new_todo = input("Enter the new todo: ")
                todos[number - 1] = new_todo + "\n"
                write_todos('files/todos.txt', todos)
            else:
                print("Invalid number.")
        case 'complete':
            number = int(input("Enter the number of the todo to complete: "))
            todos = get_todos('files/todos.txt')

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