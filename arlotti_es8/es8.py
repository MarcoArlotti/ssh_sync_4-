class Piatto:
    def __init__(self,nome: str, prezzo: float,):
        self.nome = nome
        self.prezzo = prezzo
        self.disponibile = True
        

def calcola_conto(piatti_ordinati):
    conto_totale = 0
    for piatto in piatti_ordinati:
        prezzo_portata = piatto.prezzo
        conto_totale = conto_totale + prezzo_portata
    return conto_totale
        
def stampa_menu(piatti_ordinati): #per ogni portata è diversa in testo TODO
    #for piatto in piatti_ordinati:
    #    descrizione = f"{piatto.nome}; {piatto.prezzo}EURO\t {piatto.disponibile}\n"

class Antipasto(Piatto):
    def __init__(self,nome: str, prezzo: float, ingredienti: list, porzione: int):
        super().__init__(nome,prezzo)
        self.ingredienti = ingredienti
        self.porzione = porzione

class Primo(Piatto):
    def __init__(self,nome: str, prezzo: float, tipo_pasta: str, sugo: str):
        super().__init__(nome,prezzo)
        self.tipo_pasta = tipo_pasta
        self.sugo = sugo

class Secondo(Piatto):
    def __init__(self,nome: str, prezzo: float, tipo_carne : str, cottura: str):
        super().__init__(nome,prezzo)
        self.tipo_carne = tipo_carne
        self.cottura = cottura

class Dolce(Piatto):
    def __init__(self,nome: str, prezzo: float, tipo_dolce: str, calorie: float):
        super().__init__(nome,prezzo)
        self.tipo_dolce = tipo_dolce
        self.claorie = calorie
# Esempio di utilizzo
antipasto = Antipasto("Bruschetta", 5.0, ["Pane", "Pomodoro", "Basilico"], "Piccola")
primo = Primo("Spaghetti alla Carbonara", 12.0, "Spaghetti", "Carbonara")
secondo = Secondo("Bistecca alla Fiorentina", 25.0, "Manzo", "Media")
dolce = Dolce("Tiramisù", 6.0, "Tiramisù", 450)

piatti_ordinati = [antipasto, primo, secondo, dolce]
conto_totale = calcola_conto(piatti_ordinati)
print(f"Il conto totale è: {conto_totale}€")  # Output: Il conto totale è: 48.0€

print("\nMenu del Ristorante:")
stampa_menu(piatti_ordinati)