"""
    Moduł interfejsu graficznego aplikacji
"""
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from classes.user import User


class Gui:
    """
        Klasa interfejsu graficznego aplikacji stanowiąca warstwę widoku.
    """
    root: tk.Tk
    font = {
        'title': ('Oswald', 34),
        'subtitle': ('Arial', 14),
        'text': ('Arial', 11),
    }
    __name: tk.Entry
    __login: tk.Entry
    __pwd: tk.Entry

    def __init__(self):
        self.__init_container()
        self.__init_title()
        self.__init_login()

    def __init_container(self):
        """
            Metoda inicjująca GUI.
        """
        root = tk.Tk()
        root.configure(bg='white')
        root.geometry('1000x600')
        root.resizable(False,False)
        root.title('Secret Santa')
        root.columnconfigure((0, 1, 2, 3, 4, 5), pad=3)
        root.rowconfigure((0, 1, 2, 3, 4), pad=3)
        self.root = root

    def __init_title(self):
        """
            Metoda dodająca informacje o programie.
        """
        textbox = tk.Text(self.root, width=124, height=8)
        textbox.grid(column=0, row=0, columnspan=6, sticky='WE')
        textbox.insert(tk.END, 'Secret Santa', 'h1')
        textbox.insert(tk.END, '\n')
        textbox.insert(tk.END, 'Program ten sam wylosuje graczom osoby, dla których będą '
                               'Tajemniczym Mikołajem.\n'
                               'Wyśle też do nich odpowiednie maile.', 'p')
        textbox.tag_config('h1', foreground='darkred', font=self.font['title'])
        textbox.tag_config('p', foreground='darkblue', font=self.font['subtitle'])
        textbox.tag_configure('center', justify='center')
        textbox.tag_add('center', 1.0, 'end')

    def __init_login(self):
        """
            Metoda dodająca elementy GUI odpowiedzialne za logowanie.
        """
        self.__login_info()
        self.__name_input()
        self.__login_input()
        self.__pwd_input()

    def delete_login_widgets(self):
        """
            Metoda usuwająca elementy GUI odpowiedzialne za logowanie.
        """
        for i in [1, 2, 3]:
            for widget in self.root.grid_slaves(i):
                widget.destroy()

    def __login_info(self):
        """
            Metoda dodająca informacje dotyczące logowania do poczty Gmail.
        """
        textbox = tk.Text(self.root, height=2)
        textbox.insert(tk.END, 'Do poprawnego działania należy ustawić dostęp do mniej '
                               'bezpiecznych aplikacji w ustawieniach konta google.', 'p')
        textbox.tag_config('p', foreground='black', font=self.font['text'])
        textbox.tag_configure('center', justify='center')
        textbox.tag_add('center', 1.0, 'end')
        textbox.grid(column=0, row=1, columnspan=6, sticky='WE')

    def __name_input(self):
        """
            Metoda dodająca input z imieniem (podpisem).
        """
        label = tk.Label(self.root, text='Twoje imię (podpis)', font=self.font['text'],
                         anchor='e', bg='white')
        label.grid(column=0, row=2, sticky='WE', ipady=5, ipadx=8)
        name_input = tk.Entry(self.root, exportselection=0, font=self.font['text'])
        name_input.grid(column=1, row=2, sticky='WE', ipady=5, ipadx=8)
        self.name = name_input

    @property
    def name(self):
        """Imię użytkownika - getter"""
        return self.__name.get()

    @name.setter
    def name(self, new):
        """
            Imię użytkownika - setter
            :param new: imię
        """
        self.__name = new

    def __login_input(self):
        """
            Metoda dodająca input z loginem gmail.
        """
        label = tk.Label(self.root, text='Adres Gmail', font=self.font['text'],
                         anchor='e', bg='white')
        label.grid(column=2, row=2, sticky='WE', ipady=5, ipadx=8)
        login_input = tk.Entry(self.root, exportselection=0, font=self.font['text'])
        login_input.grid(column=3, row=2, sticky='WE', ipady=5, ipadx=8)
        self.login = login_input

    @property
    def login(self):
        """Login użytkownika - getter"""
        return self.__login.get()

    @login.setter
    def login(self, new):
        """
            Login użytkownika - setter
            :param new: login
        """
        self.__login = new

    def __pwd_input(self):
        """
            Metoda dodająca input z hasłem.
        """
        label = tk.Label(self.root, text='Hasło', font=self.font['text'],
                         anchor='e', bg='white')
        label.grid(column=4, row=2, sticky='WE', ipady=5, ipadx=8)
        pwd_input = tk.Entry(self.root, exportselection=0, show="*",
                             font=self.font['text'])
        pwd_input.grid(column=5, row=2, sticky='WE', ipady=5, ipadx=8)
        self.pwd = pwd_input

    @property
    def pwd(self):
        """Hasło użytkownika - getter"""
        return self.__pwd.get()

    @pwd.setter
    def pwd(self, new):
        """
            Hasło użytkownika - setter
            :param new: hasło
        """
        self.__pwd = new

    def add_login_button(self, onclick):
        """
            Metoda dodająca do widoku przycisk logowania.
            :param onclick: funkcja wywoływana przyciśnięciem przycisku
        """
        btn = tk.Button(self.root, text='Zaloguj', font=('Arial', 12, 'bold'),
                        bg='darkblue', fg='white',
                        bd=0, cursor='hand2', command=onclick)
        btn.grid(column=2, columnspan=2, row=3, ipady=8, ipadx=40, pady=12)

    def add_user_info(self, user: User):
        """
            Metoda dodająca informacje o zalogowanym użytkowniku.
            :param user: obiekt użytkownika
        """
        text = f'Zalogowano jako {user.get_email()} ({user.get_name()})'
        label = tk.Label(self.root, text=text, font=self.font['text'], bg='white')
        label.grid(column=0, columnspan=6, row=1, sticky='WE', ipady=5, ipadx=8)

    def add_file_button(self, onclick):
        """
            Metoda dodająca do widoku przycisk wyboru pliku CSV.
            :param onclick: funkcja wywoływana przyciśnięciem przycisku
        """
        file_btn = tk.Button(self.root, text='Wczytaj listę graczy z pliku .csv',
                             cursor='hand2', bd=0, font=('Arial', 12, 'bold'),
                             bg='darkblue', fg='white', command=onclick)
        file_btn.grid(column=2, columnspan=2, row=2, ipady=8, ipadx=40, pady=12)

        def info_function():
            """
                Funkcja wyświetlająca okno z informacjami o programie.
            """
            info = 'Plik .csv musi składać się z dwóch kolumn - imię uczestnika i jego ' \
                   'adres e-mail.\n' \
                   'Oczywiście może to być imię i nazwisko, pseudonim, cokolwiek. ' \
                   'Będzie to po prostu nazwa adresata.\n' \
                   'Kolumny mają być oddzielone średnikiem, a rekordy znakiem nowej ' \
                   'linii, np.:\n' \
                   'Jan Kowalski;jan.kowalski@gmail.com\n' \
                   'Ania Nowak;ania_nowak@wp.pl\n' \
                   'Seba;sebix@onet.pl'
            Gui.info(info)
        info_btn = tk.Button(self.root, text='Pomoc', bd=0, font=('Arial', 12, 'bold'),
                             bg='blue', fg='white',
                             cursor='hand2', command=info_function)
        info_btn.grid(column=4, row=2, ipady=8, ipadx=10, pady=12)

    def delete_file_button(self):
        """
            Metoda usuwająca przycisk wczytania pliku CSV.
        """
        for widget in self.root.grid_slaves(2):
            widget.destroy()

    @staticmethod
    def ask_file():
        """
            Metoda statyczna wyświetlająca okno dialogowe wyboru pliku CSV.
        """
        return filedialog.askopenfilename(title='Plik .csv z listą uczestników',
                                          filetypes=[('Plik .csv', ['.csv'])])

    def add_players_list(self, players):
        """
            Metoda dodająca listę uczestników.
            :param players: lista uczestników
        """
        text_area = scrolledtext.ScrolledText(self.root, font=self.font['text'], height=20)
        text_area.grid(column=1, columnspan=4, pady=10, padx=10)
        text_area.insert(tk.INSERT, '\n'.join(players))

    def add_execute_button(self, onclick):
        """
            Metoda dodająca do widoku przycisk wysłania wiadomości e-mail
            :param onclick: funkcja wywoływana przyciśnięciem przycisku
        """
        file_btn = tk.Button(self.root, text='Wyślij maile do graczy', bd=0,
                             font=('Arial', 12, 'bold'), bg='darkblue',
                             fg='white', cursor='hand2', command=onclick)
        file_btn.grid(column=2, columnspan=2, ipady=8, ipadx=40, pady=12)

    def __delete_execute_button(self):
        """
            Metoda usuwająca przycisk wysyłania wiadomości.
        """
        for widget in self.root.grid_slaves(3):
            widget.destroy()

    def __add_finish_label(self):
        """
            Metoda dodająca pole tekstowe z informacją o wysłaniu wiadomości.
        """
        label = tk.Label(self.root, text='Wiadomości zostały wysłane',
                         font=self.font['subtitle'], bg='white')
        label.grid(column=2, columnspan=2, ipady=8, ipadx=40, pady=12)

    def finish(self):
        """
            Metoda zastępująca przycisk wysyłania informacją o wysłaniu maili.
        """
        self.__delete_execute_button()
        self.__add_finish_label()

    @staticmethod
    def error(msg):
        """
            Metoda wyświetlająca okienko z błędem.
            :param msg: wyświetlany w okienku tekst
        """
        messagebox.showerror(title='Błąd', message=msg)

    @staticmethod
    def info(msg, title='Secret Santa'):
        """
            Metoda wyświetlająca okienko z informacją.
            :param msg: wyświetlany w okienku tekst
            :param title: tytuł okienka
        """
        messagebox.showinfo(title=title, message=msg)

    def run(self):
        """
            Metoda uruchamiająca GUI.
        """
        self.root.mainloop()
