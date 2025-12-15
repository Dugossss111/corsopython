
def mostra_feedback(messaggio: str) -> None:
    """
    Restituisce il feedback formattato nella maniera desiderata.
    """
    simbol: str = "*"*30      #Creo una stringa 'simbol' contenente 30 asterischi per incorniciare il messaggio
    print(f"""                #Stampo il messaggio incorniciato. Le triple virgolette permettono un blocco multi-linea
{simbol}
{messaggio}
{simbol}
""")

def is_risposta_esatta(scelta: str, risposta_esatta: str) -> bool:

    # Confronta la scelta dell'utente (convertita in maiuscolo) con la risposta corretta.
    # Attenzione: la funzione usa scelta.upper() ma non normalizza 'risposta_esatta'.
    # Se 'risposta_esatta' nel file è minuscola, il confronto potrebbe fallire.

    if scelta.upper() == risposta_esatta:
        return True
    else:
        return False
    # Nota: potremmo semplicemente return scelta.upper() == risposta_esatta

def genera_feedback(is_corretta: bool) -> str:

     # Se is_corretta è True ritorna il messaggio di vittoria, altrimenti quello di errore.
    if is_corretta == True:
        return "Hai indovinato!"
    else:
        return "Non hai indovinato."
    

def valida_scelta(scelta: str) -> bool:
    """
    Questa funzione prende un valore di tipo stringa e verifica che la risposta sia una delle opzioni tra A, B, C e D. 
    Se la risposta è una stringa vuota, restituisce false, idem se la risposta non è una di quelle sopra elencate.
    """
    # Converto la scelta in maiuscolo per non dipendere dal formato inserito dall'utente
    scelta_tmp = scelta.upper()

    # Controllo se la scelta è esattamente "A", "B", "C" o "D".
    if scelta_tmp == "A" or scelta_tmp == "B" or scelta_tmp == "C" or scelta_tmp == "D":
        return True
    else: 
        return False

def mostra_domanda(domanda: str) -> None: 
    """
    Questa funzione restituisce la domanda e le opzioni della riposta. 
    """
    
    print(domanda)

def raccogli_risposta() -> str:
     
     # Chiedo all'utente di inserire la scelta e ritorno la stringa esattamente com'è (senza normalizzarla qui).  
    return input("Inserisci la tua scelta: ")
    

def leggi_file(file_path: str) -> str:
    # Apro il file in lettura testuale e ne leggo tutto il contenuto come stringa; lo ritorno.
    with open(file_path, "r") as file:
        content = file.read()
        return content

def estrai_index(content: str) -> int: 
    # Cerca il carattere speciale "£" e ritorna l'indice della sua prima occorrenza.
    # Attenzione: se "£" non è presente .index() solleverà ValueError e il programma crasha.
    return content.index("£")

def estrai_domanda(content: str, index: int) -> str:
    # Restituisce la porzione di stringa prima dell'indice: la domanda (contenuto da 0 a index-1).
    return content[0:index]

def estrai_risposta(content: str, index: int) -> str:
    # Restituisce la porzione di stringa dopo il carattere "£": la risposta.
    return content[index+1:]

def estrai_lista_domande(file_path: str) -> list[str]:
     # Inizializzo una lista vuota per contenere i nomi dei file/domande
    lista_domande: list[str] = []
     # Apro il file che contiene i nomi dei file/domande (es. "domande.txt")
    with open(file_path, "r") as f:
        # Itero ogni riga del file; ogni riga rappresenta probabilmente il nome di un file
        for i in f:
            # strip() rimuove newline e spazi esterni; aggiungo il nome alla lista
            lista_domande.append(i.strip())
     # Ritorno la lista costruita   
    return lista_domande 

