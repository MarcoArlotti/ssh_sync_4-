class Frazione:
    def __init__(self,numeratore,denominatore):
        self.numeratore = numeratore
        self.denominatore = denominatore

    def __add__(self,numeri): #fare che se la parte sotto della frazione è diversa, fà un MCM e lo calcola
        if denominatore
        return Frazione(self.numeratore + numeri.numeratore, self.denominatore)
    def __sub__(self,numeri):
        return Frazione(self.numeratore - numeri.numeratore, self.denominatore)
    def __mul__(self,numeri):
        return Frazione(self.numeratore * numeri.numeratore, self.denominatore * numeri.denominatore)
    def __repr__(self):
        return f"risultati della frazione ({self.numeratore}, {self.denominatore})"
# Esempio di utilizzo
f1 = Frazione(2, 2)
f2 = Frazione(3, 4)

# Addizione
f3 = f1 + f2
print(f3)  # Output: Frazione(5, 4)

# Sottrazione
f4 = f1 - f2
print(f4)  # Output: Frazione(-1, 4)

# Moltiplicazione
f5 = f1 * f2
print(f5)  # Output: Frazione(3, 8)

# Rappresentazione
print(f1)  # Output: Frazione(1, 2)