class Dipendente:
    def __init__(self,nome: str,stipendio: float) -> None:
        self.nome = nome
        self.stipendio = stipendio


class Manager(Dipendente):
    def __init__(self, nome: str, stipendio: float,numero_di_team: int) -> None:
        super().__init__(self,stipendio)
        self.numero_di_team = numero_di_team

    def get_nome(self):
        return self.nome
    
    def get_stipendio(self):
        return self.stipendio
    
    def get_numero_di_team(self):
        return self.numero_di_team

class Sviluppatore(Dipendente):
    def __init__(self, nome: str, stipendio: float,linguaggio_di_ptogrammazione: str) -> None:
        super().__init__(self,stipendio)
        self.linguaggio_di_programmazione = linguaggio_di_ptogrammazione

    def get_nome(self):
        return self.nome
    
    def get_stipendio(self):
        return self.stipendio
    
    def get_linguaggio_di_programmazione(self):
        return self.linguaggio_di_programmazione
    
manager = Manager("Alice", 50000, 3)
print(manager.get_nome())  # Output: Alice
print(manager.get_stipendio())  # Output: 50000
print(manager.get_numero_di_team())  # Output: 3

sviluppatore = Sviluppatore("Bob", 40000, "Python")
print(sviluppatore.get_nome())  # Output: Bob
print(sviluppatore.get_stipendio())  # Output: 40000
print(sviluppatore.get_linguaggio_di_programmazione())
# Output: Python