"""
Voglio creare un programma che sia in grado di accedere alla mia lista di followers su github e che riesca a tracciarli giorno per giorno. IN questo modo, posso capire chi ha smesso di seguirmi oppure chi mi segue.

1. della lista di follower
    - Dove si trova? nella sezione followers
    - Problema:
        - la lista non è completa e per vedere tutti i followers devo navigare tra le pagine. Inoltre devo utilizzare il bottone next per navigare tra le pagine. Inoltre devo utilizzare il bottone next per navigare tra le pagine

#quando il bottone è cliccabile       
<a rel="nofollow" href="https://github.com/emanuelegurini?page=3&amp;tab=followers"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;">Prossimo</font></font></font></font></a>

#quando non è cliccabile
<span class="disabled color-fg-muted"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;">Prossimo</font></font></span>


https://github.com/emanuelegurini?tab=followers
https://github.com/emanuelegurini?page=2&tab=followers
https://github.com/emanuelegurini?page=3&tab=followers

2. Voglio prendere tutto il contenuto html della pagina per identificare il pattern del bottone


3. voglio ottenere le statistiche
    - dal file in cui ci sono tutti i followers che ho preso nei giorni precedenti



OPERAZIONI DA COMPIERE
1. start
2. scarichiamo il contenuto di una pagina
3. verifichiamo che ci sia il bottone next
    - se si:
        -  prendiamo l'url e scarichiamo anche quella pagina
    - se no:
        - verichichiamo se ci sono i followers attraverso lo specifico elemento html

4. dobbiamo salvare i followers e il numero
    - dove?
        - in un file
        - tabella




"""