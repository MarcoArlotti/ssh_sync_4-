class Parco_naturale:
    def __init__(self,lista_ecosistemi):
        self._lista_ecosistemi = lista_ecosistemi

class Ecosistema:
    def __init__(self,lista_sensori,tipo):
        self._lista_sensori = lista_sensori
        self._tipo = tipo
    def aggiungi_sensore(self,sensore):
        if type(sensore) != str and type(sensore) != int and type(sensore) != float and type(sensore) != bool and type(sensore) != tuple:
            self._lista_sensori.append(sensore)

    def rimuovi_sensore(self,sensore):
        if type(sensore) != str and type(sensore) != int and type(sensore) != float and type(sensore) != bool and type(sensore) != tuple:
            for sensore_ in self._lista_sensori:
                if sensore._valore == sensore_._valore and sensore._ecosistema == sensore_._ecosistema and sensore._tipo_valore == sensore_._tipo_valore and sensore._valore == sensore_._valore and sensore._stato == sensore_._stato:
                    self._lista_sensori.remove(sensore_)
                    return True
            return False
        
    def controllo_automatico_sensore(self,sensore):
        if sensore._tipo_valore == "temperatura":
            if sensore._valore > 30:
                sensore.attiva_sensore()
                return True
            else:
                sensore.spegni_sensore()
                return False

        elif sensore._tipo_valore == "umidita":
            if sensore._valore < 60:
                sensore.attiva_sensore()
                return True
            else:
                sensore.spegni_sensore()
                return False

        elif sensore._tipo_valore == "aria":
            if sensore._valore < 40:
                sensore.attiva_sensore()
                return True
            else:
                sensore.spegni_sensore()
                return False

    def restituisci_valori(self,sensore):
        dict = {
            sensore._ecosistema : "ecosistema",
            sensore._tipo_valore : "tipo_valore",
            sensore._valore : "valore",
            sensore._stato : "stato"
        }
        return dict

class Sensore:
    def __init__(self,ecosistema,tipo_valore,valore,stato):
        self._ecosistema = ecosistema
        self._tipo_valore = tipo_valore
        self._valore = valore
        self._stato = stato
    @property
    def ecosistema(self):
        return self._ecosistema
    @ecosistema.setter
    def ecosistema(self,nuovo_eco):
        self._ecosistema = nuovo_eco
        
    def attiva_sensore(self):
        if self._stato == False:
            self._stato = True
            return True
        else:
            return False
        
    def spegni_sensore(self):
        if self._stato == False:
            return False
        else:
            self._stato = False
            return True


sens1 = Sensore(None,"temperatura",20,False)
sens2 = Sensore(None,"umidita",60,False)
sens3 = Sensore(None,"aria",10,False)

eco1 = Ecosistema([sens1,sens2,sens3],"foresta")
eco2 = Ecosistema([],"zona umida")

sens1._ecosistema = eco1
sens2._ecosistema = eco1
sens3._ecosistema = eco1

parco1 = Parco_naturale([eco1,eco2])
ris1 = eco1.controllo_automatico_sensore(sens1)
ris2 = eco1.controllo_automatico_sensore(sens2)

if ris1 == True:
    print("il primo sensore si è acceso")
else:
    print("il primo sensore si è spento")
if ris2 == True:
    print("il secondo sensore si è acceso")
else:
    print("il secondo sensore si è spento")