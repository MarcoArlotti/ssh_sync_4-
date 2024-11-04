class ContoBancario:
    def __init__(self, numero_conto, intestatario, saldo):
        self.numero_conto = numero_conto
        self.intestatario = intestatario
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo

    def deposita(self,depositato):
        if not depositato < 0:
            saldo = contoBancario.get_saldo() 
            self.__saldo = saldo + depositato #privato

    def preleva(self,prelevare):
        saldo = contoBancario.get_saldo()
        rimasto = saldo - prelevare
        if not rimasto < 0:
            self.__saldo = rimasto

contoBancario = ContoBancario("123456789", "Mario Rossi", 1000.0)
print(contoBancario.get_saldo())  # Output: 1000.0
contoBancario.deposita(500.0)
print(contoBancario.get_saldo())  # Output: 1500.0
contoBancario.preleva(200.0)
print(contoBancario.get_saldo())
contoBancario.preleva(2000.0)
print(contoBancario.get_saldo())  # Output: 1300.0
contoBancario.deposita(-500.0)
print(contoBancario.get_saldo())