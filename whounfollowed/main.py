"""

"""

from requests import get
import re

BASE_URL: str = "https://github.com"
END_URL: str = "tab=followers" 


PATTERN= r'<a\s+[^>]*href="https://github\.com/([^/]+)\?page=(\d+)&amp;tab=followers"[^>]*>Next</a>'

def is_next_button_present(text: str) -> bool:
  if not text:
    raise ValueError("La stringa non può essere vuota!")
  
  return bool(re.search(PATTERN, text))
  

def main() -> None:

  controller: bool = False

  print("Start del programma")

#===============
# Primo while
#===============


  while True:
    try:
      nome_utente: str = input("Inserisci lo username del profilo github che vuoi analizzare") 
    
      if not nome_utente:
        raise ValueError("Il nome utente non può essere vuoto")
    
      # TODO: il nome exit esiste come profio
      if nome_utente.strip().lower() == "exit":
        break

      print(f"Stai cercando: {nome_utente}")
 
    
      response = get(f"{BASE_URL}/{nome_utente}")

      if response.status_code == 404:
        print("Il profilo non esiste")
        
      else:
        print(f"Profilo {nome_utente} trovato")
        controller = True
        break

    except Exception as e:
      print(f"OPS! Qualcosa è andato storto: {e}")

#===============
# Secondo while
#===============
  counter : int = 1
  
  while controller:

      url = f"{BASE_URL}?page={counter}&{END_URL}"
      try:
        response = get(url)

        with open(f"tmp/pagina-{counter}.txt","w") as f:
          f.write(response.text)
          controller = is_next_button_present(response.text)
          if controller:
            counter = counter + 1
          
          print("File salvato")

      except Exception as e:
        print(f"Errore: {e}")
  
  print("Fine programma, arrivederci")

if __name__ == "__main__":
  main()
