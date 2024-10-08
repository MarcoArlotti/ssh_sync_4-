class Dispositivo:
    numero_dispositivi = 0
    def __init__(self, marca: str, modello: str, prezzo: int):
        self.marca = marca
        self.modello = modello
        self.prezzo = prezzo
        self.disponibile = True
    #@staticmethod
    #def conta_dispositivi(numero_dispositivi):
    #    numero_dispositivi = numero_dispositivi + 1
    #    return numero_dispositivi

    def calcola_sconto(prezzo,quanto_scontare):
        scontato = prezzo * quanto_scontare /100
        tot = prezzo - scontato
        return tot

    #@property
    def get_marca(self):
        return self.marca

    #@marca.set
    def set_marca(self,marca_cambiata):
        self.marca = marca_cambiata
    
    def get_modello(self):
        return self.modello
    def set_modello(self,modello_cambiato):
        self.modello = modello_cambiato

    def get_prezzo(self):
        return self.prezzo
    def set_prezzo(self,prezzo_cambiato):
        self.prezzo = prezzo_cambiato
    

    def vendi(self):
        self.disponibile = False
    
    def disponibile(self):
        return self.disponibile 

class Smartphone(Dispositivo):
    def __init__(self, marca: str, modello: str, prezzo: int, memoria_ssd: int):
        super().__init__(marca, modello, prezzo)
        self.memoria_ssd = memoria_ssd

    def descrizione(self):
        return f"Smartphone {self.marca} {self.modello} con {self.memoria_ssd} di spazio"

class Laptop(Dispositivo):
    def __init__(self, marca: str, modello: str, prezzo: int, ram: int):
        super().__init__(marca, modello, prezzo)
        self.ram = ram

    def descrizione(self):
        return f"Laptop {self.marca} {self.modello} con {self.ram}GB di ram"

class Tablet(Dispositivo):
    def __init__(self, marca: str, modello: str, prezzo: int, schermo: int):
        super().__init__(marca, modello, prezzo)
        self.schermo = schermo

    def descrizione(self):
        return f"Tablet {self.marca} {self.modello} con chermo da {self.schermo} pollici"

class Inventario:
    def __init__(self):
        self.inventario = []

    def aggiungi_dispositivo(self,cosa_aggiungere):
        self.inventario.append(cosa_aggiungere)

    def stampa_inventario(inventario):
        for dispositivo in inventario:
            print(type)
            #if dispositivo = type()

# Fase 1
smartphone = Smartphone("Apple", "iPhone 12", 999, 128)
print(smartphone.get_marca())  # Output: Apple
smartphone.vendi()
print(smartphone.disponibile)  # Output: False

# Fase 2
laptop = Laptop("Dell", "XPS 13", 1200, 16)
tablet = Tablet("Samsung", "Galaxy Tab S7", 650, 11)

print(smartphone.descrizione())  # Output: Smartphone Apple iPhone 12 con 128GB di memoria
print(laptop.descrizione())  # Output: Laptop Dell XPS 13 con 16GB di RAM
print(tablet.descrizione())  # Output: Tablet Samsung Galaxy Tab S7 con schermo da 11 pollici

# Fase 3
################print(Dispositivo.conta_dispositivi())  # Output: 3
print(Dispositivo.calcola_sconto(1000, 10))  # Output: 900.0

# Fase 4#############################################################
inventario = Inventario()
inventario.aggiungi_dispositivo(smartphone)
inventario.aggiungi_dispositivo(laptop)
inventario.aggiungi_dispositivo(tablet)

inventario.stampa_inventario()
# Output: 
# Smartphone Apple iPhone 12 con 128GB di memoria
# Laptop Dell XPS 13 con 16GB di RAM
# Tablet Samsung Galaxy Tab S7 con schermo da 11 pollici

# Cerca dispositivi per prezzo
dispositivi_economici = inventario.cerca_per_prezzo(1000)
print("Dispositivi con prezzo inferiore a 1000€:")
for dispositivo in dispositivi_economici:
    print(dispositivo.descrizione())
# Output:
# # Dispositivi con prezzo inferiore a 1000€:
# Smartphone Apple iPhone 12 con 128GB di memoria
# Tablet Samsung Galaxy Tab S7 con schermo da 11 pollici

# Cerca dispositivi disponibili
dispositivi_disponibili = inventario.cerca_disponibili()
print("Dispositivi disponibili:")
for dispositivo in dispositivi_disponibili:
    print(dispositivo.descrizione())
# Output:
# # Dispositivi disponibili:
# Laptop Dell XPS 13 con 16GB di RAM
# Tablet Samsung Galaxy Tab S7 con schermo da 11 pollici