import PySimpleGUI as PSG

rows = [
            [PSG.Slider(range=(1, 100),
                        orientation="h",
                        size=(10, 20),
                        default_value=25,
                        key="mySlider")],
            [PSG.Multiline("type a \n story here",
                        key="myMultiline")],
            [PSG.ReadFormButton("Submit values")]
       ]

form = PSG.FlexForm("This is a form.")
form.Layout(rows)

while True:
    button, value = form.Read()
    print("Slider value: " + str(value["mySlider"]))
    print(value["myMultiline"])
