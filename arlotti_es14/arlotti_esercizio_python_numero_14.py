class Studente:
    def __init__(self, nome:str, matricola:str):
        self._nome = nome
        self._matricola = matricola
        self.corsi = [] #corsi che questo studente è iscritto

    def aggiungi_corso(self,corso):
        #if type(corso) == "<class '__main__.Corso": #verifica se il corso inserito  è una classe
        lista_corsi_in_Studente = self.corsi
        lista_corsi_in_Studente.append(corso)
        self.corsi = lista_corsi_in_Studente
        lista_studenti_in_Corso = corso.studenti
        lista_studenti_in_Corso.append(self)
        corso._studenti = lista_studenti_in_Corso
    
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

class Corso:
    def __init__(self, titolo:str, codice:str):
        self._titolo = titolo
        self._codice = codice
        self.studenti = [] #studenti che sono iscritti a questo corso

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



# Creazione delle istanze di Studente
studente1 = Studente("Alice Rossi", "MAT123")
studente2 = Studente("Marco Bianchi", "MAT456")

# Creazione delle istanze di Corso
corso1 = Corso("Programmazione Python", "PY101")
corso2 = Corso("Database Relazionali", "DB201")
corso3 = Corso("Sistemi Operativi", "SO301")

# Associazione tra studenti e corsi
studente1.aggiungi_corso(corso1)
studente1.aggiungi_corso(corso2)
studente2.aggiungi_corso(corso2)
studente2.aggiungi_corso(corso3)

# Verifica delle associazioni
print(f"{studente1.nome} è iscritto ai seguenti corsi:")
for corso in studente1.corsi:
    print(f"- {corso.titolo} ({corso.codice})")

print(f"\n{corso2.titolo} ha i seguenti studenti iscritti:")
for studente in corso2.studenti:
    print(f"- {studente.nome} ({studente.matricola})")