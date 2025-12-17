# ===============================
#   UI
# =============================== 

def print_risultato(value: int, spec: str) -> None:
    """Stampa il risultato delle operazioni di calcolo caratteri etc."""
    if value is None:
        raise ValueError(f"{value} è obbligatorio (non può essere None)")
    if not isinstance(value, (int)):
        raise TypeError(f"{value} deve essere un numero")

    print("*"*50)
    print(f"Il numero di {spec} è {value}")
    print("*"*50)