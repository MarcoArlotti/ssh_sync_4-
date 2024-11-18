class Casa:
    def __init__(self, indirizzo:str, proprietario:str):
        self._indirizzo = indirizzo
        self._proprietario = proprietario
        self.stanze = []

    #def aggiungi_stanza(self,stanza):
    #    self.stanze.append(stanza)
#
    @property
    def indirizzo(self):
        return self.indirizzo
    @indirizzo.setter
    def indirizzo(self,indirizzo):
        if type(indirizzo) == str:
            self.indirizzo = indirizzo
    
    @property
    def proprietario(self):
        return self.proprietario
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
        return self.nome
    @nome.setter
    def nome(self,nome):
        if type(nome) == str:
            self.nome = nome
    
    @property
    def superficie(self):
        return self.superficie
    @superficie.setter
    def proprietario(self,superficie):
        if type(superficie) == str:
            self.superficie = superficie

# Creazione dell'istanza di Casa
casa = Casa("Via delle Rose 15", "Maria Rossi")

# Creazione delle istanze di Stanza
soggiorno = Stanza("Soggiorno", 30)
cucina = Stanza("Cucina", 15)
camera = Stanza("Camera da Letto", 20)

# Aggiunta delle stanze alla casa
#casa.aggiungi_stanza(soggiorno)
#casa.aggiungi_stanza(cucina)
#casa.aggiungi_stanza(camera)

# Verifica dell'associazione, TODO ERRORE SELF.PROPRIETARIO 
print(f"Casa di {casa.proprietario} situata in {casa.indirizzo} contiene le seguenti stanze:")
for stanza in casa.stanze:
    print(f"- {stanza.nome} ({stanza.superficie} mq)")