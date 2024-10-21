class Ricetta:
    def __init__(self, nome:str, tempo_preparazione:float, ingredienti:list, difficolta:float):
        self.nome = nome
        self.tempo_preparazione = tempo_preparazione
        self.ingredienti = ingredienti
        self.difficolta = difficolta
        self.disponibile = True
    def tempo_totale_preparazione(self): #stampa il tempo di preparazione di ogni ricetta
    
    def verifica_disponibilita_ingredienti(self):

    def stampa_ricette(self): # prende una lista di ricette e stampa le informazioni di tutte le ricette

    def verifica_ingredienti(self): # prende una lista di ricette e restituisce quelle che possono essere preparate con gli ingredienti disponibili
    

    def get_nome(self):
    
    def set_nome(self):
    
    
    def get_tempo_preparazione(self):
    
    def set_tempo_preparazione(self):
    

    def get_ingredienti(self):
    
    def set_ingredienti(self):
    

    def get_difficolta(self):
    
    def set_difficolta(self):
    

    def get_disponiblie(self):
    
    def set_disponiblie(self):
    

    def aggiungi_ingredienti(self):
        
class Primo(Ricetta):

class secondo(Ricetta):

class dolce(Ricetta):


# Esempio di utilizzo
primo = Primo("Spaghetti alla Carbonara", 20, ["Spaghetti", "Uova", "Pancetta"], "Media", "Spaghetti", "Carbonara")
secondo = Secondo("Bistecca alla Fiorentina", 30, ["Bistecca", "Sale", "Pepe"], "Alta", "Manzo", "Media")
dolce = Dolce("Tiramisù", 30, ["Mascarpone", "Caffè", "Savoiardi"], "Media", 200, "Dessert")

ricette = [primo, secondo, dolce]
ricette_possibili = verifica_ingredienti(ricette, ["Spaghetti", "Uova", "Pancetta", "Bistecca", "Sale", "Pepe", "Mascarpone", "Caffè", "Savoiardi", "Pane", "Pomodoro", "Basilico"])
print(f"Ricette che possono essere preparate: {len(ricette_possibili)}")

print("\nInformazioni sulle ricette:")
stampa_ricette(ricette)