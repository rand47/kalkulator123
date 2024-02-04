import math

def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
    if b != 0:
        return a / b
    else:
        return "Błąd! Nie można dzielić przez zero."

def potegowanie(a, b):
    return a ** b

def pierwiastek_kwadratowy(a):
    return math.sqrt(a)

def sinusa(a):
    return math.sin(math.radians(a))

def cosinusa(a):
    return math.cos(math.radians(a))

def tangensa(a):
    return math.tan(math.radians(a))

def kalkulator():
    print("Witaj w kalkulatorze!")
    while True:
        print("\nWybierz operację:")
        print("1. Dodawanie")
        print("2. Odejmowanie")
        print("3. Mnożenie")
        print("4. Dzielenie")
        print("5. Potęgowanie")
        print("6. Pierwiastek kwadratowy")
        print("7. Sinus")
        print("8. Cosinus")
        print("9. Tangens")
        print("0. Wyjście")

        wybor = input("Twój wybór: ")

        if wybor == '0':
            print("Dziękuję za korzystanie z kalkulatora. Do widzenia!")
            break
        elif wybor in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
            try:
                a = float(input("Podaj pierwszą liczbę: "))
                if wybor != '6':
                    b = float(input("Podaj drugą liczbę: "))
            except ValueError:
                print("Błąd! Wprowadź poprawne liczby.")
                continue

            if wybor == '1':
                print("Wynik: ", dodawanie(a, b))
            elif wybor == '2':
                print("Wynik: ", odejmowanie(a, b))
            elif wybor == '3':
                print("Wynik: ", mnozenie(a, b))
            elif wybor == '4':
                print("Wynik: ", dzielenie(a, b))
            elif wybor == '5':
                print("Wynik: ", potegowanie(a, b))
            elif wybor == '6':
                print("Wynik: ", pierwiastek_kwadratowy(a))
            elif wybor == '7':
                print("Wynik: ", sinusa(a))
            elif wybor == '8':
                print("Wynik: ", cosinusa(a))
            elif wybor == '9':
                print("Wynik: ", tangensa(a))
            else:
                print("Błąd! Wybierz poprawną operację.")
        else:
            print("Błąd! Wybierz poprawną opcję.")

if __name__ == "__main__":
    kalkulator()