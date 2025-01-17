class Albergo:
    def __init__(self,lista_camere:list):
        self._lista_camere = lista_camere
        self._lista_camere_disponibili = self._lista_camere
        self._lista_camere_prenotate = []

    def aggiungi_camera(self,nuova_camera):
        if type(nuova_camera) != str and type(nuova_camera) != int and type(nuova_camera) != float and type(nuova_camera) != bool and type(nuova_camera) != tuple:
            self._lista_camere.append(nuova_camera)
        else:
            raise ValueError("ERRORE IN aggiungi_camera")
        
    def prenota_stanza(self,camera_da_prenotare):
        for i in self._lista_camere:
            if camera_da_prenotare.occupata == False and i == camera_da_prenotare:
                camera_da_prenotare.occupata = True
                self._lista_camere_disponibili.remove(camera_da_prenotare)
                self._lista_camere_prenotate.append(camera_da_prenotare)
                break
            else:
                raise ValueError("ERRORE IN prenota_stanza")

    def visualizza_camere_disponibili(self):
        return 0
    def visualizza_camere_prenotate(self):
        return self._lista_camere_prenotate
    
@property
def lista_camere(self):
    return self._lista_camere
@lista_camere.setter
def lista_camere(self,lista_camere_da_verificare):
    if type(lista_camere_da_verificare) == list:
        self._lista_camere = lista_camere_da_verificare
    else:
        raise ValueError("ERRORE IN lista_camere")


class Camera:
    def __init__(self,numero:int,tipo:str):
        self._numero = numero
        self._tipo = tipo
        self.occupata = False

@property
def numero(self):
    return self._numero
@numero.setter
def numero(self,numero_da_verificare):
    if type(numero_da_verificare) == int:
        self._numero = numero_da_verificare
    else:
        raise ValueError("ERRORE IN numero")
    
@property
def tipo(self):
    return self._tipo
@tipo.setter
def tipo(self,tipo_da_verificare):
    if type(tipo_da_verificare) == str:
        self._tipo = tipo_da_verificare
    else:
        raise ValueError("ERRORE IN tipo")
    

cam1 = Camera(1,"camera1")
cam2 = Camera(2,"camera2")
cam3 = Camera(3,"camera3")
cam4 = Camera(4,"camera4")
alb1 = Albergo([])
alb1.aggiungi_camera(cam1)
alb1.aggiungi_camera(cam2)
alb1.aggiungi_camera(cam3)
alb1.aggiungi_camera(cam4)

alb1.prenota_stanza(cam1)
alb1.prenota_stanza(cam2)

cam_dispo = alb1.visualizza_camere_disponibili()
cam_occup = alb1.visualizza_camere_prenotate()
print("disponibili:")
for i in cam_dispo:
    print(i._tipo,end="\t")
    print(f"numero:{i._numero}")
print("occupate:")
for j in cam_occup:
    print(j._tipo,end="\t")
    print(f"numero:{j._numero}")