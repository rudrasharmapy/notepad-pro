#Datum poslední úpravy: 23.03.2021

import PySimpleGUI as sg

sg.change_look_and_feel("Topanga")

# window1 - menu of the game (In this window, the game will also display the results (sentences))

layout1 = [( sg.Text ("Enter ammount of players (Min. 2 and max. 10):"), sg. Input(key = "players")),
            [sg.Text(("**************************************************************************************************************************************************************************************************************"), key = 'OUTPUT1')],
            [sg.Text(("**************************************************************************************************************************************************************************************************************"), key = 'OUTPUT2')],
            [sg.Text(("**************************************************************************************************************************************************************************************************************"), key = 'OUTPUT3')],
            [sg.Text(("**************************************************************************************************************************************************************************************************************"), key = 'OUTPUT4')],
            [sg.Text(("**************************************************************************************************************************************************************************************************************"), key = 'OUTPUT5')],
            [sg.Text(("**************************************************************************************************************************************************************************************************************"), key = 'OUTPUT6')],
            [sg.Text(("**************************************************************************************************************************************************************************************************************"), key = 'OUTPUT7')],
            [sg.Text(("**************************************************************************************************************************************************************************************************************"), key = 'OUTPUT8')],
            [sg.Text(("**************************************************************************************************************************************************************************************************************"), key = 'OUTPUT9')],
            [sg.Text(("**************************************************************************************************************************************************************************************************************"), key = 'OUTPUT10')],
            [sg. Button("Continue"), sg.Button("Exit")]]

window1 = sg.Window('Game', layout1)

