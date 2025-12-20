def czy_parzysta(liczba):
    if liczba % 2 == 0:
        return True
    else:
        return False


liczba = 7
wynik = czy_parzysta(liczba)

if wynik:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
