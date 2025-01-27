class Veicolo:
    def __init__(self,marca,modello,carburante):
        self._marca = marca
        self._modello = modello
        self._carburante = carburante

    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self,nuova_marca):
        if type(nuova_marca) == str:
            self._marca = nuova_marca

    @property
    def modello(self):
        return self._modello
    @modello.setter
    def modello(self,nuova_modello):
        if type(nuova_modello) == str:
            self._modello = nuova_modello

    @property
    def carburante(self):
        return self._carburante
    @carburante.setter
    def carburante(self,nuova_carburante):
        if type(nuova_carburante) == str:
            self._carburante = nuova_carburante

class Auto(Veicolo):
    def __init__(self, marca, modello, carburante):
        super().__init__(marca, modello, carburante)
    #grande utilità una classe vuota

class Camion(Veicolo):
    def __init__(self, marca, modello, carburante):
        super().__init__(marca, modello, carburante)
    #grande utilità una classe vuota

class Flotta:
    def __init__(self,lista_veicoli):
        self._lista_veicoli = lista_veicoli
    
    @property
    def lista_veicoli(self):
        return self._lista_veicoli
    @lista_veicoli.setter
    def carburante(self,nuova_lista_veicoli):
        if type(nuova_lista_veicoli) == str:
            self._lista_veicoli = nuova_lista_veicoli

    def aggiungi_veicolo(self,Veicolo):
        if type(Veicolo) != str and type(Veicolo) != int and type(Veicolo) != float and type(Veicolo) != bool and type(Veicolo) != tuple:
            self._lista_veicoli.append(Veicolo)
    def stampa_tutti_veicoli(self):
        for veicolo in self._lista_veicoli:
            print(f"MARCA:{veicolo._marca}, MODELLO:{veicolo._modello}, CARBURANTE:{veicolo._carburante}")