from datetime import datetime

class Animale:
    def __init__(self,codiceIdentificativo:str, nome:str, eta:int, peso:float):
        self.codiceIdentificativo = codiceIdentificativo
        self.nome = nome
        self.eta = eta
        self.peso = peso
        self.lista_visite = []

    def aggiungi_visita(self,visita):
        self.lista_visite.append(visita)

class Mammifero(Animale):
    def __init__(self, codiceIdentificativo, nome, eta, peso, tipoPelliccia:str, temperaturaCorpo:float, periodoGestazione:int):
        super().__init__(codiceIdentificativo, nome, eta, peso)
        self.tipoPelliccia = tipoPelliccia
        self.temperaturaCorpo = temperaturaCorpo
        self.periodoGestazione = periodoGestazione

class Rettile(Animale):
    def __init__(self, codiceIdentificativo, nome, eta, peso, velenoso:bool):
        super().__init__(codiceIdentificativo, nome, eta, peso)
        self.velenoso = velenoso

class SistemaGestioneZoo:
    def __init__(self):
        self.Lista_animali = []
        self.habitats = []
        self.veterinari = []
        self.lista_RegistroVisite = []

    def aggiungi_animale(self,animale):
        self.Lista_animali.append(animale)

    def rimuovi_animale(self,animale):
        pass

    def assegna_habitat(self,animale,habitat):
        if animale.codiceIdentificativo[0] == "M" and habitat.nome == "Savana Africana": #se la prima lettera è M, è un mammifero
            self.aggiungi_animale(animale)
            habitat.aggiungi_animale(animale)
            return True
        
        elif animale.codiceIdentificativo[0] == "R" and habitat.nome == "Rettilario":
            self.aggiungi_animale(animale)
            habitat.aggiungi_animale(animale)
            return True
        
        else:
            return False
        
    def registra_visita(self,visita):
        self.lista_RegistroVisite.append(visita)


    def get_animali_habitat(self,habitat):
        return habitat.lista_animali_nell_abitat
        
    def get_storico_visite(self,animale):
        return animale.lista_visite
    def get_habitat_compatibili(self,animale):
        pass
    def calcola_eta_media_per_habitat(self):
        pass

class Habitat:
    def __init__(self,codiceArea:str, nome:str, dimensione:float):
        self.codiceArea = codiceArea
        self.nome = nome
        self.dimensione = dimensione
        
        self.lista_animali_nell_abitat = []

    def aggiungi_animale(self,animale):
        self.lista_animali_nell_abitat.append(animale)

    def rimuovi_animale(self,animale):
        for animale_nell_abitat in self.lista_animali_nell_abitat:
            if animale_nell_abitat.codiceIdentificativo == animale.codiceIdentificativo:
                self.lista_animali_nell_abitat.remove(animale_nell_abitat)
                break

    def get_animali(self):
        return self.lista_animali_nell_abitat
    
    def get_eta_media(self):
        lista_animali = self.get_animali()
        tot = 0
        for animale in lista_animali:
            tot = tot + animale.eta
        ris = tot / len(lista_animali)
        print(ris)
        return ris

class VisitaVeterinaria:
    def __init__(self,data:datetime, diagnosi:str, trattamentoProposto:str):
        self.data = data
        self.diagnosi = diagnosi
        self.trattamentoProposto = trattamentoProposto

class Veterinario:
    def __init__(self,matricola:str, nome:str, cognome:str, specializzazione:str, anniEsperienza:str):
        self.matricola = matricola
        self.nome = nome
        self.cognome = cognome
        self.specializzazione = specializzazione
        self.anniEsperienza = anniEsperienza

    def effettua_visita(self,animale,diagnosi,trattamento):
        visitaVeterinaria = VisitaVeterinaria(datetime.now(),diagnosi,trattamento)
        #animale.lista_visite.append(visitaVeterinaria)
        return visitaVeterinaria


############################################################
def main():
    # Creazione del sistema
    zoo = SistemaGestioneZoo()

    # Creazione degli habitat
    savana = Habitat("H001", "Savana Africana", 1000.0)
    rettilario = Habitat("H002", "Rettilario", 500.0)
    zoo.habitats.extend([savana, rettilario])

    # Creazione dei veterinari
    vet1 = Veterinario("V001", "Mario", "Rossi", "Mammiferi", 10)
    vet2 = Veterinario("V002", "Laura", "Bianchi", "Rettili", 8)
    zoo.veterinari.extend([vet1, vet2])

    # Creazione degli animali
    leone = Mammifero("M001", "Simba", 5, 180.0, "Folta", 38.5, 110)
    serpente = Rettile("R001", "Kaa", 3, 5.0, True)
    giraffa = Mammifero("M002", "Melman", 7, 800.0, "Maculata", 38.0, 450)

    # Aggiunta degli animali al sistema
    for animale in [leone, serpente, giraffa]:
        zoo.aggiungi_animale(animale)

    # Assegnazione degli habitat
    zoo.assegna_habitat(leone, savana)
    zoo.assegna_habitat(giraffa, savana)
    success = zoo.assegna_habitat(serpente, savana)
    print("\nTentativo di mettere serpente in savana:", "Riuscito" if success else "Fallito")
    zoo.assegna_habitat(serpente, rettilario)

    # Effettuazione delle visite veterinarie
    visita1 = vet1.effettua_visita(leone, "Controllo di routine", "Somministrazione vaccino annuale")
    zoo.registra_visita(visita1)

    visita2 = vet2.effettua_visita(serpente, "Infezione batterica", "Antibiotico per 7 giorni")
    zoo.registra_visita(visita2)

    # Stampa delle informazioni
    print("\n=== Stato dello Zoo ===")

    print("\nAnimali nella Savana:")
    for animale in zoo.get_animali_habitat(savana):
        print(f"- {animale.nome} ({animale.codiceIdentificativo})")

    print("\nAnimali nel Rettilario:")
    for animale in zoo.get_animali_habitat(rettilario):
        print(f"- {animale.nome} ({animale.codiceIdentificativo})")

    #print("\nEtà media per habitat:")
    #for habitat, eta_media in zoo.calcola_eta_media_per_habitat().items():
    #    print(f"- {habitat}: {eta_media:.1f} anni")

    print("\nStorico visite di Simba:")
    for visita in zoo.get_storico_visite(leone):
        print(f"- Data: {visita.data}")
        print(f"  Veterinario: {visita.veterinario.nome} {visita.veterinario.cognome}")
        print(f"  Diagnosi: {visita.diagnosi}")
        print(f"  Trattamento: {visita.trattamentoProposto}")



if __name__ == "__main__":
    main()

# Tentativo di mettere serpente in savana: Fallito

# === Stato dello Zoo ===

# Animali nella Savana:
# - Simba (M001)
# - Melman (M002)

# Animali nel Rettilario:
# - Kaa (R001)

# Età media per habitat:
# - Savana Africana: 6.0 anni
# - Rettilario: 3.0 anni

# Storico visite di Simba:
# - Data: 2025-02-11 15:27:06.489484
#   Veterinario: Mario Rossi
#   Diagnosi: Controllo di routine
#   Trattamento: Somministrazione vaccino annuale
