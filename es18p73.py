import math

def main():
    lista = [i ** 2 for i in range(0, int(math.sqrt(200)) + 1) if i % 2 != 0]
    print(f"Quadrati dispari: {lista}")

if __name__ == '__main__':
    main()
