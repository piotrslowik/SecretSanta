"""
    Główny moduł aplikacji
"""
import smtplib

from classes.app import App
from classes.gui import Gui


class ViewModel:
    """
        Klasa główna programu łącząca logikę klasy App z widokiem klasy Gui.
    """
    def __init__(self):
        self.app = App()
        self.gui = Gui()

    def run(self):
        """
            Metoda uruchamiająca program.
        """
        self.__login()
        self.gui.run()

    def info(self):
        """
            Metoda wyświetlająca informacje o aplikacji.
        """
        self.gui.info('Program SecretSanta służy do automatyzacji '
                      'zabawy w tajemniczego Świętego Mikołaja.')

    def __login(self):
        """
            Metoda dodająca do GUI przycisk logowania z odpowiednią akcją.
        """
        self.gui.add_login_button(self.__handle_login)

    def __handle_login(self):
        """
            Metoda łącząca się z pocztą Gmail i aktualizująca GUI po zalogowaniu.
        """
        try:
            self.app.login(self.gui.name, self.gui.login, self.gui.pwd)
            self.gui.delete_login_widgets()
            self.gui.add_user_info(self.app.user)
            self.gui.add_file_button(self.__handle_csv)
        except ConnectionRefusedError:
            self.gui.error('Nie udało się połączyć z serwerem poczty.')
        except smtplib.SMTPServerDisconnected:
            self.gui.error('Nieprawidłowy login lub hasło')
        except smtplib.SMTPAuthenticationError:
            self.gui.error('Nie udało się zalogować.\n'
                           'Być może nie został włączony "Dostęp mniej bezpiecznych aplikacji"')
        except smtplib.SMTPException:
            self.gui.error('Nie udało się zalogować.\n'
                           'Być może nie został włączony "Dostęp mniej bezpiecznych aplikacji"')
        except Exception as error:
            self.gui.error('Nieznany błąd:\n' + str(error))

    def __handle_csv(self):
        """
            Metoda wczytująca plik CSV z uczestnikami i aktualizująca GUI.
        """
        try:
            file = self.gui.ask_file()
            self.app.load_players_csv(file)
            self.gui.delete_file_button()
            self.gui.add_players_list(self.app.get_players_info())
            self.gui.add_execute_button(self.__handle_execution)
        except FileNotFoundError as error:
            self.gui.error(str(error))
        except PermissionError as error:
            self.gui.error(str(error))
        except OSError as error:
            self.gui.error(str(error))
        except IndexError as error:
            self.gui.error(str(error))

    def __handle_execution(self):
        """
            Metoda wysyłająca maile i aktualizująca GUI.
        """
        self.app.execute_emails()
        self.gui.finish()


if __name__ == '__main__':
    program = ViewModel()
    program.run()
