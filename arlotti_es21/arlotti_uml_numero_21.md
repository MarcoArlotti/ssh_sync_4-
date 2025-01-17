```mermaid
    classDiagram
class Albergo {
    list: lista_camere
}

class Camera {
    int: numero_stanza
    str: tipo
    bool: occupata
}
Albergo "1"--> "n" Camera :possiede
```