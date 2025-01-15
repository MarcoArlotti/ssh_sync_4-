class Persona:
    def __init__(self,nome,cognome):
        self._nome = nome
        self._cognome = cognome

    def nome(self):
        return self._nome
    @property
    def nome(self,nome):
        if type(nome) == str:
            self._nome = nome
    
    def cognome(self):
        return self._cognome
    @property
    def cognome(self,cognome):
        if type(cognome) == str:
            self._cognome = cognome


class Allenatore(Persona):
    def __init__(self,nome:str,cognome:str,specializzazione:str):
        super().__init__(nome,cognome)
        self._membro_assegnato = None
        self._specializzazione = specializzazione
        self._scheda_assegnata = None
        self._corsi = []

    def specializzazione(self):
        return self._specializzazione
    @property
    def specializzazione(self,specializzazione):
        if type(specializzazione) == str:
            self._specializzazione = specializzazione
      
class Membro(Persona):
    def __init__(self,nome:str,cognome:str):
        super().__init__(nome,cognome)
        self._allenatore_assegnato = None
        self._corsi_iscritti = []
        self._scheda_allenamento_assegnata = None

    def set_allenatore(self,allenatore):
        self._allenatore_assegnato = allenatore
        allenatore._membro_assegnato = self
    
    def iscrivi_corso(self,corso):
        non_assegnare = False
        for corso_ in self._corsi_iscritti:
            if corso_ == corso:
                non_assegnare = True
        if non_assegnare == False:
            self._corsi_iscritti.append(corso)

    def set_scheda_allenamento(self,scheda):
        self._scheda_allenamento_assegnata = scheda

    @property
    def scheda_allenamento_assegnata(self):
        return self._scheda_allenamento_assegnata
    @scheda_allenamento_assegnata.setter
    def scheda_allenamento_assegnata(self,scheda_allenamento_assegnata_da_assegnare):
        if type(scheda_allenamento_assegnata_da_assegnare) != str and type(scheda_allenamento_assegnata_da_assegnare) != int and type(scheda_allenamento_assegnata_da_assegnare) != bool and type(scheda_allenamento_assegnata_da_assegnare) != float and type(scheda_allenamento_assegnata_da_assegnare) != tuple and type(scheda_allenamento_assegnata_da_assegnare) != list and type(scheda_allenamento_assegnata_da_assegnare) != dict:
            self._scheda_allenamento_assegnata = scheda_allenamento_assegnata_da_assegnare
            
    @property
    def corsi_iscritti(self):
        return self._corsi_iscritti
    @corsi_iscritti.setter
    def corsi_iscritti(self,corsi_iscritti_da_verificare): #TODO controllo se è una classe
        self._corsi_iscritti = corsi_iscritti_da_verificare

class Corso:
    def __init__(self,nome:str,durata:str,allenatore):
        self._nome = nome
        self._durata = durata
        self._allenatore = allenatore

    def nome(self):
        return self._nome
    @property
    def nome(self,nome):
        if type(nome) == str:
            self._nome = nome

    def durata(self):
        return self._durata
    @property
    def durata(self,durata):
        if type(durata) == str:
            self._durata = durata

    def allenatore(self):
        return self._allenatore
    @property
    def allenatore(self,allenatore):
        self._allenatore = allenatore #TODO controllo se è una classe

class SchedaAllenamento:
    def __init__(self,membro,lista_esercizi:list[str]):
        self._membro = membro
        self._lista_esercizi = lista_esercizi

    def lista_esercizi(self):
        return self._lista_esercizi
    @property
    def lista_esercizi(self,lista_esercizi):
        if type(lista_esercizi) == str:
            self._lista_esercizi = lista_esercizi

def main():
    # Creazione degli allenatori
    allenatore1 = Allenatore("Giovanni", "Rossi", "Fitness")
    allenatore2 = Allenatore("Luca", "Bianchi", "Yoga")

    # Creazione dei membri
    membro1 = Membro("Anna", "Verdi")
    membro2 = Membro("Marco", "Neri")

    # Assegnazione degli allenatori ai membri
    membro1.set_allenatore(allenatore1)
    membro2.set_allenatore(allenatore2)

    # Creazione dei corsi
    corso1 = Corso("Pilates", "3 mesi", allenatore1)
    corso2 = Corso("HIIT", "6 mesi", allenatore1)
    corso3 = Corso("Yoga Avanzato", "4 mesi", allenatore2)

    # Iscrizione dei membri ai corsi
    membro1.iscrivi_corso(corso1)
    membro1.iscrivi_corso(corso2)
    membro2.iscrivi_corso(corso3)

    # Creazione delle schede di allenamento
    scheda1 = SchedaAllenamento(membro1, ["Esercizio 1: Squat", "Esercizio 2: Push-up"])
    scheda2 = SchedaAllenamento(membro2, ["Esercizio 1: Plank", "Esercizio 2: Burpee"])

    # Assegnazione delle schede di allenamento ai membri
    membro1.set_scheda_allenamento(scheda1)
    membro2.set_scheda_allenamento(scheda2)

    # Stampa delle informazioni
    print(membro1)
    print(membro2)

if __name__ == "__main__":
    main()