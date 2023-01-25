import PySimpleGUI as sg

layout = [
    [sg.Text("Hello from PySimpleGUI")],
    [sg.Button("Ok")]
]

# create the window
window = sg.Window("Demo", layout)

# create event loop
while True:
    event, values = window.read()
    # end button if user closes window or presses the ok button.
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()
