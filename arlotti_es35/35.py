from enum import Enum
import random

class Utente:
    def __init__(self,id_utente,nome_utente,email):
        self.id_utente = id_utente
        self.nome_utente = nome_utente
        self.email = email
        self.progetti = []
    
    def crea_progetto(self,titolo):
        titolo = ProgettoMusicale(titolo)
        self.progetti.append(titolo)
        return titolo
    
    def progetti_per_genere(self):
        pass

    def conta_progetti_totali(self):
        return len(self.progetti)

    def strumento_piu_usato(self):
        pass

class ProgettoMusicale:
    def __init__(self,titolo_progetto):
        self.id_progetto = random.randint(1,1000000000000000000000000)
        self.titolo_progetto = titolo_progetto
        self.data_creazione = None
        self.genere_musicale = None
        self.tracce = []

    def aggiungi_traccia(self,nome_traccia):
        if type(nome_traccia) == str:
            self.tracce.append(nome_traccia)

            nome_traccia = TracciaAudio(nome_traccia)
            return nome_traccia
        else:
            raise ValueError("ERRORE nome_traccia NON E' UNA STR")

    def percentuale_tracce_con_effetti():
        pass
    def effetto_piu_usato():
        pass

class TracciaAudio:
    def __init__(self,nome_traccia):
        self.id_traccia = None
        self.nome_traccia = nome_traccia
        self.durata_secondi = None
        self.volume_db = None
        self.sequenza_note_manuali = None
        self.strumento_utilizzato = None
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


# Esempio di utilizzo
if __name__ == "__main__":
    # Creazione utente
    utente = Utente("u1", "Mario Rossi", "mario@example.com")  # type: ignore # noqa: F821

    # Creazione progetti
    progetto_rock = utente.crea_progetto("La Mia Canzone Rock")
    progetto_rock.genere_musicale = "Rock"
    
    progetto_jazz = utente.crea_progetto("Jazz Session")
    progetto_jazz.genere_musicale = "Jazz"

    # Aggiunta tracce al progetto rock
    traccia_basso = progetto_rock.aggiungi_traccia("Linea di basso")
    traccia_chitarra = progetto_rock.aggiungi_traccia("Chitarra ritmica")

    # Creazione e aggiunta strumenti
    basso = StrumentoVirtuale("s1", "Basso elettrico", TipoStrumento.BASSO)  # type: ignore # noqa: F821
    chitarra = StrumentoVirtuale("s2", "Chitarra elettrica", TipoStrumento.CHITARRA)  # type: ignore # noqa: F821
    
    traccia_basso.aggiungi_strumento(basso)
    traccia_chitarra.aggiungi_strumento(chitarra)

    # Aggiunta effetti
    distorsione = EffettoAudio("e1", "Distorsione Heavy", TipoEffetto.DISTORSIONE)  # type: ignore # noqa: F821
    delay = EffettoAudio("e2", "Delay Echo", TipoEffetto.DELAY)  # type: ignore # noqa: F821
    
    traccia_basso.applica_effetto(distorsione)
    traccia_chitarra.applica_effetto(distorsione)
    traccia_chitarra.applica_effetto(delay)

    # Impostazione volume e note
    traccia_basso.modifica_volume(-6)
    traccia_basso.imposta_sequenza_note("C2 G2 C3 E3")
    traccia_chitarra.modifica_volume(-3)
    traccia_chitarra.imposta_sequenza_note("C4 G4 C5 E5 G5")

    # Test dei metodi statistici
    print("\nStatistiche a livello utente:")
    print(f"Progetti per genere: {utente.progetti_per_genere()}")
    print(f"Numero totali progetti: {utente.conta_progetti_totali()}")
    # print(f"Strumento più usato: {utente.strumento_piu_usato().nome_strumento}") TODO

    print("\nStatistiche progetto rock:")
    # print(f"Percentuale tracce con effetti: {progetto_rock.percentuale_tracce_con_effetti()}%")
    # print(f"Effetto più usato: {progetto_rock.effetto_piu_usato().nome_effetto}")

    print("\nStatistiche traccia basso:")
    # print(f"Ha effetti: {traccia_basso.ha_effetti()}")
    # print(f"Numero di note: {traccia_basso.numero_note()}")