def main():
    parola = "ciobssss"  # Sostituisci con la tua parola
    if len(parola) >= 8:
        parola_sost = parola[:2] + "?" + parola[3:]
        print(f"Parola originale: {parola}")
        print(f"Parola con ? al posto della terza lettera: {parola_sost}")
    else:
        print("La parola deve avere almeno 8 lettere.")

if __name__ == "__main__":
    main()