window2_active = False
while True:
    event1, values1 = window1.read(timeout=100)

    if event1 == sg.WIN_CLOSED or event1 == 'Exit':
        break

        #window2 - window for the first player (Here the player will be able to enter his sentence [parts of the sentence, such as where, when, who and etc.] and in the last phase, the program will mix them, so new sentences are created as the result)
    if not window2_active and event1 == 'Continue':
        window2_active = True

        i = 0 #variable ,,i" counts, how many times, the window for player to enter sentence has been opened

        players = int(values1["players"])
        if ((players >= 2) and (players <= 10)):
            if i < players :
                letter = "abcdefghijklm"[i]
                layout2 = [
                            ( sg.Text ("Enter when:"), sg. Input(key = "when")),
                            ( sg.Text ("Enter where:"), sg. Input(key = "where")),
                            ( sg.Text ("Enter who:"), sg. Input(key = "who")),
                            ( sg.Text ("Enter with_who:"), sg. Input(key = "with_who")),
                            ( sg.Text ("Enter what they did/were doing:"), sg. Input(key = "did")),
                            ( sg.Text ("Enter a thing or a person:"), sg. Input(key = "what")),
                            [sg. Button("Ok")]]

                window2 = sg.Window('Sentence', layout2)
                i = i + 1
    if window2_active:
        event2, values2 = window2.read(timeout=100)
        if event2 == sg.WIN_CLOSED:
            window2_active  = False
            window2.close()

        #saving process of the inputs (parts of the sentences)
        if event2 == "Ok" :
            when = values2["when"]
            where = values2["where"]
            who = values2["who"]
            with_who = values2["with_who"]
            did = values2["did"]
            what = values2["what"]

            if i == 1 :
                when_a = when + letter
                where_a = where + letter
                who_a = who + letter
                with_who_a = with_who + letter
                did_a = did + letter
                what_a = what + letter
            elif i == 2 :
                when_b = when + letter
                where_b = where + letter
                who_b = who + letter
                with_who_b = with_who + letter
                did_b = did + letter
                what_b = what + letter
            elif i == 3 :
                when_c = when + letter
                where_c = where + letter
                who_c = who + letter
                with_who_c = with_who + letter
                did_c = did + letter
                what_c = what + letter
            elif i == 4 :
                when_d = when + letter
                where_d= where + letter
                who_d = who + letter
                with_who_d = with_who + letter
                did_d = did + letter
                what_d = what + letter
            elif i == 5 :
                when_e = when + letter
                where_e = where + letter
                who_e = who + letter
                with_who_e = with_who + letter
                did_e = did + letter
                what_e = what + letter
            elif i == 6 :
                when_f = when + letter
                where_f = where + letter
                who_f = who + letter
                with_who_f = with_who + letter
                did_f = did + letter
                what_f = what + letter
            elif i == 7 :
                when_g = when + letter
                where_g = where + letter
                who_g = who + letter
                with_who_g = with_who + letter
                did_g = did + letter
                what_g = what + letter
            elif i == 8 :
                when_h = when + letter
                where_h = where + letter
                who_h = who + letter
                with_who_h = with_who + letter
                did_h = did + letter
                what_h = what + letter
            elif i == 9:
                when_i = when + letter
                where_i = where + letter
                who_i = who + letter
                with_who_i = with_who + letter
                did_i = did + letter
                what_i = what + letter
            elif i == 10 :
                when_j = when + letter
                where_j = where + letter
                who_j = who + letter
                with_who_j = with_who + letter
                did_j = did + letter
                what_j = what + letter

            window2_active  = False
            window2.close()

            #continuing with opening more windows for player to enter sentece, until the variable ,,i" is equal to ammount of players
            if i < players :
                window2_active = True
                letter = "abcdefghijklm"[i]
                layout2 = [
                            ( sg.Text ("Enter when:"), sg. Input(key = "when")),
                            ( sg.Text ("Enter where:"), sg. Input(key = "where")),
                            ( sg.Text ("Enter who:"), sg. Input(key = "who")),
                            ( sg.Text ("Enter s kým:"), sg. Input(key = "with_who")),
                            ( sg.Text ("Enter what did:"), sg. Input(key = "did")),
                            ( sg.Text ("Enter věc/člověka:"), sg. Input(key = "what")),
                            [sg. Button("Ok")]]

                window2 = sg.Window('Sentence', layout2)
                i = i + 1

            #the rest of the code is a system, how the game is mixing the words (In the future I would like to program the game to mix words randomly)
            else:
                if players == 2 :
                    result1 = '{0} '.format(when_a[0:-1]) + '{0} '.format(where_b[0:-1]) + '{0} '.format(who_a[0:-1]) + '{0} '.format(with_who_b[0:-1]) + '{0} '.format(did_a[0:-1]) + '{0} '.format(what_b[0:-1])
                    result2 = '{0} '.format (when_b[0:-1]) + '{0} '.format(where_a[0:-1]) + '{0} '.format(who_b[0:-1]) + '{0} '.format(with_who_a[0:-1]) + '{0} '.format(did_b[0:-1]) + '{0} '.format(what_a[0:-1])

                    window1['OUTPUT1'].update(result1)
                    window1['OUTPUT2'].update(result2)
                elif players == 3 :
                    result1 = '{0} '.format(when_a[0:-1]) + '{0} '.format(where_c[0:-1])+ '{0} '.format(who_b[0:-1])+ '{0} '.format(with_who_a[0:-1])+ '{0} '.format(did_c[0:-1])+ '{0} '.format(what_b[0:-1])
                    result2 = '{0} '.format(when_b[0:-1]) + '{0} '.format(where_a[0:-1])+ '{0} '.format(who_c[0:-1])+ '{0} '.format(with_who_b[0:-1])+ '{0} '.format(did_a[0:-1])+ '{0} '.format(what_c[0:-1])
                    result3 = '{0} '.format(when_c[0:-1]) + '{0} '.format(where_b[0:-1])+ '{0} '.format(who_a[0:-1])+ '{0} '.format(with_who_c[0:-1])+ '{0} '.format(did_b[0:-1])+ '{0} '.format(what_a[0:-1])

                    window1['OUTPUT1'].update(result1)
                    window1['OUTPUT2'].update(result2)
                    window1['OUTPUT3'].update(result3)
                elif players == 4 :
                    result1 = '{0} '.format(when_a[0:-1]) + '{0} '.format(where_d[0:-1])+ '{0} '.format(who_c[0:-1])+ '{0} '.format(with_who_b[0:-1])+ '{0} '.format(did_a[0:-1])+ '{0} '.format(what_a[0:-1])
                    result2 = '{0} '.format(when_b[0:-1]) + '{0} '.format(where_a[0:-1])+ '{0} '.format(who_d[0:-1])+ '{0} '.format(with_who_c[0:-1])+ '{0} '.format(did_c[0:-1])+ '{0} '.format(what_d[0:-1])
                    result3 = '{0} '.format(when_c[0:-1]) + '{0} '.format(where_b[0:-1])+ '{0} '.format(who_a[0:-1])+ '{0} '.format(with_who_d[0:-1])+ '{0} '.format(did_b[0:-1])+ '{0} '.format(what_b[0:-1])
                    result4 = '{0} '.format(when_d[0:-1]) + '{0} '.format(where_c[0:-1])+ '{0} '.format(who_b[0:-1])+ '{0} '.format(with_who_a[0:-1])+ '{0} '.format(did_d[0:-1])+ '{0} '.format(what_c[0:-1])

                    window1['OUTPUT1'].update(result1)
                    window1['OUTPUT2'].update(result2)
                    window1['OUTPUT3'].update(result3)
                    window1['OUTPUT4'].update(result4)
                elif players == 5 :
                    result1 = '{0} '.format(when_b[0:-1]) + '{0} '.format(where_e[0:-1])+ '{0} '.format(who_c[0:-1])+ '{0} '.format(with_who_a[0:-1])+ '{0} '.format(did_d[0:-1])+ '{0} '.format(what_a[0:-1])
                    result2 = '{0} '.format(when_d[0:-1]) + '{0} '.format(where_b[0:-1])+ '{0} '.format(who_b[0:-1])+ '{0} '.format(with_who_c[0:-1])+ '{0} '.format(did_c[0:-1])+ '{0} '.format(what_d[0:-1])
                    result3 = '{0} '.format(when_a[0:-1]) + '{0} '.format(where_a[0:-1])+ '{0} '.format(who_d[0:-1])+ '{0} '.format(with_who_e[0:-1])+ '{0} '.format(did_b[0:-1])+ '{0} '.format(what_e[0:-1])
                    result4 = '{0} '.format(when_c[0:-1]) + '{0} '.format(where_d[0:-1])+ '{0} '.format(who_a[0:-1])+ '{0} '.format(with_who_b[0:-1])+ '{0} '.format(did_e[0:-1])+ '{0} '.format(what_c[0:-1])
                    result5 = '{0} '.format(when_e[0:-1]) + '{0} '.format(where_c[0:-1])+ '{0} '.format(who_e[0:-1])+ '{0} '.format(with_who_d[0:-1])+ '{0} '.format(did_a[0:-1])+ '{0} '.format(what_b[0:-1])

                    window1['OUTPUT1'].update(result1)
                    window1['OUTPUT2'].update(result2)
                    window1['OUTPUT3'].update(result3)
                    window1['OUTPUT4'].update(result4)
                    window1['OUTPUT5'].update(result5)
                elif players == 6 :
                    result1 = '{0} '.format(when_a[0:-1]) + '{0} '.format(where_b[0:-1])+ '{0} '.format(who_c[0:-1])+ '{0} '.format(with_who_d[0:-1])+ '{0} '.format(did_e[0:-1])+ '{0} '.format(what_f[0:-1])
                    result2 = '{0} '.format(when_b[0:-1]) + '{0} '.format(where_c[0:-1])+ '{0} '.format(who_d[0:-1])+ '{0} '.format(with_who_e[0:-1])+ '{0} '.format(did_f[0:-1])+ '{0} '.format(what_a[0:-1])
                    result3 = '{0} '.format(when_f[0:-1]) + '{0} '.format(where_a[0:-1])+ '{0} '.format(who_b[0:-1])+ '{0} '.format(with_who_c[0:-1])+ '{0} '.format(did_d[0:-1])+ '{0} '.format(what_e[0:-1])
                    result4 = '{0} '.format(when_e[0:-1]) + '{0} '.format(where_f[0:-1])+ '{0} '.format(who_a[0:-1])+ '{0} '.format(with_who_b[0:-1])+ '{0} '.format(did_c[0:-1])+ '{0} '.format(what_d[0:-1])
                    result5 = '{0} '.format(when_d[0:-1]) + '{0} '.format(where_e[0:-1])+ '{0} '.format(who_f[0:-1])+ '{0} '.format(with_who_a[0:-1])+ '{0} '.format(did_b[0:-1])+ '{0} '.format(what_c[0:-1])
                    result6 = '{0} '.format(when_c[0:-1]) + '{0} '.format(where_d[0:-1])+ '{0} '.format(who_e[0:-1])+ '{0} '.format(with_who_f[0:-1])+ '{0} '.format(did_a[0:-1])+ '{0} '.format(what_b[0:-1])

                    window1['OUTPUT1'].update(result1)
                    window1['OUTPUT2'].update(result2)
                    window1['OUTPUT3'].update(result3)
                    window1['OUTPUT4'].update(result4)
                    window1['OUTPUT5'].update(result5)
                    window1['OUTPUT6'].update(result6)
                elif players == 7 :
                    result1 = '{0} '.format(when_a[0:-1]) + '{0} '.format(where_b[0:-1])+ '{0} '.format(who_c[0:-1])+ '{0} '.format(with_who_d[0:-1])+ '{0} '.format(did_e[0:-1])+ '{0} '.format(what_f[0:-1])
                    result2 = '{0} '.format(when_g[0:-1]) + '{0} '.format(where_c[0:-1])+ '{0} '.format(who_d[0:-1])+ '{0} '.format(with_who_e[0:-1])+ '{0} '.format(did_f[0:-1])+ '{0} '.format(what_a[0:-1])
                    result3 = '{0} '.format(when_f[0:-1]) + '{0} '.format(where_a[0:-1])+ '{0} '.format(who_b[0:-1])+ '{0} '.format(with_who_c[0:-1])+ '{0} '.format(did_d[0:-1])+ '{0} '.format(what_e[0:-1])
                    result4 = '{0} '.format(when_e[0:-1]) + '{0} '.format(where_f[0:-1])+ '{0} '.format(who_g[0:-1])+ '{0} '.format(with_who_b[0:-1])+ '{0} '.format(did_g[0:-1])+ '{0} '.format(what_g[0:-1])
                    result5 = '{0} '.format(when_d[0:-1]) + '{0} '.format(where_e[0:-1])+ '{0} '.format(who_f[0:-1])+ '{0} '.format(with_who_a[0:-1])+ '{0} '.format(did_b[0:-1])+ '{0} '.format(what_c[0:-1])
                    result6 = '{0} '.format(when_c[0:-1]) + '{0} '.format(where_d[0:-1])+ '{0} '.format(who_e[0:-1])+ '{0} '.format(with_who_g[0:-1])+ '{0} '.format(did_a[0:-1])+ '{0} '.format(what_b[0:-1])
                    result7 = '{0} '.format(when_b[0:-1]) + '{0} '.format(where_g[0:-1])+ '{0} '.format(who_a[0:-1])+ '{0} '.format(with_who_f[0:-1])+ '{0} '.format(did_c[0:-1])+ '{0} '.format(what_d[0:-1])

                    window1['OUTPUT1'].update(result1)
                    window1['OUTPUT2'].update(result2)
                    window1['OUTPUT3'].update(result3)
                    window1['OUTPUT4'].update(result4)
                    window1['OUTPUT5'].update(result5)
                    window1['OUTPUT6'].update(result6)
                    window1['OUTPUT7'].update(result7)
                elif players == 8 :
                    result1 = '{0} '.format(when_a[0:-1]) + '{0} '.format(where_b[0:-1])+ '{0} '.format(who_c[0:-1])+ '{0} '.format(with_who_d[0:-1])+ '{0} '.format(did_e[0:-1])+ '{0} '.format(what_h[0:-1])
                    result2 = '{0} '.format(when_g[0:-1]) + '{0} '.format(where_c[0:-1])+ '{0} '.format(who_d[0:-1])+ '{0} '.format(with_who_e[0:-1])+ '{0} '.format(did_f[0:-1])+ '{0} '.format(what_a[0:-1])
                    result3 = '{0} '.format(when_f[0:-1]) + '{0} '.format(where_a[0:-1])+ '{0} '.format(who_b[0:-1])+ '{0} '.format(with_who_c[0:-1])+ '{0} '.format(did_h[0:-1])+ '{0} '.format(what_e[0:-1])
                    result4 = '{0} '.format(when_e[0:-1]) + '{0} '.format(where_f[0:-1])+ '{0} '.format(who_g[0:-1])+ '{0} '.format(with_who_b[0:-1])+ '{0} '.format(did_g[0:-1])+ '{0} '.format(what_g[0:-1])
                    result5 = '{0} '.format(when_d[0:-1]) + '{0} '.format(where_e[0:-1])+ '{0} '.format(who_f[0:-1])+ '{0} '.format(with_who_h[0:-1])+ '{0} '.format(did_b[0:-1])+ '{0} '.format(what_c[0:-1])
                    result6 = '{0} '.format(when_c[0:-1]) + '{0} '.format(where_d[0:-1])+ '{0} '.format(who_h[0:-1])+ '{0} '.format(with_who_g[0:-1])+ '{0} '.format(did_a[0:-1])+ '{0} '.format(what_b[0:-1])
                    result7 = '{0} '.format(when_b[0:-1]) + '{0} '.format(where_h[0:-1])+ '{0} '.format(who_a[0:-1])+ '{0} '.format(with_who_f[0:-1])+'{0} '.format (did_c[0:-1])+ '{0} '.format(what_d[0:-1])
                    result8 = '{0} '.format(when_h[0:-1]) + '{0} '.format(where_g[0:-1])+ '{0} '.format(who_e[0:-1])+ '{0} '.format(with_who_a[0:-1])+ '{0} '.format(did_d[0:-1])+ '{0} '.format(what_f[0:-1])

                    window1['OUTPUT1'].update(result1)
                    window1['OUTPUT2'].update(result2)
                    window1['OUTPUT3'].update(result3)
                    window1['OUTPUT4'].update(result4)
                    window1['OUTPUT5'].update(result5)
                    window1['OUTPUT6'].update(result6)
                    window1['OUTPUT7'].update(result7)
                    window1['OUTPUT8'].update(result8)
                elif players == 9 :
                    result1 = '{0} '.format(when_a[0:-1]) + '{0} '.format(where_b[0:-1])+ '{0} '.format(who_c[0:-1])+ '{0} '.format(with_who_d[0:-1])+ '{0} '.format(did_e[0:-1])+ '{0} '.format(what_g[0:-1])
                    result2 = '{0} '.format(when_g[0:-1]) + '{0} '.format(where_c[0:-1])+ '{0} '.format(who_d[0:-1])+ '{0} '.format(with_who_e[0:-1])+ '{0} '.format(did_f[0:-1])+ '{0} '.format(what_a[0:-1])
                    result3 = '{0} '.format(when_f[0:-1]) + '{0} '.format(where_a[0:-1])+ '{0} '.format(who_b[0:-1])+ '{0} '.format(with_who_c[0:-1])+ '{0} '.format(did_h[0:-1])+ '{0} '.format(what_e[0:-1])
                    result4 = '{0} '.format(when_e[0:-1]) + '{0} '.format(where_f[0:-1])+ '{0} '.format(who_g[0:-1])+ '{0} '.format(with_who_b[0:-1])+ '{0} '.format(did_g[0:-1])+ '{0} '.format(what_i[0:-1])
                    result5 = '{0} '.format(when_d[0:-1]) + '{0} '.format(where_e[0:-1])+ '{0} '.format(who_f[0:-1])+ '{0} '.format(with_who_h[0:-1])+ '{0} '.format(did_i[0:-1])+ '{0} '.format(what_c[0:-1])
                    result6 = '{0} '.format(when_c[0:-1]) + '{0} '.format(where_d[0:-1])+ '{0} '.format(who_h[0:-1])+ '{0} '.format(with_who_i[0:-1])+ '{0} '.format(did_a[0:-1])+ '{0} '.format(what_b[0:-1])
                    result7 = '{0} '.format(when_b[0:-1]) + '{0} '.format(where_h[0:-1])+ '{0} '.format(who_i[0:-1])+ '{0} '.format(with_who_f[0:-1])+ '{0} '.format(did_c[0:-1])+ '{0} '.format(what_d[0:-1])
                    result8 = '{0} '.format(when_h[0:-1]) + '{0} '.format(where_i[0:-1])+ '{0} '.format(who_e[0:-1])+ '{0} '.format(with_who_a[0:-1])+ '{0} '.format(did_d[0:-1])+ '{0} '.format(what_f[0:-1])
                    result9 = '{0} '.format(when_i[0:-1]) + '{0} '.format(where_c[0:-1])+ '{0} '.format(who_a[0:-1])+ '{0} '.format(with_who_g[0:-1])+ '{0} '.format(did_b[0:-1])+ '{0} '.format(what_h[0:-1])

                    window1['OUTPUT1'].update(result1)
                    window1['OUTPUT2'].update(result2)
                    window1['OUTPUT3'].update(result3)
                    window1['OUTPUT4'].update(result4)
                    window1['OUTPUT5'].update(result5)
                    window1['OUTPUT6'].update(result6)
                    window1['OUTPUT7'].update(result7)
                    window1['OUTPUT8'].update(result8)
                    window1['OUTPUT9'].update(result9)
                elif players == 10 :
                    result1 = '{0} '.format(when_a[0:-1]) + '{0} '.format(where_b[0:-1])+ '{0} '.format(who_c[0:-1])+ '{0} '.format(with_who_d[0:-1])+ '{0} '.format(did_e[0:-1])+ '{0} '.format(what_g[0:-1])
                    result2 = '{0} '.format(when_g[0:-1]) + '{0} '.format(where_c[0:-1])+ '{0} '.format(who_d[0:-1])+ '{0} '.format(with_who_e[0:-1])+ '{0} '.format(did_f[0:-1])+ '{0} '.format(what_a[0:-1])
                    result3 = '{0} '.format(when_f[0:-1]) + '{0} '.format(where_a[0:-1])+ '{0} '.format(who_b[0:-1])+ '{0} '.format(with_who_c[0:-1])+ '{0} '.format(did_h[0:-1])+ '{0} '.format(what_j[0:-1])
                    result4 = '{0} '.format(when_e[0:-1]) + '{0} '.format(where_f[0:-1])+ '{0} '.format(who_j[0:-1])+ '{0} '.format(with_who_b[0:-1])+ '{0} '.format(did_g[0:-1])+ '{0} '.format(what_i[0:-1])
                    result5 = '{0} '.format(when_d[0:-1]) + '{0} '.format(where_e[0:-1])+ '{0} '.format(who_f[0:-1])+ '{0} '.format(with_who_g[0:-1])+ '{0} '.format(did_j[0:-1])+ '{0} '.format(what_c[0:-1])
                    result6 = '{0} '.format(when_c[0:-1]) + '{0} '.format(where_d[0:-1])+ '{0} '.format(who_h[0:-1])+ '{0} '.format(with_who_i[0:-1])+ '{0} '.format(did_a[0:-1])+ '{0} '.format(what_b[0:-1])
                    result7 = '{0} '.format(when_b[0:-1]) + '{0} '.format(where_h[0:-1])+ '{0} '.format(who_i[0:-1])+ '{0} '.format(with_who_f[0:-1])+ '{0} '.format(did_c[0:-1])+ '{0} '.format(what_d[0:-1])
                    result8 = '{0} '.format(when_h[0:-1]) + '{0} '.format(where_i[0:-1])+ '{0} '.format(who_e[0:-1])+ '{0} '.format(with_who_a[0:-1])+ '{0} '.format(did_d[0:-1])+ '{0} '.format(what_f[0:-1])
                    result9 = '{0} '.format(when_i[0:-1]) + '{0} '.format(where_j[0:-1])+ '{0} '.format(who_a[0:-1])+ '{0} '.format(with_who_c[0:-1])+ '{0} '.format(did_b[0:-1])+ '{0} '.format(what_h[0:-1])
                    result10 = '{0} '.format(when_j[0:-1]) + '{0} '.format(where_c[0:-1])+ '{0} '.format(who_g[0:-1])+ '{0} '.format(with_who_h[0:-1])+ '{0} '.format(did_i[0:-1])+ '{0} '.format(what_e[0:-1])

                    window1['OUTPUT1'].update(result1)
                    window1['OUTPUT2'].update(result2)
                    window1['OUTPUT3'].update(result3)
                    window1['OUTPUT4'].update(result4)
                    window1['OUTPUT5'].update(result5)
                    window1['OUTPUT6'].update(result6)
                    window1['OUTPUT7'].update(result7)
                    window1['OUTPUT8'].update(result8)
                    window1['OUTPUT9'].update(result9)
                    window1['OUTPUT10'].update(result10)
