class MaterialeBiblioteca:
    def __init__(self, titolo, anno_di_pubblicazione):
        self.titolo = titolo
        self.anno_di_pubblicazione = anno_di_pubblicazione
        self.disponibile = True

    def prestito(self):
        if self.disponibile:
            self.disponibile = False
            return "disponibile"
        else:
            return "già in noleggio"
        
    def restituzione(self):
        self.disponibile = True
        return "ritornato con successo"
       
    def is_disponibile(self):
        return self.disponibile

    def get_titolo(self):
        return self.titolo
    
    @staticmethod
    def ricerca(materiali,titolo):
        risultato = []
        for i in materiali:
            titolo_ = i.get_titolo()
            if titolo_ == titolo:
                print("trovato")
                risultato.append(i)
        if risultato == [None]:
            print("libro non trovato")
        return risultato


class Libro(MaterialeBiblioteca):
    def __init__(self,titolo,anno_di_pubblicazione,autore,pagine):
        super().__init__(titolo,anno_di_pubblicazione)
        self.autore = autore
        self.pagine = pagine
    def get_autore(self):
        return self.autore
    def get_anno_pubblicazione(self):
        return self.anno_di_pubblicazione
    
class Rivista(MaterialeBiblioteca):
    def __init__(self,titolo,anno_di_pubblicazione,numero_edizione,autore):
        super().__init__(titolo,anno_di_pubblicazione)
        self.numero_edizione = numero_edizione
        self.autore = autore

    def get_numero_edizione(self):
        return self.numero_edizione

class DVD(MaterialeBiblioteca):
    def __init__(self,titolo,anno_di_pubblicazione,regista,durata):
        super().__init__(titolo,anno_di_pubblicazione)
        self.regista = regista
        self.durata = durata
    
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
risultato = MaterialeBiblioteca.ricerca(materiali, titolo="Inception")
print(risultato)
for risultato_ in risultato:
    print(risultato_.get_titolo())  # Output: Inception