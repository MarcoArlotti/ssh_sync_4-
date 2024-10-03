class MaterialeBiblioteca:
    def __init__(self,disponibile:bool=True):
        self.disponibile = disponibile

    def prestito(self):
        if self.disponibile:
            self.disponibile = False
            return "disponibile"
        else:
            return "già in noleggio"
        
    def restituzione(self):
        self.disponibile = True
        return "ritornato con successo"
       
    def is_diponibile(self):
        return self.disponibile
    
#    def ricerca(self):
    

class Libro(MaterialeBiblioteca):
    def __init__(self,titolo,anno_di_pubblicazione,autore,pagine):
        super().__init__(disponibile)
        self.titolo = titolo
        self.anno_di_pubblicazione = anno_di_pubblicazione
        self.autore = autore
        self.pagine = pagine
    def get_autore(self):
        return self.autore
    def get_titolo(self):
        return self.titolo
    def get_anno_pubblicazione(self):
        return self.anno_di_pubblicazione
    
class Rivista(MaterialeBiblioteca):
    def __init__(self,disponibile,titolo,anno,numero_edizione,editore):
        super().__init__(disponibile)
        self.titolo = titolo
        self.anno = anno
        self.numero_di_edizione = numero_edizione
        self.editore = editore

    def get_titolo(self):
        return self.titolo
    
    def get_numero_di_edizione(self):
        return self.numero_di_edizione

class DVD(MaterialeBiblioteca):
    def __init__(self,disponibile,titolo,regista):
        super().__init__(disponibile)
        self.titolo = titolo
        self.regista = regista

    def get_titolo(self):
        return self.titolo
    
    def get_regista(self):
        return self.regista
    
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
#risultato = MaterialeBiblioteca.ricerca(materiali, titolo="Inception")
#print(risultato.get_titolo())  # Output: Inception