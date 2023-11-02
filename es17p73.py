def main():
    import math

    num = int(input("Inserisci un numero: "))
    esponente = num ** 2
    lista = [2**i for i in range(0, esponente + 1)]
    print(lista)

if __name__ == "__main__":
    main()
