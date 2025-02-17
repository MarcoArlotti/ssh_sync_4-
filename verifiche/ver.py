import math

class VeicoloSpaziale:
    def __init__(self, nome:str, velocita_massima:float, massa:float, posizione:list[float]):
        self._nome = nome
        self._velocita_massima = velocita_massima
        self._massa = massa
        self._posizione = posizione
        self._numero_veicoli = 0 #numero tot dei veicoli
    #@staticmethod
    def veicoli_totali(self):
        return self._numero_veicoli
    
    
    def calcola_tempo_comunicazione(self,altro_veicolo) -> float:
        posizione = altro_veicolo.posizione
        x1 = posizione[0] #dati altro veicolo
        y1 = posizione[1] #dati altro veicolo
        z1 = posizione[2] #dati altro veicolo

        posizione2 = self.posizione
        x2 = posizione2[0] #dati veicolo
        y2 = posizione2[1] #dati veicolo
        z2 = posizione2[2] #dati veicolo
        distanza_tra_i_2 = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2 - z1)**2)
        tempo_comunicazione = distanza_tra_i_2 / 299792 #tutti i dati sono in kilometri
        return tempo_comunicazione
    
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self,nome):
        if type(nome) == str:
            self._nome = nome
    
    @property
    def velocita_massima(self):
        return self._velocita_massima
    @velocita_massima.setter
    def velocita_massima(self,velocita_massima):
        if type(velocita_massima) == float:
            self._velocita_massima = velocita_massima
    
    @property
    def massa(self):
        return self._massa
    @massa.setter
    def massa(self,massa):
        if type(massa) == float:
            self._massa = massa
    
    @property
    def posizione(self):
        return self._posizione
    @posizione.setter
    def posizione(self,posizione):
        if type(posizione) == list[float]:
            self._posizione = posizione

class Sonda(VeicoloSpaziale):
    def __init__(self, nome:str, velocita_massima:float, massa:float, posizione:list[float], tipo_missione:str, energia:float, consumo_energia:float):
        super().__init__(nome,velocita_massima,massa,posizione)
        self._tipo_missione = tipo_missione
        self._energia = energia
        self._consumo_energia = consumo_energia

    def __str__(self) -> str:
        #stringa descrittiva dell'astronave TODO
        return f"Sonda: {self.nome} - Velocità Massima: {self.velocita_massima} km/s - Massa: {self.massa} kg - Missione: {self.tipo_missione} - Energia: {self.energia} MJ"
    
    def simula_missione(self,durata) -> bool:
        #durata = 80
        consumo = self._consumo_energia
        energia = self._energia

        consumo_tot = consumo * durata
        
        if consumo_tot <= energia:
            rimasto = energia - consumo_tot
            self._energia = rimasto
            return True
        else:
            return False

    @property
    def tipo_missione(self):
        return self._tipo_missione
    @tipo_missione.setter
    def tipo_missione(self,tipo_missione):
        if type(tipo_missione) == str:
            self._tipo_missione = tipo_missione
    
    @property
    def energia(self):
        return self._energia
    @energia.setter
    def energia(self,energia):
        if type(energia) == float:
            self._energia = energia
    
    @property
    def consumo_energia(self):
        return self._consumo_energia
    @consumo_energia.setter
    def consumo_energia(self,consumo_energia):
        if type(consumo_energia) == float:
            self._consumo_energia = consumo_energia

class Astronave(VeicoloSpaziale):
    def __init__(self, nome:str, velocita_massima:float, massa:float, posizione:list[float], numero_equipaggio:int, carburante:float, consumo_carburante:float):
        super().__init__(nome,velocita_massima,massa,posizione)
        self._numero_equipaggio = numero_equipaggio
        self._carburante = carburante
        self._consumo_carburante = consumo_carburante

    def __str__(self) -> str:
        return f"Astronave: {self.nome} - Velocità Massima: {self.velocita_massima} km/s - Massa: {self.massa} kg - Equipaggio: {self.numero_equipaggio} - Carburante: {self.carburante} t"
    
    def puo_raggiungere(self,distanza):
        consumocarburante = self._consumo_carburante
        carburantenecessario = distanza * consumocarburante
        carburante = self._carburante
        if carburantenecessario <= carburante:
            return True
        else:
            return False

    @property
    def numero_equipaggio(self):
        return self._numero_equipaggio
    @numero_equipaggio.setter
    def numero_equipaggio(self,numero_equipaggio):
        if type(numero_equipaggio) == int:
            self._numero_equipaggio = numero_equipaggio
    
    @property
    def carburante(self):
        return self._carburante
    @carburante.setter
    def carburante(self,carburante):
        if type(carburante) == float:
            self._carburante = carburante
    
    @property
    def consumo_carburante(self):
        return self._consumo_carburante
    @consumo_carburante.setter
    def consumo_carburante(self,consumo_carburante):
        if type(consumo_carburante) == float:
            self._consumo_carburante = consumo_carburante

