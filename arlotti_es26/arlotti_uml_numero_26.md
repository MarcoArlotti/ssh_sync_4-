```mermaid
    classDiagram

    class Flotta {
    -listlista_veicoli
    -aggiungi_veicolo(Veicolo) : void
    -stampa_tutti_veicoli() : void
    }
    class Veicolo {
    -str marca
    -str modello
    -str carburante
    }
    class Auto {
    }
    class Camion {
    }
    Auto --|> Veicolo
    Camion --|> Veicolo
    Flotta "1" --> "1..*" Veicolo :gestisce e crea