class Libro:
    def __init__(self, titolo:str, autore :str, pagine:int):
        self._titolo = titolo
        self._autore = autore
        self._pagine = pagine

    @property
    def titolo(self):
        return self._titolo

    @titolo.setter
    def titolo(self,titolo):
        if titolo != "" and str:
            self._titolo = titolo


    @property
    def autore(self):
        return self._titolo

    @autore.setter
    def autore(self,autore):
        if autore != "" and str:
            self._autore = autore


    @property
    def pagine(self):
        return self._pagine

    @pagine.setter
    def pagine(self,pagine):
        if pagine > 0:
            self._pagine = pagine

# Esempio di utilizzo
libro = Libro("Il Signore degli Anelli", "J.R.R. Tolkien", 1200)
print(libro.titolo)  # Chiama automaticamente il getter
libro.titolo = "Lo Hobbit"  # Chiama automaticamente il setter
print(libro.titolo)