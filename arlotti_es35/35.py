from enum import Enum
import random
import uuid
import datetime
class Utente:
    def __init__(self,id_utente,nome_utente,email):
        self.id_utente = id_utente
        self.nome_utente = nome_utente
        self.email = email
        self.progetti = []
    
    def crea_progetto(self,titolo,genere):
        progetto = ProgettoMusicale(id_progetto=generate_id(),titolo_progetto=titolo,genere_musicale=genere)
        self.progetti.append(progetto)
        return progetto
    
    def progetti_per_genere(self):
        canzoni = {}
        for progetto in self.progetti:
            canzoni[progetto.genere_musicale] = progetto.titolo_progetto
        return canzoni

    def conta_progetti_totali(self):
        return len(self.progetti)

    def strumento_piu_usato(self):
        #grazie galo
        strumenti_count = {
            TipoStrumento.BASSO: 0,
            TipoStrumento.CHITARRA: 0,
            TipoStrumento.BATTERIA: 0,
        }
        for progetto in self.progetti:
            for traccia in progetto.tracce:
                tipo = traccia.strumento_utilizzato.tipo_strumento_virtuale
                strumenti_count[tipo] += 1

        max_count = max(strumenti_count.values())

        for tipo, count in strumenti_count.items():
            if count == max_count:
                return tipo
        return None
 

class ProgettoMusicale:
    def __init__(self,id_progetto,titolo_progetto,genere_musicale):
        self.id_progetto = id_progetto
        self.titolo_progetto = titolo_progetto
        self.data_creazione = "oggi"
        self.genere_musicale = genere_musicale
        self.tracce = []

    def aggiungi_traccia(self,nome_traccia,strumento_utilizzato):
        if type(nome_traccia) == str:
            nome_traccia = TracciaAudio(nome_traccia,strumento_utilizzato)
            self.tracce.append(nome_traccia)
            return nome_traccia
        else:
            raise ValueError("ERRORE nome_traccia NON E' UNA STR")

    def percentuale_tracce_con_effetti():
        pass
    def effetto_piu_usato():
        pass

class TracciaAudio:
    def __init__(self,nome_traccia,strumento_utilizzato):
        self.id_traccia = None
        self.nome_traccia = nome_traccia
        self.durata_secondi = None
        self.volume_db = None
        self.sequenza_note_manuali = None
        self.strumento_utilizzato = strumento_utilizzato
        self.effetti_applicati = []

    def aggiungi_strumento(self,strumento):
        self.strumento_utilizzato = strumento
    
    def applica_effetto(self,effetto):
        self.effetti_applicati.append(effetto)

    def rimuovi_effetto(self,effetto):
        for effetto_ in self.effetti_applicati:
            if effetto_ == effetto:
                self.effetti_applicati.remove(effetto_)
            
    def imposta_sequenza_note(self,note):
        self.sequenza_note_manuali = note

    def modifica_volume(self,nuovo_volume_db):
        if -20 < nuovo_volume_db < 20:
            self.volume_db = nuovo_volume_db
        else:
            raise ValueError("ERRORE nuovo_volume_db NON E' tra -20 e +20")
    
    def ha_effetti():
        pass
    def numero_note():
        pass

class StrumentoVirtuale:
    def __init__(self,id_strumento,nome_strumento,tipo_strumento_virtuale):
        self.id_strumento = id_strumento
        self.nome_strumento = nome_strumento
        self.tipo_strumento_virtuale = tipo_strumento_virtuale
    
class EffettoAudio:
    def __init__(self,id_effetto,nome_effetto,tipo_effetto_audio):
        self.id_effetto = id_effetto
        self.nome_effetto = nome_effetto
        self.tipo_effetto_audio = tipo_effetto_audio

class TipoStrumento(Enum):
    BATTERIA = 1
    CHITARRA = 2
    BASSO = 3

class TipoEffetto(Enum):
    RIVERBERO = 1
    DELAY = 2
    DISTORSIONE = 3

def generate_id():
    return f"{uuid.uuid1()}"

# Esempio di utilizzo
if __name__ == "__main__":
    # Creazione utente
    utente = Utente(generate_id(), "Mario Rossi", "mario@example.com")

    # Creazione strumenti
    basso = StrumentoVirtuale(generate_id(), "Basso elettrico", TipoStrumento.BASSO)
    chitarra = StrumentoVirtuale(generate_id(), "Chitarra elettrica", TipoStrumento.CHITARRA)
    batteria = StrumentoVirtuale(generate_id(), "Batteria acustica", TipoStrumento.BATTERIA)

    # Creazione e gestione primo progetto (Rock)
    progetto_rock = utente.crea_progetto("La Mia Canzone", "Rock")

    traccia_basso = progetto_rock.aggiungi_traccia("Linea di basso", basso)
    traccia_chitarra = progetto_rock.aggiungi_traccia("Chitarra ritmica", chitarra)

    distorsione = EffettoAudio(generate_id(), "Distorsione Heavy", TipoEffetto.DISTORSIONE)
    riverbero = EffettoAudio(generate_id(), "Riverbero Hall", TipoEffetto.RIVERBERO)

    traccia_basso.applica_effetto(distorsione)
    traccia_chitarra.applica_effetto(riverbero)

    traccia_basso.modifica_volume(-6)
    traccia_chitarra.modifica_volume(-3)

    traccia_basso.imposta_sequenza_note("C2 G2 C3 E3")
    traccia_chitarra.imposta_sequenza_note("E4 G4 B4")

    # Creazione e gestione secondo progetto (Jazz)
    progetto_jazz = utente.crea_progetto("Jazz Session", "Jazz")

    traccia_basso_jazz = progetto_jazz.aggiungi_traccia("Bass groove", basso)
    traccia_batteria = progetto_jazz.aggiungi_traccia("Drums", batteria)

    delay = EffettoAudio(generate_id(), "Delay leggero", TipoEffetto.DELAY)
    traccia_basso_jazz.applica_effetto(delay)

    # Test dei metodi statistici
    print("\nStatistiche utente:")
    print(f"Totale progetti: {utente.conta_progetti_totali()}")
    print(f"Progetti per genere: {utente.progetti_per_genere()}")
    print(f"Strumento più usato: {utente.strumento_piu_usato()}")

    print("\nStatistiche progetto Rock:")
    print(f"Percentuale tracce con effetti: {progetto_rock.percentuale_tracce_con_effetti()}%")
    print(f"Effetto più usato: {progetto_rock.effetto_piu_usato()}")

    print("\nStatistiche tracce:")
    print(f"Traccia basso ha effetti: {traccia_basso.ha_effetti()}")