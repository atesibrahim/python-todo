import functions
import FreeSimpleGUI as fsgui
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

fsgui.theme("Black")

clock = fsgui.Text("", key="clock")
label = fsgui.Text("Type in a to-do")
input_box = fsgui.InputText(tooltip="Enter todo", key="todo")
add_button = fsgui.Button(size=1, image_source="add_icon.png", tooltip="Add todo",)
list_box = fsgui.Listbox(values=functions.get_todos(), key="todos",
                         enable_events=True, size=[45, 10])

edit_button = fsgui.Button("Edit")
complete_button = fsgui.Button("Complete")
exit_button = fsgui.Button("Exit")

layout = [[clock],
          [label],
          [input_box, add_button],
          [list_box, edit_button, complete_button],
          [exit_button]]

window = fsgui.Window("My To-Do App",
                      layout=layout,

                      font=("Helvetica", 20))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    if event == "Add":
        todos = functions.get_todos()
        new_todo = window["todo"].get() + "\n"
        todos.append(new_todo)
        functions.write_todos(todos)
        window["todos"].update(values=todos)
    elif event == "Edit":
        try:
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + "\n"
            functions.write_todos(todos)
            window["todos"].update(values=todos)

        except IndexError:
            fsgui.popup("Please select an item first", font=("Helvetica", 20))
    elif event == "Complete":
        try:
            todo_to_complete = values["todos"][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")
        except IndexError:
            fsgui.popup("Please select an item first", font=("Helvetica", 20))
    elif event == "todos":
        window["todo"].update(value=values["todos"][0])
    elif event == "Exit":
        break
    elif event == fsgui.WIN_CLOSED:
        break

window.close()
