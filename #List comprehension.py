def main():
    #List comprehension
    #Lista con i primi 6 quadrati perfetti
    import random
    quadrati = [i ** 2 for i in range(1,6)]
    print(quadrati)
    stringhe = ["Computer", "ciao", "cellulare"]
    stringhe_c = [parola for parola in stringhe if parola[0] == "c"]
    print(stringhe_c)
    voti = [random.randint(2, 10) for i in range (10)]
    print(voti)
    voti_insuff = [voto for voto in voti if voto < 6]
    print(voti_insuff)
if __name__ == "__main__":
    main()