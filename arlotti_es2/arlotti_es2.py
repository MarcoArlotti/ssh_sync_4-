class Conto_bancario:
    def __init__(self, numero_conto, intestatario, saldo):
        self.numero_conto = numero_conto
        self.intestatario = intestatario
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo

    def deposita(self,depositato):
        saldo = conto_bancario.get_saldo() 
        self.__saldo = saldo + depositato #privato

    def preleva(self,prelevare):
        saldo = conto_bancario.get_saldo()
        rimasto = saldo - prelevare
        self.__saldo = rimasto

conto_bancario = Conto_bancario("123456789", "Mario Rossi", 1000.0)
print(conto_bancario.get_saldo())  # Output: 1000.0
conto_bancario.deposita(500.0)
print(conto_bancario.get_saldo())  # Output: 1500.0
conto_bancario.preleva(200.0)
print(conto_bancario.get_saldo())  # Output: 1300.0