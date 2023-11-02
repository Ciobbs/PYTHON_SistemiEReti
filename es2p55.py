def main():
    prima = 10
    seconda = 20
    print(f"Prima: {prima}, Seconda: {seconda}")
    prima, seconda = seconda, prima
    print(f"Dopo lo scambio - Prima: {prima}, Seconda: {seconda}")
if __name__ == "__main__":
    main()
