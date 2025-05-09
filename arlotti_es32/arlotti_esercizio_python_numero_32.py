
class Video:
    def __init__(self,titolo,descrizione,url,durata):
        self.titolo = titolo
        self.descrizione = descrizione
        self.url = url
        self.durata = durata
        self.commenti = []
        self.piattaforma = None

class Playlist:
    def __init__(self,video,creatore,nome):
        self.nome = nome
        self.video = video
        self.creatore = creatore

class Utente:
    def __init__(self,nome,email,password,abbonamento):
        self.nome = nome
        self.email = email
        self.password = password
        self.abbonamento = abbonamento
        self.playlists = []

    def crea_playlist(self,nome):
        try:
            playlist = Playlist([],self,nome)
            self.playlists.append(playlist)
            return True
        except:
            return False

    def guarda_video(self,video):
        print(f"{self.nome} sta guardando {video.titolo}")

    def aggiungi_video_playlist(self,video,playlist):
        try:
            for playlist in self.playlists:
                if playlist.nome == playlist:
                    playlist.video.append(video)
                    self.playlists.update(playlist)
                    return True
        except:
            return False
    def rimuovi_video_playlist(self,video,playlist):
        try:
            for playlist in self.playlists:
                if playlist.nome == playlist:
                    playlist.video.remove(video)
                    self.playlists.update(playlist)
                    return True
        except:
            return False

    def cancella_playlist(self,playlist):
        try:
            self.playlists.remove(playlist)
            return True
        except:
            return False

    def aggiungi_commento(self,video,commento):
        try:
            video.commenti.append(commento)
            video.piattaforma.video.update(video)
            return True
        except:
            return False
        
class Commento:
    def __init__(self,autore,commento,data_di_pubblicazione,video,):
        self.autore = autore
        self.commento = commento
        self.data_di_pubblicazione = data_di_pubblicazione
        self.video = video

class Piattaforma:
    def __init__(self):
        self.video = []

    def aggiungi_video(self,video_):
        try:
            self.video.append(video_)
            return True
        except:
            return False
    def rimuovi_video(self,video_):
        try:
            self.video.remove(video_)
            return True
        except:
            return False
        
class Abbonamento:
    def __init__(self,inizio,fine,tier,prezzo):
        self.inizio = inizio
        self.fine = fine
        self.tier = tier
        self.prezzo = prezzo

you_fabio = Piattaforma()

video1 = Video("vendo un rene per comprare la switch 2!!!!1!!111!!!","yap yap yap yapyap","www.fabio/1.com",50)

you_fabio.aggiungi_video(video1)

fabio = Utente("nome","fabio@dezznuts.com","1234","povero")

fabio.crea_playlist("test")
fabio.aggiungi_video_playlist(video1,"test")

Commento1 = Commento(fabio,"hisjadjndDSAKJL PRIMO",(12,12,12),video1)
