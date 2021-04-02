#Datum poslední úpravy: 23.03.2021

import os
import subprocess

import PySimpleGUI as sg

sg.change_look_and_feel("Topanga")

#menu window
layout = [[sg.Text ("What would you like me to start?"),],
        [sg.Text(("***************************************************************"), key = 'OUTPUT')],
        [sg.Button("Word game"),sg.Button("Draw me something"), sg.Button("Info"), sg.Button("Exit")]]

window = sg.Window("Appka menu", layout)
window1_active = False
window2_active = False
while True:
    event, values = window.read(timeout=100)

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    #game window
    if event == "Word game" :

        answer = "Word game has started!"

        window['OUTPUT'].update(answer)

        command = "Game-EN"

        subprocess.Popen(command)

    #info window
    if not window1_active and event == 'Info':
        window1_active = True
        answer = "For more info contact the author tom.ferdan@seznamcz"

        window['OUTPUT'].update(answer)




        layout1 = [[sg.Text ("Author: Tomáš Ferdan | Date of publishment: 17:06 CET 23.03.2021 | Version: 1.13 | Creative Commons")],
                   [sg.Button('Exit')]]


        window1 = sg.Window("Info", layout1)



    if window1_active:
        event1, values1 = window1.read(timeout=100)

        if event1 == sg.WIN_CLOSED or event1 == 'Exit':
            window1_active  = False
            window1.close()

    #drawing window
    if not window2_active and event == 'Draw me something':
        window2_active = True

        layout2 = [[sg.Text ("What would you like me to draw?")],
                    [sg.Text(("***************************************************"), key = 'OUTPUT2')],
                   [sg.Button('Hearth'), sg.Button("Exit")]]


        window2 = sg.Window("Drawing", layout2)



    if window2_active:
        event2, values2 = window2.read(timeout=100)

        if event2 == sg.WIN_CLOSED or event2 == 'Exit':
            window2_active  = False
            window2.close()

        #drawing
        if event2 == "Hearth" :

            answer2 = "Drawing has started, be patient."

            window2['OUTPUT2'].update(answer2)

            command = "Hearth-EN"

            subprocess.Popen(command)
