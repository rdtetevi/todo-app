import PySimpleGUI as sg
from convertitor import convert


label_feet = sg.Text("Enter feet:")
feet_input = sg.Input(key="feets")
feet_float = float()

label_inches = sg.Text("Enter inches:")
inches_input = sg.Input(key="inches")


convert_btn = sg.Button("Convert")

label_mess = sg.Text(key="output")

window = sg.Window("Convertor", layout= [[label_feet, feet_input],
                                         [label_inches, inches_input],
                                         [convert_btn, label_mess]])

while True:
    event, values = window.read()
    print(event, values)
    """
    # event = il button convert_btn 
    # values = {'feets': '2', 'inches': '3'} dictionary che contiene le key dei input e come valori dati passati dall'utenti
    print(f"event--{event} values--{values}")
    """
    convert_res = convert(float(values['feets']), float(values['inches']))
    window["output"].update(value=f"{convert_res} m")


window.close()
