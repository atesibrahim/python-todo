def get_todos(filepath="files/todos.txt"):
    """ Read a text file and return the list of to-do items.

    Args:
        filepath (str): The path to the text file containing to-do items. Defaults to "files/todos.txt".

    Returns:
        list: A list of to-do items read from the file.
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos_local, filepath="files/todos.txt"):
    """ Write the list of to-do items to a text file.

    Args:
        todos_local (list): The list of to-do items to write to the file.
        filepath (str): The path to the text file where to-do items will be written. Defaults to "files/todos.txt".
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_local)

def complete_todos(todos_local, filepath="files/todos.txt"):
    """ Remove the last to-do item from the list and update the text file.

    Args:
        todos_local (list): The list of to-do items.
        filepath (str): The path to the text file where to-do items are stored. Defaults to "files/todos.txt".
    """
    if todos_local:
        todos_local.pop()
        write_todos(todos_local, filepath)
    else:
        print("No to-do items to complete.")

def remove_todo(number, filepath="files/todos.txt"):
    """ Remove a specific to-do item from the list and update the text file.

    Args:
        number (int): The index of the to-do item to remove (1-based).
        filepath (str): The path to the text file where to-do items are stored. Defaults to "files/todos.txt".
    """
    todos_local = get_todos(filepath)
    if 0 < number <= len(todos_local):
        todos_local.pop(number - 1)
        write_todos(todos_local, filepath)
    else:
        print("Invalid number.")

def edit_todo(todos_local, number, new_todo, filepath="files/todos.txt"):
    """ Edit a specific to-do item in the list and update the text file.

    Args:
        todos_local (list): The list of to-do items.
        number (int): The index of the to-do item to edit (1-based).
        new_todo (str): The new to-do item text.
        filepath (str): The path to the text file where to-do items are stored. Defaults to "files/todos.txt".
    """
    if 0 < number <= len(todos_local):
        todos_local[number - 1] = new_todo + "\n"
        write_todos(todos_local, filepath)
    else:
        print("Invalid number.")