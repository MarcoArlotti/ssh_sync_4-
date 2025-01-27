from datetime import date
class Ristorante:
    def __init__(self,lista_prenotazioni):
        pass

class Prenotazione:
    def __init__(self,prenotazione:str,data:date,quante_persone:int,stato:str):
        self._prenotazione = prenotazione
        self._data = data
        self._quante_persone = quante_persone
        self._stato = stato

