class Video:
    def __init__(self,titolo,descrizione,url,durata,commenti):
        pass

    class Playlist:
        def __init__(self,video,creatore):
            self.nome = creatore.nome

    }
    class Utente:
        def __init__(self,nome,email,password,playlist,abbonamento):
            pass
        def crea_playlist(nome):
            pass
        def guarda_video(video):
            pass
        def aggiungi_video_playlist(video,playlist):
            pass
        def rimuovi_video_playlist(video,playlist):
            pass
        def cancella_playlist(playlist):
            pass
        def aggiungi_commento(video):
            pass
    }
    class Commento:
        def __init__(autore,commento,data_di_pubblicazione,video,canali_seguiti):
            pass
        
    class Piattaforma {
    }
    class Abbonamento {
        -date inizio
        -date fine
        -str tier
        -float prezzo %%??????
    }