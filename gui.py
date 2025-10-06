import functions
import FreeSimpleGUI as fsgui

label = fsgui.Text("Type in a to-do")
input_box = fsgui.InputText(tooltip="Enter todo", key="todo")
add_button = fsgui.Button("Add")

window = fsgui.Window("My To-Do App",
                      layout=[[label], [input_box, add_button]],
                      font=("Helvetica", 20))

while True:
    event, values = window.read()
    if event == "Add":
        todos = functions.get_todos()
        new_todo = window["todo"].get() + "\n"
        todos.append(new_todo)
        functions.write_todos(todos)
    if event == fsgui.WIN_CLOSED:
        break

window.close()
