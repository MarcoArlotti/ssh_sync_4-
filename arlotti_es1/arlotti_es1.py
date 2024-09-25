class Persona:
    def __init__(self, nome, eta, citta):
        self.nome = nome
        self.eta = eta
        self.citta = citta

    def saluta(self):
        print(f"ciao sono {self.nome}.")

    def descrizione(self):
        print(f"ho {self.eta} e ovviamente ho scelto {self.citta}.")

persona1 = Persona("Mario",18,"Roma")

persona1.saluta()
persona1.descrizione()