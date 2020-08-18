import PySimpleGUI as PSG

values = ["XBOX","PS4"]

rows = [
            [PSG.Listbox(values,key="CONSOLE",size=(30,6))],
            [PSG.ReadFormButton("Submit values")]
       ]

form = PSG.FlexForm("This is a form.")
form.Layout(rows)

while True:
    button, value = form.Read()
    if "XBOX" in value["CONSOLE"]:
        print("XBOX selected.")
    if "PS4" in value["CONSOLE"]:
        print("PS4 selected.")