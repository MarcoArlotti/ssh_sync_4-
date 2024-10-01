class MaterialeBiblioteca:
    def __init__(self,titolo:str,anno_pubblicazione:int,disponibile:bool=True):
        self.Titolo = Titolo
        self.anno_pubblicazione = anno_pubblicazione
        self.disponibile = disponibile
    def prestito(self):
    
    def restituzione(self):

    def get_titolo(self):

    def get_anno_pubblicazione(self):
    
    def is_diponibile(self):
        
    

class Libro(MaterialeBiblioteca):
    def __init__(self,titolo):
    


class Rivista(MaterialeBiblioteca):

class DVD(MaterialeBiblioteca):
# Esempio di utilizzo
libro = Libro("Il Signore degli Anelli", 1954, "J.R.R. Tolkien", 1178)
print(libro.get_titolo())  # Output: Il Signore degli Anelli
print(libro.get_autore())  # Output: J.R.R. Tolkien
libro.prestito()
print(libro.is_disponibile())  # Output: False
libro.restituzione()
print(libro.is_disponibile())  # Output: True

rivista = Rivista("National Geographic", 2023, 5, "Maggio")
print(rivista.get_titolo())  # Output: National Geographic
print(rivista.get_numero_edizione())  # Output: 5

dvd = DVD("Inception", 2010, "Christopher Nolan", 148)
print(dvd.get_titolo())  # Output: Inception
print(dvd.get_regista())  # Output: Christopher Nolan

materiali = [libro, rivista, dvd]
risultato = MaterialeBiblioteca.ricerca(materiali, titolo="Inception")
print(risultato.get_titolo())  # Output: Inception