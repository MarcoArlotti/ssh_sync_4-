```mermaid
classDiagram
Studente "*"-->"*" Corso :frequenta
class Studente
Studente:string -nome
Studente:string -matricola
class Corso
Corso:string -titolo
Corso:string -codice
```