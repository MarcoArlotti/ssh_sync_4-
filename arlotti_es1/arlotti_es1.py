class Persona:
    def __init__(self, nome, eta, citta):
        self.nome = nome
        self.eta = eta
        self.citta = citta

    def saluta(self):
        return f"Ciao, mi chiamo {self.nome}."

    def descrizione(self):
        return f"Ho {self.eta} anni e vivo a {self.citta}."

persona1 = Persona("Mario",30,"Roma")

persona1.saluta()
persona1.descrizione()