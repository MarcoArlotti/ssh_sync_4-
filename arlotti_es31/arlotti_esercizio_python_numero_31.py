from datetime import date
class Corso:
    def __init__(self,titolo,descrizione,docente):
        self.titolo = titolo
        self.descrizione = descrizione
        self.docente = docente
        self.quiz = None
        self.iscritti = []

    def impostaQuiz(self,quiz):
        self.quiz = quiz

    def iscriviStudente(self,studente):
        self.iscritti.append(studente)

class Quiz:
    def __init__(self,titolo,punteggio_minimo):
        self.titolo = titolo
        self.domande = []
        self.punteggio_minimo = punteggio_minimo

    def valutaRisposte(self,risposte):
        punteggio = 0
        i = 0
        for risposta in risposte: 
            if risposta == self.domande[i].risposta_corretta:
                punteggio = punteggio + 1
            i = i + 1
        return punteggio

    def verificaSuperamento(self,punteggio):
        if punteggio >= self.punteggio_minimo:
            return True
        return False

class Domanda:
    def __init__(self,testo,opzioni,risposta_corretta):
        self.testo = testo
        self.opzioni = opzioni
        self.risposta_corretta = risposta_corretta
    
    def verificaRisposta(self,risposta):
        if risposta == self.risposta_corretta:
            return True
        return False

class Studente:
    def __init__(self,nome,cognome,email):
        self.nome = nome
        self.cognome = cognome
        self.email = email
        self.corsiIscritti = []
        self.tentativi = []

class QuizAttempt:
    def __init__(self,quiz,studente):
        self.dataOra = date.today()
        self.quiz = quiz
        self.studente = studente
        self.risposte = None
        self.punteggio = None
        self.superato = None
        
    def submitRisposte(self,risposte_):
        if type(risposte_) == list:
            self.risposte = risposte_
            return True
        return False
    
    def calcolaPunteggio(self):
        i = 0
        punteggio = 0
        for risposta in quiz.domande:
            if risposta.risposta_corretta == self.risposte[i]:
                punteggio = punteggio + 1
            i = i + 1

        self.punteggio = punteggio
        if quiz.punteggio_minimo <= self.punteggio:
            self.superato = True
        else:
            self.superato = False
        return self.punteggio

# Esempio di utilizzo
if __name__ == "__main__":
    # Creare un corso
    corso_python = Corso("Corso Python", "Introduzione a Python", "Prof. Rossi")

    # Creare un quiz
    quiz = Quiz("Quiz Python Base", punteggio_minimo=1)

    # Aggiungere domande al quiz
    domanda1 = Domanda("Cosa è Python?", ["Un serpente", "Un linguaggio di programmazione", "Un gioco"], 1)
    quiz.domande.append(domanda1)

    # Impostare il quiz per il corso
    corso_python.impostaQuiz(quiz)

    # Creare uno studente
    studente = Studente("Mario", "Rossi", "mario.rossi@email.com")

    # Iscrivere lo studente al corso
    corso_python.iscriviStudente(studente)

    # Creare un tentativo di quiz
    tentativo_1 = QuizAttempt(quiz, studente)

    # Sottomettere le risposte
    tentativo_1.submitRisposte([0])  # Risposta sbagliata
    tentativo_1.calcolaPunteggio()
    # Stampare i risultati
    print(f"Punteggio: {tentativo_1.punteggio}")
    print(f"Superato: {tentativo_1.superato}")

    # Creare un tentativo di quiz
    tentativo_2 = QuizAttempt(quiz, studente)

    # Sottomettere le risposte
    tentativo_2.submitRisposte([1])  # Risposta corretta
    tentativo_2.calcolaPunteggio()
    # Stampare i risultati
    print(f"Punteggio: {tentativo_2.punteggio}")
    print(f"Superato: {tentativo_2.superato}")