def genera_statistiche(risultato_finale: list[dict[str, str | bool]]) -> dict[str, int]:
    # Crea il dict che conterrà le statistiche finale
    statistica: dict[str, int] = {}

     # Inizializzo contatori a zero
    risposte_esatte: int = 0
    risposte_non_esatte: int = 0

     # Itero sulla lista di risultati (ogni elemento è un dict con chiavi "domanda" e "risposta_corretta")
    for i in risultato_finale: 
        # Se il campo "risposta_corretta" è True incremento il contatore delle esatte
        if i["risposta_corretta"]:
            risposte_esatte += 1
        else:
            risposte_non_esatte += 1

 # Compongo il dizionario di statistica e lo ritorno
    statistica["risposte_esatte"] = risposte_esatte
    statistica["risposte_non_esatte"] = risposte_non_esatte
    return statistica

def get_numero_domanda_corrente(value: int) -> int:
    #restituisce l'indice della domanda corrente +1 per l'utente
    return value + 1

def print_indice_domanda(valore_domanda_corrente: int, valore_domande_totali: int) -> None:
    # restituiscce l'indicatore della domanda corrente rispetto al numero di domande totali
    print("-----------------------")
    print(f"Domanda 1 di 5")
    print("-----------------------")

def main():
    # Inizializzo strutture dati vuote
    lista_domande: list[str] = []
    risultato_finale: list[dict[str, str | bool]] = []
    # domanda_e_risposta è un dizionario temporaneo che conterrà "domanda" e "risposta" per la domanda corrente.
    # Nota: i valori sono impostati a None ma l'annotazione dice str; è meglio inizializzarli come "" o typing.Optional[str].
    domanda_e_risposta: dict[str, str] = {"domanda" : None, "risposta" : None}
   
    # Estraggo la lista dei nomi dei file/domande dal file "domande.txt"
    lista_domande = estrai_lista_domande("domande.txt")

    # Inizializzo il contatore della domanda corrente a 0 (indice della lista)
    counter_domanda_corrente: int = 0

    # Salvo la lunghezza della lista per controllare il while
    lista_domande_length: int = len(lista_domande)

    # Ciclo finché il contatore è minore della lunghezza della lista (scorro tutte le domande)
    while counter_domanda_corrente < lista_domande_length:
        # Leggo il contenuto del file della domanda corrente (es. "domande_risposte/q1.txt")
        content: str = leggi_file(f"domande_risposte/{lista_domande[counter_domanda_corrente]}")
        # Estraggo l'indice del delimitatore "£" nel contenuto
        index: int = estrai_index(content)
        # Estraggo la porzione prima della "£" come domanda
        domanda_e_risposta["domanda"] = estrai_domanda(content, index)
        # Estraggo la porzione dopo la "£" come risposta corretta
        domanda_e_risposta["risposta"] = estrai_risposta(content, index)

        domanda_corrente: int = get_numero_domanda_corrente(counter_domanda_corrente)
        print_numero_domanda(domanda_corrente, lista_domande_length)
        mostra_domanda(domanda_e_risposta["domanda"])

        # Mostro la domanda all'utente
        mostra_domanda(domanda_e_risposta["domanda"])

        # Raccogli la risposta dall'utente (input)
        risposta_utente: str = raccogli_risposta()

        # Verifico se la risposta inserita è valida (A, B, C o D)
        is_risposta_valid: bool = valida_scelta(risposta_utente)

        feedback: str = ""        # inizializzo il messaggio di feedback vuoto

        if is_risposta_valid:
            # Se la risposta è valida creo un record di risultato
            risultato: dict[str, str | bool] = {}
            # Controllo se la risposta è esatta; is_risposta_esatta confronta scelta.upper() con la risposta estratta
            is_risposta_corretta: bool = is_risposta_esatta(risposta_utente, domanda_e_risposta["risposta"])
            # Genero il feedback testuale (es. "Hai indovinato!" o "Non hai indovinato.")
            feedback = genera_feedback(is_risposta_corretta)
            # Compongo il risultato da aggiungere alle statistiche finali
            risultato["domanda"] = lista_domande[counter_domanda_corrente]
            risultato["risposta_corretta"] = is_risposta_corretta
            # Aggiungo il risultato alla lista finale
            risultato_finale.append(risultato)
            # Passo alla domanda successiva incrementando il contatore
            counter_domanda_corrente += 1
        else: 
            # Se la scelta non è valida, preparo un messaggio di errore ma *non* incremento il contatore.
            # Questo permette all'utente di riprovare la stessa domanda.
            feedback = "Inserisci solo la risposta tra le opzioni elencate"

        # Mostro il messaggio di feedback (sia in caso di scelta valida sia non valida)
        mostra_feedback(feedback)

    # Dopo aver processato tutte le domande genero le statistiche dai risultati raccolti
    statistiche: dict[str, int] = genera_statistiche(risultato_finale)

     # Stampo il numero di risposte esatte e non esatte (due print separate)
    print(statistiche["risposte_esatte"])
    print(statistiche["risposte_non_esatte"])   


