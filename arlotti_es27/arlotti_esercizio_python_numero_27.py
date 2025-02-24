class Volo:
    def __init__(self,numero_volo,destinazione,partenza,capacita_massima):
        self._numero_volo = numero_volo
        self._destinazione = destinazione
        self._partenza = partenza
        self._capacita_massima = capacita_massima

    @property
    def numero_volo(self):
        return self._numero_volo
    @numero_volo.setter
    def numero_volo(self,nuova_numero_volo):
        if type(nuova_numero_volo) == int:
            self._numero_volo = nuova_numero_volo

    @property
    def destinazione(self):
        return self._destinazione
    @destinazione.setter
    def destinazione(self,nuova_destinazione):
        if type(nuova_destinazione) == str:
            self._destinazione = nuova_destinazione

    @property
    def partenza(self):
        return self._partenza
    @partenza.setter
    def partenza(self,nuova_partenza):
        if type(nuova_partenza) == list:
            self._partenza = nuova_partenza

    @property
    def capacita_massima(self):
        return self._capacita_massima
    @capacita_massima.setter
    def capacita_massima(self,nuova_capacita_massima):
        if type(nuova_capacita_massima) == int:
            self._capacita_massima = nuova_capacita_massima

class SistemaPrenotazioni:
    def __init__(self,lista_voli,lista_prenotazioni):
        self._lista_voli = lista_voli
        self._lista_prenotazioni = lista_prenotazioni

    @property
    def lista_voli(self):
        return self._lista_voli
    @lista_voli.setter
    def lista_voli(self,nuova_lista_voli):
        if type(nuova_lista_voli) == str:
            self._lista_voli = nuova_lista_voli

    @property
    def lista_prenotazioni(self):
        return self._lista_prenotazioni
    @lista_prenotazioni.setter
    def lista_prenotazioni(self,nuova_lista_prenotazioni):
        if type(nuova_lista_prenotazioni) == str:
            self._lista_prenotazioni = nuova_lista_prenotazioni


    def aggiungi_volo(self,Volo):
        if type(Volo) != str and type(Volo) != int and type(Volo) != float and type(Volo) != bool and type(Volo) != tuple:
            self._lista_voli.append(Volo)
            return True
        else:
            return False

    def aggiungi_prenotazione(self,Prenotazione,Volo):
        if type(Volo) != str and type(Volo) != int and type(Volo) != float and type(Volo) != bool and type(Volo) != tuple:
            if type(Prenotazione) != str and type(Prenotazione) != int and type(Prenotazione) != float and type(Prenotazione) != bool and type(Prenotazione) != tuple:
                Prenotazione._volo = Volo
                self._lista_prenotazioni.append(Prenotazione)
                return True
        else:
            return False
    
    def mostra_tutti_voli_disponibili(self):
        for volo in self._lista_voli:
            mese = volo._partenza[0]
            giorno = volo._partenza[1]
            anno = volo._partenza[2]
            ore = volo._partenza[3]
            minuti = volo._partenza[4]
            print(f"NUMERO VOLO:{volo._numero_volo}, DESTINAZIONE:{volo._destinazione}, PARTENZA:(mese:{mese},giorno:{giorno},anno:{anno},ore:{ore},minuti:{minuti}), CAPIENZA MASSIMA: {volo._capacita_massima}")

class Prenotazione:
    def __init__(self,nome_passeggiero,classe,volo):
        self._nome_passeggiero = nome_passeggiero
        self._classe = classe
        self._volo = volo
    
    @property
    def nome_passeggiero(self):
        return self._nome_passeggiero
    @nome_passeggiero.setter
    def nome_passeggiero(self,nuova_nome_passeggiero):
        if type(nuova_nome_passeggiero) == str:
            self._nome_passeggiero = nuova_nome_passeggiero

    @property
    def classe(self):
        return self._classe
    @classe.setter
    def classe(self,nuova_classe):
        if type(nuova_classe) == str:
            self._classe = nuova_classe

    @property
    def volo(self):
        return self._volo
    @volo.setter
    def volo(self,nuova_volo):
        if type(nuova_volo) != str and type(nuova_volo) != int and type(nuova_volo) != float and type(nuova_volo) != bool and type(nuova_volo) != tuple:
            self._volo = nuova_volo

def main():

    data1 = [1,27,25,15,30] #mese / giorno / anno / ore / minuti

    volo1 = Volo(1,"Francia",data1,200)
    volo2 = Volo(2,"Inghilterra",data1,160)
    volo3 = Volo(3,"Spagna",data1,300)

    persona1 = Prenotazione("Fabio","classe A",volo1)
    persona2 = Prenotazione("Mario","classe C",volo2)
    persona3 = Prenotazione("Luigi","classe B",volo3)

    sistemaPrenotazioni1 = SistemaPrenotazioni([],[])

    print(sistemaPrenotazioni1.aggiungi_prenotazione(persona1,volo1))
    print(sistemaPrenotazioni1.aggiungi_prenotazione(persona2,volo2))
    print(sistemaPrenotazioni1.aggiungi_prenotazione(persona3,volo3))

    print(sistemaPrenotazioni1.aggiungi_volo(volo1))
    print(sistemaPrenotazioni1.aggiungi_volo(volo2))
    print(sistemaPrenotazioni1.aggiungi_volo(volo3))

    sistemaPrenotazioni1.mostra_tutti_voli_disponibili()

main()