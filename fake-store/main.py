
from requests import get, post, Response
from requests.exceptions import HTTPError, ConnectionError, Timeout

BASE_URL: str = "https://api.escuelajs.co/api/v1/products"

# ===============================
#   Repository
# ===============================

def get_lista_prodotti(URL: str) -> list[dict[str, any]]:
    if not URL: 
        raise ValueError("L'URL non può essere vuoto!")

    response: Response = get_data(URL) 
    data = response.json()

    if not isinstance(data, list):
        raise TypeError(
            f"Risposta inattesa: mi aspettavo un lista, "
            f"ma ho ricevuto {type(data).__name__}"
    )

    return data

def get_prodotto(URL: str) -> dict[str, any]:
    if not URL: 
        raise ValueError("L'URL non può essere vuoto!")

    response: Response = get_data(URL) 
    data = response.json()

    if not isinstance(data, dict):
        raise TypeError(
            f"Risposta inattesa: mi aspettavo un dict, "
            f"ma ho ricevuto {type(data).__name__}"
    )

    return data

def create_product(URL: str, data: dict) -> dict[str, any]:

    if not URL or not data: 
        raise ValueError("L'URL non può essere vuoto!")

    if not isinstance(data, dict):
        raise TypeError(
            f"Risposta inattesa: mi aspettavo un dict, "
            f"ma ho ricevuto {type(data).__name__}"
        )

    response = post_data(URL, data)
    return response.json()

def create_category(URL: str, data: dict) -> dict[str, any]:

    if not URL or not data: 
        raise ValueError("L'URL non può essere vuoto!")

    if not isinstance(data, dict):
        raise TypeError(
            f"Risposta inattesa: mi aspettavo un dict, "
            f"ma ho ricevuto {type(data).__name__}"
    	)

    response = post_data(URL, data)
    return response.json()
 

def post_data(URL: str, data: dict) -> Response:
    if not URL: 
        raise ValueError("L'URL non può essere vuoto!")

    response: Response = post(URL, headers={"Content-Type": "application/json"}, json=data)
    response.raise_for_status()
    return response

def get_data(URL: str) -> Response:
    if not URL: 
        raise ValueError("L'URL non può essere vuoto!")
    
    response : Response = get(URL)
    response.raise_for_status()
    return response

# ===============================
#   Model
# ===============================

def product_model(product: dict[str, any]) -> dict[str, any]:
    return {
        "id": product["id"], 
        "title": product["title"], 
        "price": product["price"], 
        "category": product["category"]["name"],
        "description": product["description"]
    }

def product_list_model(product_list: list[dict[str, any]]) -> list[dict[str, str]]:
    """Restituisce una lista di prodotti definita in {id: valore, title: nome prodotto}"""
    return [{"id": str(product["id"]), "title": str(product["title"])} for product in product_list]

# ===============================
#   UI
# ===============================

def print_prodotto(product: dict[str, any]) -> None:
    print("*" * 30)
    print("PRODOTTO")
    print("*" * 30)
    print(f"ID: {product['id']}")
    print(f"Titolo: {product['title']}")
    print(f"Category: {product['category']['name']}")
    print(f"PRICE: {product['price']}")

def print_product_list(product_list: list[dict]) -> None:
    print("*" * 30)
    print("LISTA PRODOTTI")
    print("*" * 30)

    for product in product_list:
        print(f"{product['id']} - {product['title']}")

prod = {
  "title": "Pippo tanto",
  "price": 10,
  "description": "A description",
  "categoryId": 7,
  "images": ["https://placehold.co/600x400"]
}

def main() -> None:

    try: 
        print_product_list(product_list_model(get_lista_prodotti(BASE_URL)))
        #id = input("Inserisci l'id del prdotto da visualizzare:")
        # product= product_model(get_prodotto(f"{BASE_URL}/{id}"))
        #print_prodotto(product)

        print_prodotto(create_product(BASE_URL, prod))
    
    except HTTPError as e:
        print(f"Errore API: {e}")
    except ConnectionError:
        print("Impossibile connettersi al server")
    except Timeout:
        print("Il server non risponde")
    except ValueError as e:
        print(f"Dati non validi: {e}")
    except TypeError as e:
        print(f"Tipo di dato inatteso: {e}")
    

if __name__ == "__main__":
    main()
