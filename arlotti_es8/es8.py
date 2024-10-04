class Piatto:
    def __init__(nome: str, prezzo: float, disponibile: bool):
        self.nome = nome
        self.prezzo = prezzo
        self.disponibile = True

    def ordina(self):
        self.disponibile = False
        disponi = True #?????????????


class Antipasto(Piatto):
    def __init__(nome: str, prezzo: float, disponibile: bool, ingredienti: list, porzione: int):
        super().__init__(prezzo, disponibile)
        self.ingredienti = ingredienti
        self.porzione = porzione

class Primo(Piatto):
    def __init__(nome: str, prezzo: float, disponibile: bool, tipo_pasta: str, sugo: str):
        super().__init__(prezzo, disponibile)
        self.tipo_pasta = tipo_pasta
        self.sugo = sugo

class Secondo(Piatto):
    def __init__(nome: str, prezzo: float, disponibile: bool, tipo_carne : str, cottura: str):
        super().__init__(prezzo, disponibile)
        self.tipo_carne = tipo_carne
        self.cottura = cottura

class Dolce(Piatto):
    def __init__(nome: str, prezzo: float, disponibile: bool, tipo_dolce: str, calorie: float):
        super().__init__(prezzo, disponibile)
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