from domain import Tractor
from repo import Repo
from service import Service
from ui import UI

class App:
    def __init__(self, file_name):
        self.__repo = Repo(file_name)
        self.__service = Service(self.repo)
        self.__ui = UI()
    
    @property
    def repo(self):
        return self.__repo

    @property
    def service(self):
        return self.__service

    @property
    def ui(self):
        return self.__ui
    
    def run(self):
        while True:
            self.ui.show_menu()
            cmd = self.ui.get_command()

            if cmd == "0":
                self.ui.show_exit()
                break
                
            elif cmd == "1":
                _id = self.ui.int_input("ID: ")
                denumire = input("Denumire: ")
                pret = self.ui.int_input("Pret: ")
                model = input("Model: ")
                data = self.ui.date_input("Zi: ", "Luna: ", "An: ")
                zi, luna, an = data.day, data.month, data.year
                self.repo.add_tractor(Tractor(
                    _id,
                    denumire,
                    pret,
                    model,
                    zi,
                    luna,
                    an,
                ))
                self.ui.enter_to_continue("Adaugare completa")

            elif cmd == "2":
                digit = self.ui.digit_input("Cifra: ")
                try:
                    self.service.delete_tractors_with_digit_in_price(digit)
                except ValueError as err:
                    self.ui.enter_to_continue(err)

            elif cmd =="3":
                filter_string = input("Filtru: ")
                filter_price = self.ui.int_input("Pret: ")
                results = self.service.filter_tractors_by_string_and_price(filter_string, filter_price)

                print(f"Filtru: {filter_string}, pret: {filter_price}")
                for result in results:
                    print(result)
    
                self.ui.enter_to_continue()

            elif cmd == "4":
                self.repo.undo()
                self.ui.enter_to_continue("Undo complet")
            
            else:
                self.ui.enter_to_continue("Comanda Invalida")


if __name__ == "__main__":
    app = App("data/tractoare.csv")
    app.run()