class StazioneOrbitante(VeicoloSpaziale):
    def __init__(self, nome:str, velocita_massima:float, massa:float, posizione:list[float], moduli:list[str], capacita_aggancio:int) -> None:
        super().__init__(nome,velocita_massima,massa,posizione)
        self._moduli = moduli
        self._capacita_aggancio = capacita_aggancio
        self._veicoli_agganciati = []

    def __str__(self) -> str: 
        return f"Stazione Orbitante: {self.nome} - Moduli: {self.moduli} - Capacità di Aggancio: {self.capacita_aggancio} - Veicoli Agganciati: {self._veicoli_agganciati}"
    
    def sgancia_veicolo(self,veicolo):
        lista_veicoli = self._veicoli_agganciati
        for veicolo_ in lista_veicoli:
            if veicolo_ == veicolo:
                return True
            else:
                return False
    @property
    def moduli(self):
        return self._moduli
    @moduli.setter
    def moduli(self,moduli):
        if type(moduli) == str:
            self._moduli = moduli

    @property
    def capacita_aggancio(self):
        return self._capacita_aggancio
    @capacita_aggancio.setter
    def capacita_aggancio(self,capacita_aggancio):
        if type(capacita_aggancio) == str:
            self._capacita_aggancio = capacita_aggancio

    @property
    def veicoli_agganciati(self):
        return self._veicoli_agganciati
    @veicoli_agganciati.setter
    def veicoli_agganciati(self,veicoli_agganciati):
        if type(veicoli_agganciati) == str:
            self._veicoli_agganciati = veicoli_agganciati

sonda1 = Sonda(
    nome="Explorer I",
    velocita_massima=15,  # km/s
    massa=800,            # kg
    posizione=(1000, 2000, 3000),  # km
    tipo_missione="Ricerca",
    energia=5000,         # MJ
    consumo_energia=50    # MJ/h
)

astronave1 = Astronave(
    nome="Odyssey",
    velocita_massima=12,  # km/s
    massa=200000,         # kg
    posizione=(11500, 12500, 13500),  # km
    numero_equipaggio=100,
    carburante=600,       # tonnellate
    consumo_carburante=0.06  # tonnellate/km
)

stazione1 = StazioneOrbitante(
    nome="Alpha Station",
    velocita_massima=0,   # Stazionaria
    massa=500000,         # kg
    posizione=(0, 0, 0),  # km
    moduli=["Habitat", "Laboratorio", "Comunicazioni"],
    capacita_aggancio=2,
)

# Informazioni sui veicoli
print(sonda1)
print(astronave1)
print(stazione1)
# Sonda: Explorer I - Velocità Massima: 15 km/s - Massa: 800 kg - Missione: Ricerca - Energia: 5000 MJ
# Astronave: Odyssey - Velocità Massima: 12 km/s - Massa: 200000 kg - Equipaggio: 100 - Carburante: 600 t
# Stazione Orbitante: Alpha Station - Moduli: ['Habitat', 'Laboratorio', 'Comunicazioni'] - Capacità di Aggancio: 5 - Veicoli Agganciati: 0

# Simulazione di una missione con la sonda
durata_missione = 80  # ore
if sonda1.simula_missione(durata_missione):
    print("Missione completata con successo.")
else:
    print("Energia insufficiente per completare la missione.")
print(f"Energia residua della sonda: {sonda1.energia} MJ")
# Missione completata con successo.
# Energia residua della sonda: 1000 MJ

# Verifica se l'astronave può raggiungere una destinazione a 8000 km
distanza_destinazione = 8000  # km
if astronave1.puo_raggiungere(distanza_destinazione):
    print("L'astronave può raggiungere la destinazione.")
else:
    print("Carburante insufficiente per raggiungere la destinazione.")
# L'astronave può raggiungere la destinazione.

# Calcolo del tempo di comunicazione tra la sonda e l'astronave
tempo_comunicazione = sonda1.calcola_tempo_comunicazione(astronave1)
print(f"Tempo di comunicazione tra sonda e astronave: {tempo_comunicazione:.2f} s")
# Tempo di comunicazione tra sonda e astronave: 0.06 s


## Aggancio dell'astronave alla stazione
#if stazione1.aggancia_veicolo(astronave1):
#    print("Astronave agganciata con successo alla stazione.")
#else:
#    print("Capacità massima di aggancio raggiunta.")
## Astronave agganciata con successo alla stazione.
#
#
## Elenco dei veicoli agganciati
#veicoli_agganciati = stazione1.elenca_veicoli_agganciati()
#print(f"Veicoli agganciati alla stazione: {veicoli_agganciati}")
## Veicoli agganciati alla stazione: ['Odyssey']
#
## Calcolo del peso totale dei veicoli
#veicoli = [sonda1, astronave1, stazione1]
#peso_totale = calcola_peso_totale(veicoli)
#print(f"Peso totale dei veicoli: {peso_totale} kg")
## Peso totale dei veicoli: 700800 kg
#
## Numero totale di veicoli creati
#print(f"Numero totale di veicoli spaziali: {VeicoloSpaziale.veicoli_totali()}")
## Numero totale di veicoli spaziali: 3