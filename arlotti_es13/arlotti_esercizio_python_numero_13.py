class Casa:
    def __init__(self, indirizzo:str, propietario:str):
        self._indirizzo = indirizzo
        self._propietario = propietario
        self.lista_stanze = []

    @property
    def indirizzo(self):
        return self.indirizzo
    @indirizzo.setter
    def indirizzo(self,indirizzo):
        if type(indirizzo) == str:
            self.indirizzo = indirizzo
    
    @property
    def propietario(self):
        return self.propietario
    @propietario.setter
    def propietario(self,propietario):
        if type(propietario) == str:
            self.propietario = propietario

class Stanza:
    def __init__(self, nome:str, superficie:int):
        self._nome = nome
        self._superficie = superficie

    @property
    def nome(self):
        return self.nome
    @nome.setter
    def nome(self,nome):
        if type(nome) == str:
            self.nome = nome
    
    @property
    def superficie(self):
        return self.superficie
    @superficie.setter
    def propietario(self,superficie):
        if type(superficie) == str:
            self.superficie = superficie