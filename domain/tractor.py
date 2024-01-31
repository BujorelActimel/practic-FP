from datetime import date

class Tractor:
    def __init__(self, ID, denumire, pret, model, zi, luna, an):
        self.__id = ID
        self.__denumire = denumire
        self.__pret = pret
        self.__model = model
        self.__data = date(an, luna, zi)

    def __str__(self):
        return f"{self.ID},{self.denumire},{self.pret},{self.model},{self.data.day}:{self.data.month}:{self.data.year}"
    
    def __repr__(self):
        return str(self)

    @property
    def ID(self):
        return self.__id

    @property
    def denumire(self):
        return self.__denumire

    @property
    def pret(self):
        return self.__pret
    
    @property
    def model(self):
        return self.__model

    @property
    def data(self):
        return self.__data

    @ID.setter
    def ID(self, new_id):
        self.__id = new_id

    @denumire.setter
    def denumire(self, new_denumire):
        self.__denumire = new_denumire

    @pret.setter
    def pret(self, new_pret):
        self.__pret = new_pret

    @model.setter
    def model(self, new_model):
        self.__model = new_model

    @data.setter
    def data(self, new_data):
        self.__data = new_data
