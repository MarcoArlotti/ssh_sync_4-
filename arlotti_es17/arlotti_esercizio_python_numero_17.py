class Insegnanti:
    def __init__(self,nome,cognome,strumento_musicale):
        self._nome = nome
        self._cognome = cognome
        self._strumento_musicale = strumento_musicale
    def

class Studenti(Insegnanti):
    def __init__(self,nome,cognome):
        super().__init__(nome,cognome)
        self._lista_corsi = []
    

class Corsi(Insegnanti):
    def __init__(self,nome,durata):
        super().__init__(nome)
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
    print(studente1)
    print(studente2)

if __name__ == "__main__":
    main()