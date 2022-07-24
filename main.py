import PySimpleGUI as sg
import logging

logger = logging.getLogger(__name__)


def main(theme):
    sg.theme(theme)  # Set the theme of the program
    sg.set_options(font='Franklin 10', button_element_size=(6, 3))

    def Button(letter, key):
        return sg.Button(letter, key=key, size=(6, 3))
    layout = [
        [sg.Text("0",
                 key="-OUTPUT-",
                 font="Franklin26",
                 expand_x=True,
                 justification='right',
                 pad=(10, 20),
                 right_click_menu=theme_menu),

         ],
        # This is just one more way of pushing items to the right.
        # [sg.Push(), sg.Text("Position Test", font="Franklin26")],
        [sg.Button('Clear', key="-CLEAR-", expand_x=True),
         sg.Button('Enter', key="-ENTER-", expand_x=True)],
        [Button('7', "7", ), Button('8', "8"),
         Button('9', "9"), Button('/', "/"), ],

        [Button('4', "4"), Button('5', "5"),
         Button('6', "6"), Button('*', "*"), ],

        [Button('1', "1"), Button('2', "2"),
         Button('3', "3"), Button('-', "-"), ],

        [sg.Button('0', key="-0-", expand_x=True),
         Button('.', "."), Button('+', "+")]
    ]

    return sg.Window('Calculator', layout)


theme_menu = ['menu', ['LightGrey1', 'dark', 'Default', 'random']]
window = main('Default')
current_num = []
full_operation = []
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event in theme_menu[1]:
        window.close()
        window = main(event)

    if event in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']:
        current_num.append(event)
        num_string = ''.join(current_num)
        window['-OUTPUT-'].update(num_string)

    if event in ['/', '*', '-', '+']:
        full_operation.append(''.join(current_num))
        current_num = []
        full_operation.append(event)
        window['-OUTPUT-'].update('')

    if event == '-ENTER-':
        full_operation.append(''.join(current_num))
        result = eval(' '.join(full_operation))
        full_operation = []
        window['-OUTPUT-'].update(result)
        current_num = [str(result)]
        print(current_num)

    if event == '-CLEAR-':
        print(event)
        full_operation = []
        current_num = []
        window['-OUTPUT-'].update('0')


window.close()
