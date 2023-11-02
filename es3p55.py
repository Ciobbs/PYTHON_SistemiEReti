def main():
    parola = "Python"
    if len(parola) >= 2:
        lettera_iniziale = parola[0]
        lettera_finale = parola[-1]
        print(f"Parola: {parola}")
        print(f"Lettera iniziale: {lettera_iniziale}")
        print(f"Lettera finale: {lettera_finale}")
    else:
        print("Parola troppo corta.")
if __name__ == "__main__":
    main()
