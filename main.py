import funzioni

def main():
    sceltaValida = False

    while not sceltaValida:
        funzioni.stampaMenu()

        scelta = input("Scegli un'opzione: ")

        match scelta:
            case "1":
                sceltaValida = True
                funzioni.modificaQta()
            case "2":
                sceltaValida = True
                funzioni.aggiungiRimuoviArticolo()
            case "3":
                sceltaValida = True
                funzioni.stampaArticoliCategoria()
            case "4":
                sceltaValida = True
                funzioni.aggiungiRimuoviCategoria()
            case "5":
                sceltaValida = True
                funzioni.salvaInfoMagazzino()
            case "0":
                sceltaValida = True
                funzioni.esci()
            case _:
                sceltaValida = False

if __name__ == "__main__":
    main()