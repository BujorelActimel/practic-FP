from datetime import date
from copy import copy

class Service:
    def __init__(self, repo):
        self.__repo = repo

    @property
    def repo(self):
        return self.__repo

    def delete_tractors_with_digit_in_price(self, digit):
        copy_tractoare = [copy(tractor) for tractor in self.repo.tractoare]
        self.repo.state.append(copy_tractoare)
        for tractor in self.repo.tractoare:
            if str(digit) in str(tractor.pret):                  
                self.repo.delete_tractor(tractor.ID)

    def filter_tractors_by_string_and_price(self, string, price):
        filtered_tractors = []
        for tractor in self.repo.tractoare:
            if string and price > 0:
                if tractor.pret < price and string in tractor.denumire:
                    filtered_tractors.append(tractor)
            elif string:
                if string in tractor.denumire:
                    filtered_tractors.append(tractor)
            elif price > 0:
                if tractor.pret < price:
                    filtered_tractors.append(tractor)
            else:
                filtered_tractors.append(tractor)

        for tractor in filtered_tractors:
            if date.today() > tractor.data:
                tractor.denumire = "*" + tractor.denumire
        
        return filtered_tractors
