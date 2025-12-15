def is_lista_utente_filled(lista_utente: list[str]) -> bool:
    if len(lista_utente) < 3:
        return True
    else: 
        return False

def get_ingredente_formattato(ingrediente: str) -> str:
    if not ingrediente:
        log_message("Il messaggio non deve essere vuoto", "ALERT")
    
    return ingrediente.strip().lower()


def get_input_from_utente(text: str) -> str:
    if not text:
        log_message("Il messaggio non deve essere vuoto", "ALERT")

    print("*"*30)
    return input(text)

 
def log_message(message: str, type: str) -> None:
   if not message:
        log_message("Il messaggio non deve essere vuoto", "ALERT")
    
   icon = None
   match type:
     case "ALERT":
      icon = "⚠️"
     case "INFO":
      icon = "✅"
    
   print(f"{icon} - {message}")



def main() -> None: 
    log_message("Start del programa", "INFO")

    lista_ricetta: list[str] = ["farina", "acqua", "lievito"]
    lista_utente: list[str] = []
    
    while is_lista_utente_filled(lista_utente):
        ingrediente = get_input_from_utente("Inserisci un ingrediente: ") 
        if not ingrediente:
            log_message("l'ingrediente non deve essere vuoto", "ALERT")
        
        ingrediente_formattato: str = get_ingredente_formattato(ingrediente)

        if ingrediente_formattato in lista_ricetta:

            if ingrediente_formattato in lista_utente:
                log_message("Ingrediente già inserito", "ALERT")
            else:
                lista_utente.append(ingrediente_formattato)
                print(lista_utente, "INFO")
            
        else: 
            log_message("Ingrediente non valido", "ALERT")


    print("impasta e fai la pizza")
    print("End del programma")



main()