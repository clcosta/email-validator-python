from PySimpleGUI import PySimpleGUI as sg

from utils import *

class EmailCheckerGui:

    THEME = 'Reddit'

    mail = EmailChecker()

    def __init__(self, sender, sender_password, subject):
        janela1, janela2 = self.__initial_window(),None
        # Event Loop
        while True:
            window, events, values = sg.read_all_windows()
            ## Evento de fechar as janelas
            if window == janela1 and events == sg.WINDOW_CLOSED: break
            if window == janela2 and events == sg.WINDOW_CLOSED: break
            ## Evento de abrir a janela de verificar codigo e fechar a de email
            if window == janela1 and events == 'Verificar':
                if values['email'] != '' and values['nome'] != '':
                    checkin_email = values['email']
                    checkin_name = values['nome']
                    janela2 = self.__checker_window()
                    janela1.hide()
                    window.Refresh()
                    check_value = self.mail.email_checker(
                        send_to=checkin_email,
                        sender=sender,
                        sender_password=sender_password,
                        subject=subject,
                        name_message=checkin_name
                    )
            ## Evento de verificar o código enviado do e-mail
            if window == janela2 and events == 'Verificar':
                user_input = values['codigo']
                
                checked = self.__verify_check(user_input, check_value, window)
                
                if checked:
                    sg.popup(
                        f'E-mail {checkin_email} confirmado!'
                    )
                    window['error'].update('Sucesso!')

    def __verify_check(self,user_value, check_value, window):
            if user_value == str(check_value):
                return True
            else:
                window['error'].update("Código invalido!")
                return False


    def __initial_window(self):
        sg.theme(self.THEME)
        layout = [
            [sg.Text("Nome"), sg.Input(key='nome')],
            [sg.Text("E-mail"), sg.Input(key='email')],
            [sg.Button('Verificar')]
        ]
        return sg.Window('E-mail Verify', layout=layout, finalize=True)

    def __checker_window(self):
        sg.theme(self.THEME)
        layout = [
            [sg.Text('Código de verificação'), sg.Input(key='codigo')],
            [sg.Text("", justification='c', key='error')],
            [sg.Button('Verificar')]
        ]
        return sg.Window('E-mail checker', layout=layout, finalize=True)
