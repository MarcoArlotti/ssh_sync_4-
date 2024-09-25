class Calcolatrice:
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2
    @staticmethod
    def addizione(n1,n2):
        tot = n1 + n2
        return tot
    @staticmethod
    def sottrazione(n1,n2):
        tot = n1 - n2
        return tot
    @staticmethod
    def moltiplicazione(n1,n2):
        tot = n1 * n2
        return tot
    @staticmethod
    def divisione(n1,n2):
        tot = n1 / n2
        return tot

# Esempio di utilizzo
print(Calcolatrice.addizione(10, 5))       # Output: 15
print(Calcolatrice.sottrazione(10, 5))     # Output: 5
print(Calcolatrice.moltiplicazione(10, 5)) # Output: 50
print(Calcolatrice.divisione(10, 5))       # Output: 2.0