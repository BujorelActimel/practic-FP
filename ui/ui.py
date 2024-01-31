import os
from datetime import date

class UI:
    def show_menu(self):
        os.system("cls")
        print("1. Adauga Tractor")
        print("2. Sterge Tractor")
        print("3. Filtrare Tractoare")
        print("4. Undo")
        print("0. Exit")

    def show_exit(self):
        os.system("cls")
        print("La Revedere")

    def enter_to_continue(self, msg=""):
        input(f"{msg}\nApasati Enter pentru a continua\n")

    def get_command(self):
        return input("\n>>> ")

    def int_input(self, msg=""):
        while True:
            try:
                return int(input(msg))
            except ValueError:
                print("Input invalid, incearca sa introduci un numar intreg")

    def date_input(self, msg1="", msg2="", msg3=""):
        while True:
            day = self.int_input(msg1)
            month = self.int_input(msg2)
            year = self.int_input(msg3)
            try:
                return date(year, month, day)
            except ValueError:
                print("Data Invalida")

    def digit_input(self, msg=""):
        while True:
            digit = input(msg)
            try:
                assert digit in [
                    "0",
                    "1", 
                    "2", 
                    "3",
                    "4",
                    "5",
                    "6",
                    "7",
                    "8",
                    "9",
                ]
            except AssertionError:
                print("Input Gresit, incearca sa introduci o cifra")
            else:
                return int(digit)
