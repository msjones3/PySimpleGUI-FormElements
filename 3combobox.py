import PySimpleGUI as PSG

rows = [
            [PSG.InputCombo(["XBOX","PS4"],key="CONSOLE")],
            [PSG.ReadFormButton("Submit values")]
       ]

form = PSG.FlexForm("This is a form.")
form.Layout(rows)

while True:
    button, value = form.Read()
    if value["CONSOLE"] == "XBOX":
        print("XBOX selected.")
    if value["CONSOLE"] == "PS4":
        print("PS4 selected.")
