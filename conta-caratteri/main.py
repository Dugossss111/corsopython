# CONTACARATTERI

# DOMINIO:
# =========

# 1. INPUT - Sorgente del testo
#    - Lettura da file di testo (.txt)
#    - Visualizzazione contenuto in console

# 2. ELABORAZIONE - Metriche da calcolare
#   - Conteggio caratteri (con e senza spazi)
#   - Conteggio parole
#   - Conteggio frasi
#   - Conteggio paragrafi
#   - Tempo di lettura stimato
#   - Frequenza parole e lettere (ripetizioni)

# 3. OUTPUT - Destinazione risultati
#    - Stampa in console
#    - Scrittura su file

# REGEX REFERENCE:
# ================

# Pattern                 | Descrizione
# ------------------------|--------------------------------------------
# .                       | Tutti i caratteri (con re.DOTALL include \n)
# \S                      | Caratteri senza spazi
# [a-zA-ZÀ-ÿ]             | Solo lettere (incluse accentate)
# \w+                     | Parole (lettere, numeri, underscore)
# [a-zA-ZÀ-ÿ]+            | Parole solo lettere (incluse accentate)
# [^.!?]+[.!?]+           | Frasi (testo seguito da punteggiatura)
# testo.split('\\n\\n')   | Paragrafi (separati da riga vuota)

# ===============================
#   Regex Patterns
# ===============================

# REGEX_TUTTI_CARATTERI = r'.'           # Tutti i caratteri (usare con re.DOTALL)
# REGEX_SENZA_SPAZI = r'\S'              # Caratteri esclusi gli spazi
# REGEX_SOLO_LETTERE = r'[a-zA-ZÀ-ÿ]'   # Solo lettere, incluse accentate
# REGEX_PAROLE = r'\w+'                  # Parole (lettere, numeri, underscore)
# REGEX_PAROLE_LETTERE = r'[a-zA-ZÀ-ÿ]+' # Parole composte solo da lettere
# REGEX_FRASI = r'[^.!?]+[.!?]+'         # Frasi terminate da . ! ?

from ui.console import print_risultato
from data.services import get_caratteri_len, get_phrase_number, get_text_len_no_space, get_words_number
from data.repository import get_data_from_server
from constant import URL

def main() -> None:
    try:
        # content: str = get_file_content("text.txt")
        content: str = get_data_from_server(URL)
        print_risultato(get_caratteri_len(content), "caratteri")
        print_risultato(get_text_len_no_space(content), "caratteri senza spazi")
        print_risultato(get_words_number(content), "parole")
        print_risultato(get_phrase_number(content), "frasi")


    except ValueError as e:
        print(f"{e}")
    
    except FileNotFoundError as e:
        print(f"{e}")
    
    except Exception as e:
        print(f"{e}")


if __name__ == "__main__":
    main()


        