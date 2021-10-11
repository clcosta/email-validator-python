import os
import smtplib
from email.message import EmailMessage
from .email_message import MESSAGE

from random import randint

import regex as re


class EmailChecker:
    def email_checker(
        self,
        send_to:str =None,
        sender:str =None,
        sender_password:str =None,
        subject:str =None,
        message:str =MESSAGE,
        name_message:str ='Fulano'
    ):
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = send_to
        check_value = self.__generate_random_number()
        msg.set_content(
            message.format(nome=name_message, codigo=check_value),
            subtype="HTML",
            charset='utf-8'
        )
        self.__send_email(sender, sender_password, msg)
        return check_value

    def __get_domain(self, sender):
        regex = re.compile(r"^.+@(.+)\.[\w]+$")
        domain = regex.findall(sender)[0]
        return domain

    def __generate_random_number(self):
        number = randint(4999, 10000)
        return number

    def __send_email(self, sender, sender_password, msg):
        domain = self.__get_domain(sender)
        if domain == "gmail":
            smtp_port = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        elif domain == "hotmail" or domain == "outlook":
            smtp_port = smtplib.SMTP("smtp-mail.outlook.com", 587)
        else:
            raise ValueError("Domain in email, is not accept value")

        # Login Account
        with smtp_port as smtp:
            smtp.login(sender, sender_password)
            smtp.send_message(msg)
            return