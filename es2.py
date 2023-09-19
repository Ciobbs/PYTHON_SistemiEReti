def main():
    a = float(input("Inserisci un numero: "))
    print(f"Il tipo di a è {type(a)}")
    if a > 5:
        print("a è maggiore 5")
    else:
        print("a è minore o uguale a 5")
if __name__ == "__main__":
    main()