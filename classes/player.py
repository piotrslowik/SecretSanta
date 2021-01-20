"""
    Moduł z klasą Player
"""
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from classes.user import User


class Player:
    """
    Klasa uczestnika zabawy. Posiada pola jego imienia, adresu e-mail
    oraz "celu" dla którego będzie Tajemniczym Mikołajem
    """
    def __init__(self, name, email):
        """
            Konstruktor klasy Player.
            :param name: imię zawodnika
            :param email: email zawodnika
        """
        self.__name = name
        self.__email = email
        self.__target_name = ''

    def set_name(self, name):
        """
            Setter pola name.
            :param name: imię zawodnika
        """
        self.__name = name

    def get_name(self):
        """
            Getter pola name.
        """
        return self.__name

    def set_email(self, email):
        """
            Setter pola name.
            :param email: email zawodnika
        """
        self.__email = email

    def get_email(self):
        """
            Getter pola email.
        """
        return self.__email

    def set_target_name(self, target):
        """
            Setter pola target_name.
            :param target: imię celu zawodnika
        """
        self.__target_name = target

    def get_target_name(self):
        """
            Getter pola target_name.
        """
        return self.__target_name

    def info(self):
        """
            Metoda zwracająca informacje o zawodniku.
        """
        return f'{self.__name} <{self.__email}>'

    def get_email_message(self, user: User):
        """
            Metoda zwracająca treść wiadomości, która zostanie wysłana do zawodnika.
            :param user: obiekt użytkownika aplikacji
        """
        sender = f'{user.get_name()} <{user.get_email()}>'
        receiver = f'{self.get_name()} <{self.get_email()}>'
        subject = 'Dla kogo Ty będziesz Mikołajem?'
        text = f"""\
        Cześć!

        Mam nadzieję, że spodoba ci się zabawa w Sekretnego Mikołaja.
        Będziesz Mikołajem dla {self.get_target_name()}.

        Życzę wielu super prezentów!
        """
        html = f"""\
        <html>
            <head>
                <meta charset="utf-8" />
                <link href='https://fonts.googleapis.com/css?family=Charmonman' rel='stylesheet'>
            </head>
            <body style="font-family: Arial, sans-serif;
                        font-size: 1.5em;
                        text-align: center;
                        background: beige;
                        color: darkred
            ">
            <p style="font-family: Charmonman; font-size: 2em">
            Cześć!
            </p>
            <p>
                Mam nadzieję, że spodoba ci się zabawa w Sekretnego Mikołaja.<br />
                Będziesz Mikołajem dla <span style="font-weight: bold">{self.get_target_name()}</span>.
            </p>
            <p>
                Życzę wielu super prezentów!
            </p>
          </body>
        </html>
        """

        text_content = MIMEText(text, 'plain')
        html_content = MIMEText(html, 'html')

        message = MIMEMultipart('alternative')
        message.attach(text_content)
        message.attach(html_content)
        message['From'] = sender
        message['To'] = receiver
        message['Subject'] = subject

        return message
