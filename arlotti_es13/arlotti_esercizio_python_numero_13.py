class Casa:
    def __init__(self, indirizzo:str, proprietario:str):
        self._indirizzo = indirizzo
        self._proprietario = proprietario
        self.stanze = []

    def aggiungi_stanza(self,stanza):
        lista_stanze = self.stanze
        lista_stanze.append(stanza)
        self.stanze = lista_stanze

    @property
    def indirizzo(self):
        return self._indirizzo
    @indirizzo.setter
    def indirizzo(self,indirizzo):
        if type(indirizzo) == str:
            self._indirizzo = indirizzo
    
    @property
    def proprietario(self):
        return self._proprietario
    @proprietario.setter
    def proprietario(self,proprietario):
        if type(proprietario) == str:
            self._proprietario = proprietario

class Stanza:
    def __init__(self, nome:str, superficie:int):
        self._nome = nome
        self._superficie = superficie
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
    
    @property
    def superficie(self):
        return self._superficie
    @superficie.setter
    def superficie(self,superficie):
        if type(self._superficie) == str:
            self._superficie = superficie

# Creazione dell'istanza di Casa
casa = Casa("Via delle Rose 15", "Maria Rossi")

# Creazione delle istanze di Stanza
soggiorno = Stanza("Soggiorno", 30)
cucina = Stanza("Cucina", 15)
camera = Stanza("Camera da Letto", 20)

# Aggiunta delle stanze alla casa
casa.aggiungi_stanza(soggiorno)
casa.aggiungi_stanza(cucina)
casa.aggiungi_stanza(camera)

# Verifica dell'associazione
print(f"Casa di {casa.proprietario} situata in {casa.indirizzo} contiene le seguenti stanze:")
for stanza in casa.stanze:
    print(f"- {stanza.nome} ({stanza.superficie} mq)")

