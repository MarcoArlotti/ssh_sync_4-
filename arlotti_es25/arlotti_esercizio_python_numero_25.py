from datetime import date

class Ristorante:
    def __init__(self,lista_prenotazioni):
        self._lista_prenotazioni = lista_prenotazioni
    
    @property
    def lista_prenotazioni(self):
        return self._lista_prenotazioni
    @lista_prenotazioni.setter
    def lista_prenotazioni(self,lista_prenotazioni):
        if type(lista_prenotazioni) == str:
            self._lista_prenotazioni = lista_prenotazioni

    def aggiungi_prenotazione(self,Prenotazione):
        self._lista_prenotazioni.append(Prenotazione)

    def cerca_prenotazione(self,Prenotazione):
        for prenotazione in self._lista_prenotazioni:
            if prenotazione._stato == Prenotazione._stato and prenotazione._quante_persone == Prenotazione._quante_persone and prenotazione._data == Prenotazione._data:
                return True
        else:
            return False

class Prenotazione:
    def __init__(self,prenotazione:str,data:date,quante_persone:int,stato:str):
        self._prenotazione = prenotazione
        self._data = data
        self._quante_persone = quante_persone
        self._stato = stato

    @property
    def prenotazione(self):
        return self._prenotazione
    @prenotazione.setter
    def prenotazione(self,prenotazione):
        if type(prenotazione) == str:
            self._prenotazione = prenotazione
    
    @property
    def data(self):
        return self._data
    @data.setter
    def data(self,data):
        if type(data) != None:
            self._data = data
    
    @property
    def quante_persone(self):
        return self._quante_persone
    @quante_persone.setter
    def quante_persone(self,quante_persone):
        if type(quante_persone) == int:
            self._quante_persone = quante_persone
    
    @property
    def stato(self):
        return self._stato
    @stato.setter
    def stato(self,stato):
        if type(stato) == str:
            self._stato = stato

def main():
    data = 20
    ristorante = Ristorante([])

    prenotaz1 = Prenotazione("fabio",data,3,"bho")
    prenotaz2 = Prenotazione("gianni",data,6,"bho")
    prenotaz3 = Prenotazione("pontos",data,7,"bho")
    prenotaz4 = Prenotazione("maro",data,2,"bho")

    ristorante.aggiungi_prenotazione(prenotaz1)
    ristorante.aggiungi_prenotazione(prenotaz2)
    ristorante.aggiungi_prenotazione(prenotaz3)
    ristorante.aggiungi_prenotazione(prenotaz4)

    print(ristorante.cerca_prenotazione(prenotaz4))
main()