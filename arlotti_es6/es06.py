class Pagamento:
    def metodo_di_pagamento():
        
    def processa_pagamento(metodo_di_pagamento: Pagamento):
        metodo_di_pagamento.processa_pagamento()

class CartaDiCredito(Pagamento):

class PayPal(Pagamento):

# Esempio di utilizzo


pagamento_carta = CartaDiCredito("Mario Rossi", "1234 5678 9012 3456", "12/23", "123")
pagamento_paypal = PayPal("mario.rossi@example.com", "password123")

effettua_pagamento(pagamento_carta)  # Output: Elaborazione pagamento 
#con Carta di Credito per Mario Rossi
effettua_pagamento(pagamento_paypal)  # Output: Elaborazione pagamento
#con PayPal per mario.rossi@example.com