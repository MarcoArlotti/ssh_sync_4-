```mermaid
classDiagram
Allenatore "1" --> "*" Membro: allena
Membro "1" --> "1" Allenatore: possiede
Membro "1" --> "*" Corso: iscriversi
Corso "1" --> "*" Membro: posside
Corso "1" --> "1" Allenatore: tenuto
Allenatore "1" --> "*" Corso: tenuto
Membro "1" --> "1" SchedaAllenamento: possiede
SchedaAllenamento "1" --> "1" Membro: appartiene

class Allenatore {
    nome
    cognome
    specializzazione
    scheda_assegnata
}
class Membro {
    nome
    cognome
    corsi_iscritti
}
class Corso {
    nome
    durata
}
class SchedaAllenamento {
    lista_esercizi
}