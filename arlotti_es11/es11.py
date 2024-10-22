class Ricetta:
    def __init__(self, nome:str, tempo_preparazione:float, ingredienti:list, difficolta:float):
        self.nome = nome
        self.tempo_preparazione = tempo_preparazione
        self.ingredienti = ingredienti
        self.difficolta = difficolta
        #self.disponibile = True
    #def tempo_totale_preparazione(self): #stampa il tempo di preparazione di ogni ricetta
    #
    #def verifica_disponibilita_ingredienti(self):
#
    #def stampa_ricette(self): # prende una lista di ricette e stampa le informazioni di tutte le ricette
#
    #def verifica_ingredienti(self): # prende una lista di ricette e restituisce quelle che possono essere preparate con gli ingredienti disponibili
    #
    #def get_tempo_preparazione(self):
#
    #
    #def set_tempo_preparazione(self):
    
    def __str__(self):
        return self.nome

    def set_nome(self,nome):
        if nome == str:
            self.nome = nome
            return self.nome

    def get_ingredienti(self):
        return self.ingredienti
    #def set_ingredienti(self):
    #
#
    #def get_difficolta(self):
    #
    #def set_difficolta(self):
    #
#
    #def get_disponiblie(self):
    #
    #def set_disponiblie(self):
    #
#
    #def aggiungi_ingredienti(self):
        
class Primo(Ricetta):
    def __init__(self, nome:str, tempo_preparazione:float, ingredienti:list, difficolta:float, tipo_pasta:str, sugo:str):
        super().__init__(nome, tempo_preparazione, ingredienti, difficolta)
        self.tipo_pasta = tipo_pasta
        self.sugo = sugo
    
    #def get_tipo_pasta(self):
    #
    #def set_tipo_pasta(self):


    #def get_sugo(self):
    #
    #def set_sugo(self):


#class secondo(Ricetta):
#    def __init__(self,tipo_carne:str, cottura:str):
#        super.__init__(self, nome:str, tempo_preparazione:float, ingredienti:list, difficolta:float)
#        self.tipo_carne = tipo_carne
#        self.cottura = cottura
    #def get_tipo_carne(self):
    #
    #def set_tipo_carne(self):
    #
    #
    #def get_cottura(self):
    #
    #def set_cottura(self):


#class dolce(Ricetta):
#    def __init__(self,zucchero:float, tipo_dolce:str):
#        super.__init__(self, nome:str, tempo_preparazione:float, ingredienti:list, difficolta:float)
#        self.tipo_carne = tipo_carne
#        self.cottura = cottura

    #def get_zucchero(self):
    #    
    #def set_zucchero(self):
    #
    #
    #def get_tipo_dolce(self):
    #
    #def set_tipo_dolce(self):


# Esempio di utilizzo
primo = Primo("Spaghetti alla Carbonara", 20, ["Spaghetti", "Uova", "Pancetta"], "Media", "Spaghetti", "Carbonara")
print(primo)
#secondo = Secondo("Bistecca alla Fiorentina", 30, ["Bistecca", "Sale", "Pepe"], "Alta", "Manzo", "Media")
#dolce = Dolce("Tiramisù", 30, ["Mascarpone", "Caffè", "Savoiardi"], "Media", 200, "Dessert")
#
#ricette = [primo, secondo, dolce]
#ricette_possibili = verifica_ingredienti(ricette, ["Spaghetti", "Uova", "Pancetta", "Bistecca", "Sale", "Pepe", "Mascarpone", "Caffè", "Savoiardi", "Pane", "Pomodoro", "Basilico"])
#print(f"Ricette che possono essere preparate: {len(ricette_possibili)}")
#
#print("\nInformazioni sulle ricette:")
#stampa_ricette(ricette)