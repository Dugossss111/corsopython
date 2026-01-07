"""
Voglio creare un programma che sia in grado di accedere alla mia lista 
di follower su Github e che riesca a tracciarli giorno per giorno, 
in questo modo posso capire chi ha smesso di seguirmi e chi mi segue.

https://github.com/emanuelegurini?tab=followers
https://github.com/emanuelegurini?page=2&tab=followers
<a rel="nofollow" href="https://github.com/emanuelegurini?page=2&amp;tab=followers">Next</a>


OPERAZIONI DA COMPIERE:
1. strat
2. scarichiamo il contenuto di una pagina
3. verifichiamo se è presente il bottone NEXT
        - se si:
            - prendiamo l'URL e scarichiamo anche quella pagina fino all'ultima
        - se no:
            - verifichiamo se ci sono i follower attraverso lo specifico elemento httml

        -dobbiamo salvare i follower e il numero
            -dove?
                -in un file
       
"""
from requests import get
import re
import uuid
import datetime
import json
import os

# Configurazioni
BASE_URL: str = "https://github.com/"
END_URL: str = "tab=followers"

PATTERN_NEXT: str = r'<a\s+[^>]*href="https://github\.com/([^/]+)\?page=(\d+)&amp;tab=followers"[^>]*>Next</a>'
PATTERN_USER: str = r'<span class="Link--secondary(?: pl-1)?">([^<]+)</span>'

# Funzione per creare il record dei follower
def create_record_object(user_list: list[str]) -> dict[str, str]:
    if not user_list:
        return None
    
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    clean_date = now_utc.isoformat(timespec='milliseconds').replace('+00:00', 'Z')

    return {
        'id': str(uuid.uuid4()),
        'createdAt': clean_date,
        'users': user_list,
        'numberOfUsers': len(user_list)
    }

# Funzione per salvare i record in db
def save(db_name: str, new_value: dict[str, str]) -> bool:
    # Assicuriamoci che la cartella "db" esista
    os.makedirs("db", exist_ok=True)
    file_path = f"db/{db_name}"

    # Se il file non esiste, creiamolo vuoto
    if not os.path.isfile(file_path):
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump([], f)

    # Leggiamo il file esistente
    with open(file_path, "r", encoding="utf-8") as f:
        db = json.load(f)

    # Aggiungiamo il nuovo record
    db.append(new_value)

    # Riscriviamo il file
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=4, ensure_ascii=False)

    return True

# Funzione per verificare presenza bottone Next
def is_next_button_present(text: str) -> bool:
    if not text:
        raise ValueError("La stringa non può essere vuota.")
    return bool(re.search(PATTERN_NEXT, text))

def main() -> None:
    # Creiamo cartella tmp se non esiste
    os.makedirs("tmp", exist_ok=True)

    controller: bool = False
    counter: int = 0
    
    print("Start del programma")

    # Chiediamo username
    while True:
        try:
            nome_utente: str = input("Inserisci il nome utente che vuoi analizzare del profilo Github: ")
            if not nome_utente:
                raise ValueError("Il nome utente non può essere vuoto.")
            
            if nome_utente.strip().lower() == "opsexit":
                break
            
            print(f"Stai cercando: {nome_utente}")
            
            # Verifichiamo che l'utente esista
            response = get(f"{BASE_URL}{nome_utente}")
            if response.status_code == 404:
                print("Il profilo non esiste")
            else:
                print(f"Profilo {nome_utente} trovato correttamente.")
                controller = True
                break

        except Exception as e:
            print(f"OPS! Qualcosa è andato storto: {e}")


    # Scarichiamo tutte le pagine dei follower
    while controller:
        counter += 1
        url = f"{BASE_URL}{nome_utente}?page={counter}&{END_URL}"
        try:
            response = get(url)
            print(response.status_code)
            
            # Salviamo la pagina temporaneamente
            with open(f"tmp/pagina-{counter}.txt", "w", encoding="utf-8") as f:
                f.write(response.text)
            
            # Controlliamo se c'è la pagina successiva
            controller = is_next_button_present(response.text)
            print("File salvato.")

        except Exception as e:
            print(f"Errore: {e}")
            break

    # Leggiamo tutte le pagine e estraiamo utenti
    lista_utenti: list[str] = []
    for i in range(counter):
        print(f"Counter: {i+1}")
        with open(f"tmp/pagina-{i+1}.txt", "r", encoding="utf-8") as f:
            text = f.read()
            lista_utenti.extend(re.findall(PATTERN_USER, text))

 
    # Salviamo il record nel db
    save("db.json", create_record_object(lista_utenti))
    print("Fine programma, arrivederci.")

if __name__ == "__main__":
    main()