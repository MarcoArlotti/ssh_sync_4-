import os

class Ricetta:
    def __init__(self, nome:str, tempo_preparazione:float, ingredienti:list, difficolta:float):
        self._nome = nome
        self._tempo_preparazione = tempo_preparazione
        self._ingredienti = ingredienti
        self._difficolta = difficolta
        #self.disponibile = True

    def tempo_totale_preparazione(ricette): #stampa il tempo di preparazione di ogni ricetta
        tempo_totale = 0
        for ricetta in ricette:
            tempo = ricetta.tempo_preparazione
            tempo_totale = tempo_totale + tempo
        return f"PER PREPARARE TUTTE LE RICETTE OCCORRONO {tempo_totale} MINUTI"
    
    def stampa_ricette(ricette): # prende una lista di ricette e stampa le informazioni di tutte le ricette
        for ricetta in ricette:
            print(ricetta)

    #def verifica_disponibilita_ingredienti(self):

    #def verifica_ingredienti(self): # prende una lista di ricette e restituisce quelle che possono essere preparate con gli ingredienti disponibili
    #
    
    def __str__(self):
        return f"{self._nome}; \n\tINGREDIENTI: {self.ingredienti},\n\tTEMPO DI PREPARAZIONE: {self.tempo_preparazione} MINUTI,\n\tDIFFICOLTA': {self.difficolta}."

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,nome):
        if type(nome) == str:
            self._nome = nome
    

    @property
    def tempo_preparazione(self):
        return self._tempo_preparazione

    @tempo_preparazione.setter
    def tempo_preparazione(self,tempo_preparazione):
        if type(tempo_preparazione) == float or type(tempo_preparazione) == int:
            self._tempo_preparazione = tempo_preparazione


    @property
    def ingredienti(self):
        return self._ingredienti

    @ingredienti.setter
    def ingredienti(self,ingredienti):
        if type(ingredienti) == list:
            self._ingredienti = ingredienti
    

    @property
    def difficolta(self):
        return self._difficolta

    @difficolta.setter
    def difficolta(self,difficolta):
        if type(difficolta) == str:
            self._difficolta = difficolta


class Primo(Ricetta):
    def __init__(self, nome:str, tempo_preparazione:float, ingredienti:list, difficolta:float, tipo_pasta:str, sugo:str):
        super().__init__(nome, tempo_preparazione, ingredienti, difficolta)
        self._tipo_pasta = tipo_pasta
        self._sugo = sugo

    def __str__(self):
        return f"{self._nome}; \n\tINGREDIENTI: {self.ingredienti},\n\tTEMPO DI PREPARAZIONE: {self.tempo_preparazione} MINUTI,\n\tDIFFICOLTA': {self.difficolta}\n\tTIPO PASTA: {self.tipo_pasta}\n\tSUGO USATO: {self.sugo}."

    @property
    def tipo_pasta(self):
        return self._tipo_pasta

    @tipo_pasta.setter
    def tipo_pasta(self,tipo_pasta):
        if type(tipo_pasta) == str:
            self._tipo_pasta = tipo_pasta
    

    @property
    def sugo(self):
        return self._sugo

    @sugo.setter
    def sugo(self,sugo):
        if type(sugo) == str:
            self._sugo = sugo

class Secondo(Ricetta):
    def __init__(self, nome:str, tempo_preparazione:float, ingredienti:list, difficolta:float, tipo_carne:str, cottura:str):
        super().__init__(nome, tempo_preparazione, ingredienti, difficolta)
        self._tipo_carne = tipo_carne
        self._cottura = cottura
    def __str__(self):
        return f"{self._nome}; \n\tINGREDIENTI: {self.ingredienti},\n\tTEMPO DI PREPARAZIONE: {self.tempo_preparazione} MINUTI,\n\tDIFFICOLTA': {self.difficolta}\n\tTIPO CARNE: {self.tipo_carne}\n\tCOTTURA: {self.cottura}."

    @property
    def tipo_carne(self):
        return self._tipo_carne

    @tipo_carne.setter
    def tipo_carne(self,tipo_carne):
        if type(tipo_carne) == str:
            self._tipo_carne = tipo_carne
    

    @property
    def cottura(self):
        return self._cottura

    @cottura.setter
    def cottura(self,cottura):
        if type(cottura) == str:
            self._cottura = cottura

class Dolce(Ricetta):
    def __init__(self, nome:str, tempo_preparazione:float, ingredienti:list, difficolta:float, zucchero:float, tipo_dolce:str):
        super().__init__(nome, tempo_preparazione, ingredienti, difficolta)
        self._zucchero = zucchero
        self._tipo_dolce = tipo_dolce
    def __str__(self):
        return f"{self._nome}; \n\tINGREDIENTI: {self.ingredienti},\n\tTEMPO DI PREPARAZIONE: {self.tempo_preparazione} MINUTI,\n\tDIFFICOLTA': {self.difficolta}\n\tQUANTO ZUCCHERO: {self.zucchero}g\n\tTIPO DI DOLCE: {self.tipo_dolce}"
        
    @property
    def zucchero(self):
        return self._zucchero

    @zucchero.setter
    def zucchero(self,zucchero):
        if type(zucchero) == float or type(zucchero) == int:
            self._zucchero = zucchero


    @property
    def tipo_dolce(self):
        return self._tipo_dolce

    @tipo_dolce.setter
    def tipo_dolce(self,tipo_dolce):
        if type(tipo_dolce) == str:
            self._tipo_dolce = tipo_dolce
    
#Esempio di utilizzo
    #primo
primo = Primo("Spaghetti alla Carbonara", 20, ["Spaghetti", "Uova", "Pancetta"], "Media", "Spaghetti", "Carbonara")
os.system("cls")
print(primo)
primo.nome = "fabio alla carbonara"
primo.tempo_preparazione = 9
primo.ingredienti = ["fabio","carbonara","pecorino"]
primo.difficolta = "a prova di fabio"

primo.tipo_pasta = "marangoni"
primo.sugo = "carbofabio"

    #secondo
secondo = Secondo("Bistecca alla Fiorentina", 30, ["Bistecca", "Sale", "Pepe"], "Alta", "Manzo", "Media")
print(secondo)

secondo.nome = "fabio in padella"
secondo.tempo_preparazione = 95
secondo.ingredienti = ["fabio","olio","patate"]
secondo.difficolta = "a prova di fabio"

secondo.tipo_carne = "fabio"
secondo.cottura = "bruciato"

print(primo)
print(secondo)
    #dolce
dolce = Dolce("Tiramisù", 30, ["Mascarpone", "Caffè", "Savoiardi"], "Media", 2.0, "Dessert")
dolce.nome = "marscarponi"
dolce.tempo_preparazione = 23
dolce.ingredienti = ["mascarponi","una diga","acqua"]
dolce.difficolta = "a prova di diga"

dolce.zucchero = 89.0
dolce.tipo_dolce = "dessert"
print(dolce)
    #stampa tutte le ricette con il tempo totale di preparazione
ricette = [primo, secondo, dolce]
print("\nSTAMPA DI TUTTE LE RICETTE;\n")
Ricetta.stampa_ricette(ricette)
print(Ricetta.tempo_totale_preparazione(ricette))
    #verifica ingredienti
#ricette_possibili = verifica_ingredienti(ricette, ["Spaghetti", "Uova", "Pancetta", "Bistecca", "Sale", "Pepe", "Mascarpone", "Caffè", "Savoiardi", "Pane", "Pomodoro", "Basilico"])
#print(f"Ricette che possono essere preparate: {len(ricette_possibili)}")
