from domain import Tractor
from copy import copy

class Repo:
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__tractoare = self.load_data()
        self.__state = []

    @property
    def file_name(self):
        return self.__file_name

    @property
    def tractoare(self):
        return self.__tractoare

    @property
    def state(self):
        return self.__state

    @tractoare.setter
    def tractoare(self, new_tractoare):
        self.__tractoare = new_tractoare

    @state.setter
    def state(self, new_state):
        self.__state = new_state

    def add_tractor(self, tractor):
        if type(tractor) == Tractor:
            copy_tractoare = [copy(tractor) for tractor in self.tractoare]
            self.state.append(copy_tractoare)
            self.tractoare.append(tractor)
            self.save_data()
            return
        raise ValueError("Not a Tractor")

    def delete_tractor(self, _id):
        for tractor in self.tractoare:
            if tractor.ID == _id:
                self.tractoare.remove(tractor)
                self.save_data()
                return
        raise ValueError("Tractor not found")

    def load_data(self):
        tractoare = []
        with open(self.file_name, "r") as f:
            lines = f.readlines()
            for line in lines[1:]:
                ID, denumire, pret, model, data = line.strip().split(",")
                zi, luna, an = list(map(int, data.split(":")))
                ID = int(ID)
                pret = int(pret)
                tractoare.append(Tractor(ID, denumire, pret, model, zi, luna, an))
        return tractoare
            

    def save_data(self):
        with open(self.file_name, "w") as f:
            f.write("id,denumire,pret,model,data\n")
            for tractor in self.tractoare:
                f.write(str(tractor) + "\n")

    def undo(self):
        try:
            self.tractoare = self.state.pop()
        except:
            pass
        else:
            self.save_data()