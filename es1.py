def main():  #definizione della funzione main
    nome = input("Come ti chiami?")
    anno = int(input("Quanti anni hai?"))
    anno_corrente = int(input("Inserisci l'anno corrente: "))


    print(f"Il tuo nome è {nome} e hai {anno} anni.")
    print(f"Sei nato nel {anno_corrente - anno}")
        
if __name__ == "__main__":
    main()