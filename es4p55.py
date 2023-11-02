def main():
    parola = "Python"
    if len(parola) >= 3:
        parola_int = parola[1:-1]
        print(f"Parola originale: {parola}")
        print(f"Parola senza le lettere iniziali e finali: {parola_int}")
    else:
        print("La parola è troppo corta per rimuovere le lettere iniziali e finali.")
if __name__ == "__main__":
    main()
