class Persona:
    def __init__(self, nome:str ,cognome:str):
        self._nome = nome
        self._cognome = cognome

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self,nome):
        if type(nome) == str:
            self._nome = nome

    @property
    def cognome(self):
        return self._cognome
    @cognome.setter
    def cognome(self,cognome):
        if type(cognome) == str:
            self._cognome = cognome
    
class Studente(Persona):
    def __init__(self, nome:str ,cognome:str):
        super().__init__(nome,cognome)
        self.corsi = []
        self.insegnante = None

    def set_insegnante(self,insegnate_nuovo):
        self.insegnante = insegnate_nuovo
    
    def iscrivi_corso(self,corso):
        self.corsi.append(corso)
        # corso.studenti.append(self)
        print(f"corso.studenti {corso.studenti}")
        corso.studenti.append("test")
        print(f"corso.studenti {corso.studenti}")
        

class Insegnante(Persona):
    def __init__(self,nome,cognome,strumento):
        super().__init__(nome,cognome)
        self._strumento = strumento
        self.studenti = []

    @property
    def strumento(self):
        return self._strumento
    @strumento.setter
    def strumento(self,strumento):
        if type(strumento) == str:
            self._strumento = strumento

class Corso:
    def __init__(self,nome,durata):
        self._durata = durata
        self._nome = nome
        self.studenti = []

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self,nome):
        if type(nome) == str:
            self._nome = nome

    @property
    def durata(self):
        return self._durata
    @durata.setter
    def durata(self,durata):
        if type(durata) == str:
            self._durata = durata



def main():
    # Creazione degli insegnanti
    insegnante1 = Insegnante("Mario", "Rossi", "Pianoforte")
    insegnante2 = Insegnante("Luca", "Bianchi", "Chitarra")

    # Creazione degli studenti
    studente1 = Studente("Anna", "Verdi")
    studente2 = Studente("Marco", "Neri")

    # Assegnazione degli insegnanti agli studenti
    studente1.set_insegnante(insegnante1)
    studente2.set_insegnante(insegnante2)

    # Creazione dei corsi
    corso1 = Corso("Teoria Musicale", "3 mesi")
    corso2 = Corso("Tecnica Pianistica", "6 mesi")

    # Iscrizione degli studenti ai corsi
    studente1.iscrivi_corso(corso1)
    studente1.iscrivi_corso(corso2)
    studente2.iscrivi_corso(corso1)

    # Stampa delle informazioni
    print(studente1.insegnante.nome)
    for s in insegnante1.studenti:
        print(s)

if __name__ == "__main__":
    main()