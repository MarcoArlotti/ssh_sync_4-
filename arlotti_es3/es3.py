
class Veicolo:
    # numero_veicoli è un attributo di
    # classe (fuori dal costruttore)
    numero_veicoli = 0
    
    def __init__(self,tipo,marca):
        self.tipo = tipo
        self.marca = marca

        # incrementa ogni volta che viene
        # chiamata una nuova istanza
        Veicolo.numero_veicoli += 1

    @classmethod
    def get_numero_veicoli(cls): 
        # cls == Veicolo
        # (cls è il nome della classe, in caso 
        # si cambia il nome della classe cls 
        # non ha bisogno di essere cambiato)
        return cls.numero_veicoli
        
print(Veicolo.get_numero_veicoli())
auto1 = Veicolo("Auto", "Toyota")
auto2 = Veicolo("Moto", "Honda")
auto3 = Veicolo("Moto", "Honda")
auto4 = Veicolo("Moto", "Honda")
print(Veicolo.get_numero_veicoli())
