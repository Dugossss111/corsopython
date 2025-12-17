
# ===============================
#   CONFIGURAZIONE E COSTANTI 
# =============================== 

REGEX_TUTTI_CARATTERI = r'.'           # Tutti i caratteri (usare con re.DOTALL)
REGEX_SENZA_SPAZI = r'\S'              # Caratteri esclusi gli spazi
REGEX_SOLO_LETTERE = r'[a-zA-ZÀ-ÿ]'   # Solo lettere, incluse accentate
REGEX_PAROLE = r'\w+'                  # Parole (lettere, numeri, underscore)
REGEX_PAROLE_LETTERE = r'[a-zA-ZÀ-ÿ]+' # Parole composte solo da lettere
REGEX_FRASI = r'[^.!?]+[.!?]+'         # Frasi terminate da . ! ?


# ===============================
#   URL 
# =============================== 

URL: str = "https://raw.githubusercontent.com/emanuelegurini/aws-restart/refs/heads/main/conta-caratteri/text.txt"
