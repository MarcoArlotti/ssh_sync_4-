from datetime import date
class Album:
    def __init__(self,titolo:str,descrizzione:str,autore,lista_foto:list):
        self._titolo = titolo
        self._descrizzione = descrizzione
        self._autore = autore
        self._lista_foto = lista_foto

class Utente:
    def __init__(self,profilo:tuple):
        self._profilo = profilo
        self._lista_seguiti = []
        self._album_creati = []
        self._lista_foto = []

    def carica_foto(self,Foto):
        if type(Foto) != str and type(Foto) != int and type(Foto) != float and type(Foto) != bool and type(Foto) != tuple:
            self._lista_foto.append(Foto)
        else:
            raise ValueError("ERRORE CARICA_FOTO")
        
    def segui_utente(self,Utente):
        if type(Utente) != str and type(Utente) != int and type(Utente) != float and type(Utente) != bool and type(Utente) != tuple:
            self._lista_seguiti.append(Utente)
        else:
            raise ValueError("ERRORE SEGUI_UTENTE")
        
class Foto:
    def __init__(self,id:str,titolo:str,descrizione:str,quando_creata:date,autore:Utente,a_che_album_appartiene:Album):
        self._id = id
        self._titolo = titolo
        self._descrizione = descrizione
        self._quando_creata = quando_creata
        self._autore = autore
        self._a_che_album_appartiene = a_che_album_appartiene
class Album:
    def __init__(self,titolo:str,descrizione:str,autore:Utente,lista_foto:list):
        self._titolo = titolo
        self._descrizione = descrizione
        self._autore = autore
        self._lista_foto = lista_foto
class Commento:
    def __init__(self,chi_lo_ha_postato:Utente,dove_e_stato_postato:Foto):
        self._chi_lo_ha_postato = chi_lo_ha_postato
        self._dove_e_stato_postato = dove_e_stato_postato

