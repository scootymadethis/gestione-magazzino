import sys
import os
import time

def prendiMagazzino() -> dict:
    current_dir = os.getcwd()
    files = os.listdir(current_dir + '/dati')
    magazzino = {}
    
    for categoria in files:    
        with open(current_dir + "/dati/" + categoria) as f:
            categoria = categoria.split('.')[0]
            magazzino[categoria] = {}
            
            r = f.readline().strip()
            while r != "":
                
                dati = r.split(';')
                
                nomeArticolo = dati[0]
                qtaArticolo = dati[1]
                magazzino[categoria][nomeArticolo] = int(qtaArticolo)
                
                r = f.readline().strip()
            
    return magazzino

def stampaMenu():
    print("--------------------------------------------------------------------")
    print("|                        MENU DELLE OPZIONI                        |")
    print("|                                                                  |")
    print("|  [1] Per modificare una quantità di un articolo                  |")
    print("|  [2] Per aggiungere o rimuovere un articolo                      |")
    print("|  [3] Per stampare l'elenco di articoli di una categoria          |")
    print("|  [4] Per aggiungere o rimuovere una categoria di articoli        |")
    print("|  [5] Per salvare le informazioni di un magazzino in un file .txt |")
    print("|  [0] Per uscire                                                  |")
    print("--------------------------------------------------------------------")
    
def modificaQta(magazzino: dict, categoria: str, prodotto: str, qtaNuova: int) -> dict:
    magazzino[categoria][prodotto] = qtaNuova
    return magazzino

def aggiungiArticolo(magazzino: dict, categoria: str, nomeProdotto: str, qtaProdotto: int) -> dict:
    magazzino[categoria][nomeProdotto] = qtaProdotto
    return magazzino

def rimuoviArticolo(magazzino: dict, categoria: str, nomeProdotto: str) -> dict:
    magazzino[categoria].pop(nomeProdotto)
    return magazzino

def stampaArticoliCategoria(magazzino: dict, categoria: str) -> str:
    prodotti = magazzino[categoria].keys()
    prodottiStr = ""
    
    for prodotto in prodotti:
        prodottiStr += prodotto + ", " + str(magazzino[categoria].get(prodotto)) + "pz\n"
    
    return prodottiStr

def categoriaEsiste(categorieEsistenti: list, categoria: str) -> bool:
    exists = False

    if categorieEsistenti.__contains__(categoria):
        exists = True

    return exists

def aggiungiCategoria(magazzino: dict, categoria: str, categorieEsistenti: list) -> dict:
    current_dir = os.getcwd()

    if categorieEsistenti.__contains__(categoria):
        magazzino[categoria] = {}
    
        f = open(current_dir + "/dati/" + categoria + ".csv", 'a')
        f.close()

    return magazzino      
def rimuoviCategoria(magazzino: dict, categoria: str) -> dict:
    current_dir = os.getcwd()
    magazzino[categoria] = {}
    
    os.remove(current_dir + "/dati/" + categoria + ".csv")
    
    return magazzino
    
def esci():
    print("Grazie per avermi utilizzato! Esco tra 3 secondi...")
    time.sleep(3)
    sys.exit()


def chiediCategoria(categorieDisponibili: list) -> str:
    str = "Categorie disponibili:\n"
    
    for k in categorieDisponibili:
        str += k + "\n"

    print(str)
    
    categoria = input("\nInserisci il nome della categoria: ").lower()
    
    while not categorieDisponibili.__contains__(categoria):
        print("Devi inserire una categoria valida!")
        categoria = input("\nInserisci il nome della categoria: ").lower()

    return categoria

def chiediProdotto(categoria: str, prodottiDisponibili: list) -> str:
    str = f"Prodotti disponibili nella categoria '{categoria}':\n"
                    
    for k in prodottiDisponibili:
        str += k + "\n"
        
    print(str)

    prodotto = input("\nInserisci il nome del prodotto da rimuovere: ").lower().capitalize()
    
    while not prodottiDisponibili.__contains__(prodotto):
        print("Devi inserire un prodotto valido!")
        prodotto = input("\nInserisci il nome del prodotto da rimuovere: ").lower().capitalize()

    return prodotto

def chiediQta(magazzino: dict, categoria: str, prodotto: str) -> int:
    qtaProdotto = magazzino[categoria].get(prodotto)
                    
    print(f"Quantità dell'articolo '{prodotto}': {qtaProdotto}")
    
    qtaNuova = input("\nInserisci la nuova quantità del prodotto: ")
    
    while not qtaNuova.isnumeric():
        print("Devi inserire un numero valido intero!")
        qtaNuova = input("\nInserisci la nuova quantità del prodotto: ")
    
    qtaNuova = int(qtaNuova)

    return qtaNuova

def salvaMagazzino(magazzino: dict):
    current_dir = os.getcwd()
    categorie = list(magazzino.keys())

    for nomeCategoria in categorie:
        categoria = magazzino.get(nomeCategoria)

        with open(current_dir + "/dati/" + nomeCategoria + ".csv", 'w') as f:
            prodotti = list(categoria.keys())

            for nomeProdotto in prodotti:
                f.write(nomeProdotto + ";" + str(categoria.get(nomeProdotto)) + "\n")

def salvaMagazzinoTxt(magazzino: dict):
    categorie = list(magazzino.keys())

    with open("magazzino.txt", 'w') as f:
        for nomeCategoria in categorie:
            f.write(f"\nCategoria '{nomeCategoria}'\n\n")

            categoria = magazzino.get(nomeCategoria)

            prodotti = list(categoria.keys())

            for nomeProdotto in prodotti:
                f.write(nomeProdotto + ", " + str(categoria.get(nomeProdotto)) + "pz\n")