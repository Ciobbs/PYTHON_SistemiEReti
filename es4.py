def main():
    num1 = float(input("Inserisci un numero: "))
    num2 = float(input("Inserisci il secondo numero"))
    max = 0
    min = 0;
    if num1 > num2:
        max = num1
        min = num2
    elif num1 < num2 :
        max = num2
        min = num1
        print(f"Ordine decrescente {max, min}")
if __name__ == "__main__":
    main()