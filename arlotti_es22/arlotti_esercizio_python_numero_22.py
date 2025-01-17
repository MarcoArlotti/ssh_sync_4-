class Automobile:
    def __init__(self,targa:str,modello:str,categoria:str):
        self._targa = targa
        self._modello = modello
        self._categoria = categoria
        self.disponibile = True

class AgenziaNoleggio:
    def __init__(self,lista_auto:list):
        self._lista_auto = lista_auto
    
    def aggiungi_auto(self,Automobile):
        pass

    def noleggia_auto(self,Automobile):
        pass

    def visualizza_auto_disponibili(self):
        pass

    def visualizza_auto_noleggiate(self):
        pass