import PySimpleGUI as PSG

rows = [
            [PSG.Checkbox("XBOX",key="XBOX")],
            [PSG.Checkbox("PS4",key="PS4",default=True)],
            [PSG.ReadFormButton("Submit values")]
       ]

form = PSG.FlexForm("This is a form.")
form.Layout(rows)

while True:
    button, value = form.Read()
    if value["XBOX"]:
        print("XBOX selected.")
    if value["PS4"]:
        print("PS4 selected.")
