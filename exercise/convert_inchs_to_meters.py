import FreeSimpleGUI as sg
from converters import convert_to_meters

feet_label = sg.Text("Feet")
feet_input = sg.Input(key="feet")
inches_label = sg.Text("Inches")
inches_input = sg.Input(key="inches")
convert_button = sg.Button("Convert")
output_label = sg.Text("", key="output")
window = sg.Window("Inches to Meters Converter",
                   layout=[
                       [feet_label, feet_input],
                       [inches_label, inches_input],
                       [convert_button, output_label]
                   ])
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    feet = float(values["feet"])
    inches = float(values["inches"])
    meters = convert_to_meters(feet, inches)
    window["output"].update(value=f"{feet} feet and {inches} inches is {meters:.2f} meters")
window.close()