# Entry point del nostro programma: chiamo main() all'avvio
main()
from data.services import (
    get_lista_domande_e_risposte, 
    valida_scelta, 
    is_risposta_esatta, 
    get_numero_domanda_corrente, 
    get_counter_aggiornato,
    genera_statistiche,
    calcola_percentuale,
    verifica_superamento,
    recupera_dati_domanda,
    aggiorna_lista_risultati
)
from ui.console import (
    mostra_feedback, 
    mostra_domanda, 
    print_numero_domanda, 
    print_gioco_terminato, 
    genera_feedback, 
    raccogli_risposta,
    mostra_risultati_finali,
    gestisci_menu_fine_gioco
)

def main():
    lista_domande = get_lista_domande_e_risposte("domande.txt")
    risultato_finale: list[dict[str, str | bool]] = []

    counter: int = 0
    totale_domande: int = len(lista_domande)

    while counter <= totale_domande:

        if counter == totale_domande:
            nuovo_indice = gestisci_menu_fine_gioco(counter, totale_domande, risultato_finale)
            if nuovo_indice is None: 
                break
            counter = nuovo_indice
            continue
        
        # recupero dei dati
        dati_correnti = recupera_dati_domanda(lista_domande[counter]) 

        # presentazione domande
        domanda_corrente: int = get_numero_domanda_corrente(counter)
        print_numero_domanda(domanda_corrente, totale_domande)
        mostra_domanda(dati_correnti["domanda"])

        # input dell'utente
        risposta_utente: str = raccogli_risposta()

        feedback: str = ""

        if valida_scelta(risposta_utente):
            esatta: bool = is_risposta_esatta(risposta_utente, dati_correnti["risposta"])
            mostra_feedback(genera_feedback(esatta))

            risultato_corrente = {
                "domanda" : lista_domande[counter],
                "risposta_corretta" : esatta,
                "scelta_utente" : risposta_utente.upper()
            }

            aggiorna_lista_risultati(risultato_finale, risultato_corrente, counter)


        else: 
            mostra_feedback("Inserisci solo la risposta tra le opzioni elencate")

        # navigazione domanda (successiva / precedente)
        if counter > 0:
            input_prev_next: str = input("Digita 'P' per andare alla domanda precedente oppure qualsiasi altro tasto per continuare: ")
            counter = get_counter_aggiornato(counter, input_prev_next)
        else:
            counter += 1 

    # statistiche finali
    print_gioco_terminato()

    statistiche: dict[str, int] = genera_statistiche(risultato_finale)
    esatte = statistiche["risposte_esatte"]
    errate = statistiche["risposte_non_esatte"]
    totale_domande_fatte = esatte + errate
    
    perc = calcola_percentuale(esatte, totale_domande_fatte)
    is_superato = verifica_superamento(perc)
    
    mostra_risultati_finali(esatte, errate, totale_domande_fatte, perc, is_superato)

if __name__ == "__main__": 
    main()

