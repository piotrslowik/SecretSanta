"""
    Moduł z klasą User
"""


class User:
    """
    Klasa użytkownika aplikacji, z którego skrzynki Gmail wysyłane będą maile
    """
    def __init__(self, email, password, name):
        """
            Konstruktor klasy User.
            :param email: login
            :param password: hasło
            :param name: podpis
        """
        self.__email = email
        self.__password = password
        self.__name = name

    def set_email(self, email):
        """
            Setter pola email.
            :param email: login
        """
        self.__email = email

    def get_email(self):
        """
            Getter pola email.
        """
        return self.__email

    def set_password(self, pwd):
        """
            Setter pola password.
            :param pwd: hasło
        """
        self.__password = pwd

    def get_password(self):
        """
            Getter pola password.
        """
        return self.__password

    def set_name(self, name):
        """
            Setter pola name.
            :param name: podpis
        """
        self.__name = name

    def get_name(self):
        """
            Getter pola name.
        """
        return self.__name

    def info(self):
        """
            Metoda zwracająca informacje o użytkowniku aplikacji.
        """
        return f'Zalogowano jako {self.get_email()}, podpisano jako {self.get_name()}'
