class Corso:
    def __init__(self,titolo,descrizione,docente_responsabile,lista_quiz):
        self.titolo = titolo
        self.descrizione = descrizione
        self.docente_responsabile = docente_responsabile
        self.lista_studenti = []
        self.lista_quiz = lista_quiz

class Quiz:
    def __init__(self,nome,requisiti_di_superamento):
        self.nome = nome
        self.lista_domande = []
        self.lista_partecipanti = []
        self.requisiti_di_superamento = requisiti_di_superamento

    def calcola_voto(self):
        pass


class Domanda:
    def __init__(self,testo,lista_risposte,risposta_corretta):
        self.testo = testo
        self.lista_risposte = lista_risposte
        self.risposta_corretta = risposta_corretta


class Studente:
    def __init__(self,nome,cognome,email):
        self.nome = nome
        self.cognome = cognome
        self.email = email
        self.lista_corsi_da_fare = []
        self.lista_corsi_completati = []
        self.lista_corsi_superati = []
        self.lista_corsi_falliti = []

    def iscriviti_a_un_corso(self,corso):
        corso.lista_studenti.append(self)
        self.lista_corsi_da_fare.append(corso)

    def disiscriviti_a_un_corso(self,corso):
        corso.lista_studenti.remove(self)
        try:
            self.lista_corsi_da_fare.remove(corso)
        except:
            self.lista_corsi_completati.remove(corso)

class Fa_quiz:
    def __init__(self,che_quiz_si_sta_facendo,studente_che_lo_fa,risposta_data):
        self.numero_tentativi_fatti = 0
        self.studente_che_lo_fa =studente_che_lo_fa
        self.che_quiz_si_sta_facendo = che_quiz_si_sta_facendo
        self.risposta_data = risposta_data
        self.punteggio = None
        
    def calcola_punteggio():
        pass

class Docente:
    def __init__(self,nome,corsi_creati):
        self.nome = nome
        self.corsi_creati = corsi_creati

if __name__ == "__main__":
    # Creare un corso
    corso_python = Corso("Corso Python", "Introduzione a Python", "Prof. Rossi")

    # Creare un quiz
    quiz = Quiz("Quiz Python Base", punteggioMinimo=1)

    # Aggiungere domande al quiz
    domanda1 = Domanda("Cosa è Python?", ["Un serpente", "Un linguaggio di programmazione", "Un gioco"], 1)
    quiz.domande.append(domanda1)

    # Impostare il quiz per il corso
    corso_python.impostaQuiz(quiz)

    # Creare uno studente
    studente = Studente("Mario", "Rossi", "mario.rossi@email.com")

    # Iscrivere lo studente al corso
    studente.iscriviti_a_un_corso(corso_python)

    # Creare un tentativo di quiz
    tentativo_1 = Fa_quiz(quiz, studente,1)

    # Stampare i risultati
    print(f"Punteggio: {tentativo_1.punteggio}")
    print(f"Superato: {tentativo_1.superato}")

    # Creare un tentativo di quiz
    tentativo_2 = Fa_quiz(quiz, studente,1)

    # Stampare i risultati
    print(f"Punteggio: {tentativo_2.punteggio}")
    print(f"Superato: {tentativo_2.superato}")