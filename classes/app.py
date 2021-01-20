"""
    Moduł logiki aplikacji
"""
import csv
import random
import smtplib
import ssl

from classes.player import Player
from classes.user import User


class App:
    """
        Klasa logiki programu stanowiąza warstwę modelu.
    """
    server: smtplib.SMTP_SSL
    user: User

    def __init__(self):
        self.players = []

    def login(self, name, login, pwd):
        """
            Metoda logowania się do konta Gmail.
            :param name: podpis
            :param login: login
            :param pwd: hasło
        """
        try:
            self.__set_user(name, login, pwd)
            self.__connect_to_server()
        except ConnectionRefusedError as error:
            print('ConnectionRefusedError', str(error))
            raise error
        except smtplib.SMTPServerDisconnected as error:
            print('SMTPServerDisconnected', str(error))
            raise error
        except smtplib.SMTPAuthenticationError as error:
            print('SMTPAuthenticationError', str(error))
            raise error
        except smtplib.SMTPException as error:
            print(str(error))
            raise error
        except Exception as error:
            print('SMTPException', str(error))
            raise error

    def __set_user(self, name, login, pwd):
        """
            Metoda przypisująca dane logowania do pola user.
            :param name: podpis
            :param login: login
            :param pwd: hasło
        """
        self.user = User(login, pwd, name)

    def __connect_to_server(self):
        """
            Metoda tworząca połączenie z serwerem poczty Gmail.
        """
        try:
            context = ssl.create_default_context()
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)
            server.ehlo()
            server.login(self.user.get_email(), self.user.get_password())
            self.server = server
        except Exception as error:
            raise error

    def load_players_csv(self, file):
        """
            Metoda wczytująca plik CSV z listą graczy.
            :param file: plik CSV
        """
        try:
            csv_file = open(file, newline='')
            csv_reader = csv.reader(csv_file, delimiter=';', quotechar='|')
            for row in csv_reader:
                self.players.append(Player(row[0], row[1]))
        except FileNotFoundError:
            print('\n ! Nie znaleziono takiego pliku !')
            raise FileNotFoundError('Nie znaleziono takiego pliku.')
        except PermissionError:
            print('\n ! Nie masz uprawnień !')
            raise PermissionError('Nie masz uprawnień.')
        except OSError:
            print('\n ! Nieprawidłowa ścieżka !')
            raise OSError('Nieprawidłowa ścieżka.')
        except IndexError:
            print('\n ! Nieprawidłowy plik !')
            raise IndexError('Nieprawidłowy plik.')

    def execute_emails(self):
        """
            Metoda zarządzająca wysłaniem maili.
        """
        self.__set_targets()
        self.__send_emails()
        self.__close_server()

    def __set_targets(self):
        """
            Metoda ustalająca graczom swoje cele.
        """
        random.shuffle(self.players)
        for i in range(len(self.players) - 1):
            self.players[i].set_target_name(self.players[i + 1].get_name())
        self.players[len(self.players) - 1].set_target_name(self.players[0].get_name())

    def __send_emails(self):
        """
            Metoda wysyłająca maile.
        """
        for player in self.players:
            mail = player.get_email_message(self.user)
            self.server.send_message(mail)

    def __close_server(self):
        """
            Metoda zamykająca połączenie z serwerem poczty Gmail.
        """
        self.server.close()

    def get_players_info(self):
        """
            Metoda zwracająca informacje o graczach.
        """
        return [el.info() for el in self.players]
