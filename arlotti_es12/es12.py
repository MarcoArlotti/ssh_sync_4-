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
        if type(motore.numero_seriale) == str and type(motore.tipo) == str:
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
        auto.engine = self

# Creazione delle istanze
auto1 = Auto("Fiat", "500")
motore1 = Motore("ENG123456", "Benzina")

# Associazione tra auto e motore
auto1.associa_motore(motore1)

# Verifica dell'associazione 
print(f"{auto1.marca} {auto1.modello} ha il motore: {auto1.motore.numero_seriale}")
print(f"Il motore {motore1.numero_seriale} appartiene a: {motore1.auto.marca} {motore1.auto.modello}")
