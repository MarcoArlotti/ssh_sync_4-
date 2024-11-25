```mermaid
classDiagram
Medico -- Farmaci
Farmaci -- Medico

class Ospedale
Ospedale:string +nome
Ospedale:string +indirizzo
class Medici
Medici:string +nome
Medici:string +cognome
Medici:string +specializzazione
class Pazienti
Pazienti:string +nome
Pazienti:string +cognome
Pazienti:string +data_di_nascita
class Farmaci
Famaci:float + dose
Farmaci:string + nome
class Reparti
Reparti:string +nome
class Infermieri
Infermieri:string +nome
Infermieri:string +cognome
Infermieri:string +turno_di_lavoro
class Cartella_clinica
Cartella_clinica:list +visite_mediche
Cartella_clinica:
Cartella_clinica:
class Visite_mediche
Visite_mediche:string +data
Visite_mediche:class +medico
Visite_mediche:string +note
```