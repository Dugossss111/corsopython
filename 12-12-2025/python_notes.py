#======================================
#=== PROGRAMMA PER FARE LA PIZZA
#======================================

"""
- input -> programma -> output

Tipi input:
- file nel file system
    - open("nomefile", "r")
- input da parte dell'utente
- dati che vengono da altri computer sulla rete


Tipi output:
- file nel file system
    - open("nomefile", "w")
- output UI 
- dati che vengono mandati ad altri computer

- programma == set di istruzioni
"""

"""
PROGRAMMA PER FARE LA PIZZA
- Obiettivo
Realizzare un programma che prenda gli ingredienti per fare la pizza dall'utente, attraverso input testuale, e restitusca il risultato finale a schermo.
Il computer non sa fare la pizza, quindi dobbiamo istruirlo noi. 

- Passi:
1. prendi ingredienti da utente (interagisci con l'utente) (input) -> if / else per controllare input -> output
2.  - prendi farina
3.  - prendi acqua
4.  - prendi lievito

-- Cosa mi serve
- input 
    - perché voglio prendere gli ingredienti dall'utente
- lista ingredienti ricetta
- lista ingredienti inseriti dall'utente
- if / else
    - input è vuoto?
    - caratteri piccoli
    - controllo che l'ingrediente sia nella lista degli ingredienti
    - controllo che l'ingrediente non sia già stato inserito
    - se l'igrediente passa i controlli aggiungi ingrediente alla lista 
    - altrimenti restituisci errore e poi input
- if / else
    - se la lista degli ingredienti ricetta == alla lista ingredienti inseriti dall'utente allora impasti
        - ingredienti sono tre?
        - controllo con un ciclo quali sono gli ingredienti che mancano
    - altrimenti riproponi input con messaggio degli ingredienti che mancano




5. impasta la pizza
6. stendi pallina
7. prendi pomodoro
8. prendi mozzarella
9. metti pomodoro
10. metti mozzarella
11. metti in forno la pizza
12. esci la pizza


"""

def main():
    return
