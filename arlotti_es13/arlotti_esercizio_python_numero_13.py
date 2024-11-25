class Studente:
    def __init__(self,nome:str ,matricola:int, corsi:int):
        self._nome = nome
        self._matricola = matricola
        self._corsi = corsi

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self,nome):
        if type(nome) == str:
            self._nome = nome

    @property
    def matricola(self):
        return self._matricola
    @matricola.setter
    def matricola(self,matricola):
        if type(matricola) == str:
            self._matricola = matricola

    @property
    def corsi(self):
        return self._corsi
    @corsi.setter
    def corsi(self,corsi):
        if type(corsi) == str:
            self._corsi = corsi
            
class Corso:
    def __init__(self,titolo,codice):
        self.titolo = titolo
        self.codice = codice

    @property
    def titolo(self):
        return self._titolo
    @titolo.setter
    def titolo(self,titolo):
        if type(titolo) == str:
            self._titolo = titolo

    @property
    def codice(self):
        return self._codice
    @codice.setter
    def codice(self,codice):
        if type(codice) == str:
            self._codice = codice
            
