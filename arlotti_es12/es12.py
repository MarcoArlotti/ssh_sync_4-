class Auto:
    def __init__(self, marca:str, modello:str):
        self._marca = marca
        self._modello = modello
        self.motore = None

    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self,marca):
        if type(marca) == str:
            self._marca = marca

    @property
    def modello(self):
        return self._modello
    @modello.setter
    def modello(self,modello):
        if type(modello) == str:
            self._modello = modello

    def associa_motore(self,motore):
        motore_nell_auto = self.motore
        if motore_nell_auto != None:
            motore_nell_auto.auto = None

        self.motore = motore
        motore.auto = self

        
class Motore:
    def __init__(self, numero_seriale:str, tipo:str):
        self._numero_seriale = numero_seriale
        self._tipo = tipo
        self.auto = None

    @property
    def numero_seriale(self):
        return self._numero_seriale
    @numero_seriale.setter
    def numero_seriale(self,numero_seriale):
        if type(numero_seriale) == str:
            self._numero_seriale = numero_seriale

    @property
    def tipo(self):
        return self._tipo
    @tipo.setter
    def tipo(self,tipo):
        if type(tipo) == str:
            self._tipo = tipo

    def associa_auto(self, auto):
        self.auto = auto
        auto.motore = self
        

# Creazione delle istanze
auto1 = Auto("Fiat", "500")
auto2 = Auto("Toyota", "Corolla")

motore1 = Motore("ENG123456", "Benzina")
motore2 = Motore("ENG654321", "Diesel")
# Associazione tra auto e motore
auto1.associa_motore(motore1)
auto2.associa_motore(motore2)
# Verifica dell'associazione 
print(f"{auto1.marca} {auto1.modello} ha il motore: {auto1.motore.numero_seriale}")
print(f"Il motore {motore1.numero_seriale} appartiene a: {motore1.auto.marca} {motore1.auto.modello}")

print(f"{auto2.marca} {auto2.modello} ha il motore: {auto2.motore.numero_seriale}")
print(f"Il motore {motore2.numero_seriale} appartiene a: {motore2.auto.marca} {motore2.auto.modello}")

auto = Auto("Fiat", "500")
motore1 = Motore("ENG123456", "Benzina")
motore2 = Motore("ENG654321", "Diesel")

auto.associa_motore(motore1)
<<<<<<< HEAD
auto.associa_motore(motore2)
=======
auto.associa_motore(motore2)
>>>>>>> 0b06bab9d70156b3a60b34f7082cf1d495ade70f
