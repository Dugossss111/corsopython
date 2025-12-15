# dizionari

personaggio1: dict[str, str] = {   # Creiamo un dizionario chiamato 'personaggio1' con chiavi e valori di tipo stringa
    "nome": "Pippo",                  # chiave "nome" con valore "Pippo"
    "tipo": "cane",
    "email": "pippo@disney.com"
}

print(personaggio1["email"])        # Stampiamo il valore della chiave "email" del dizionario

personaggio1["telefono"] = "0918348081"   # Aggiungiamo una nuova chiave "telefono" con il suo valore
personaggio1["telefono"] = "0918346453"   # Modifichiamo il valore della chiave "telefono"

print(personaggio1.get("telefono"))     # Usando il metodo get(), otteniamo il valore della chiave "telefono"
                                        # Se la chiave non esiste, get() evita errori e restituisce None

for chiave, valore in personaggio1.items():         # Ciclo for per stampare tutte le coppie chiave:valore del dizionario
    print(f"{chiave}:{valore}")




# liste
"""
stringhe: list[str] = ["Pippo", 1]

stringhe.append("Pluto")            # Aggiungiamo altri elementi alla lista
stringhe.append("Minnie")

deleted_values: list[str] = []      # Lista vuota per salvare i valori eliminati

value_to_check_and_delete: str = "Pluto"        # Valore che vogliamo controllare ed eventualmente eliminare dalla lista

is_value_in_the_list: bool = value_to_check_and_delete in stringhe      # Controlliamo se il valore è presente nella lista

if is_value_in_the_list== True:             # Se il valore è presente, lo eliminiamo e lo aggiungiamo alla lista dei valori eliminati
    index_value_to_delete = stringhe.index(value_to_check_and_delete)
    deleted_value = stringhe.pop(index_value_to_delete)
    deleted_values.append(deleted_value)
else:                                       # Se il valore non è presente, stampiamo un messaggio 
    print(f"{value_to_check_and_delete} non esiste nella lista {stringhe}")

print("*"*30)               # Separatore per chiarezza nella stampa
print(stringhe)             # Stampiamo la lista aggiornata
print(deleted_value)        # Stampiamo il valore eliminato
"""