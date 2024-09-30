class Pagamento:
    def processa_pagamento(self):
        pass

class CartaDiCredito(Pagamento):
    def __init__(self,nome,codice1,codice2,codice3):
        self.nome = nome
        self.codice1 = codice1
        self.codice2 = codice2
        self.codice3 = codice3

    def processa_pagamento(self):
        print(f"pagamento fatto con carta di credito, grazie {self.nome} con {self.codice1}, {self.codice2}, {self.codice3}")

class PayPal(Pagamento):
    def __init__(self,email,password):
        self.email = email
        self.password = password
    def processa_pagamento(self):
        print(f"pagamento fatto con PayPal, grazie {self.email} con {self.password}")

# Esempio di utilizzo
def effettua_pagamento(metodo_di_pagamento: Pagamento):
    metodo_di_pagamento.processa_pagamento()

pagamento_carta = CartaDiCredito("Mario Rossi", "1234 5678 9012 3456", "12/23", "123")
pagamento_paypal = PayPal("mario.rossi@example.com", "password123")

effettua_pagamento(pagamento_carta)  # Output: Elaborazione pagamento 
#con Carta di Credito per Mario Rossi
effettua_pagamento(pagamento_paypal)  # Output: Elaborazione pagamento
#con PayPal per mario.rossi@example.com