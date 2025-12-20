# Zad 2a.
def lista_imion(imiona):
    for imie in imiona:
        print(imie)


imiona = ["Jan", "Jacek", "Bartłomiej", "Krzysztof", "Piotr"]
lista_imion(imiona)


# Zad 2b.
# i.
def lista_liczb(liczby):
    wynik = []
    for liczba in liczby:
        wynik += [liczba*2]
    return wynik


liczby = [1, 2, 3, 4, 5]
print(lista_liczb(liczby))


# ii.
def lista_liczb(liczby):
    return [liczba * 2 for liczba in liczby]


liczby = [1, 2, 3, 4, 5]
print(lista_liczb(liczby))


# Zad 2.c.


def lista_liczb2(liczby):
    for liczba in liczby:
        if liczba % 2 == 0:
            print(liczba)


liczby = list(range(10))
lista_liczb2(liczby)


# Zad 2.d.
def lista_liczb3(liczby):
    for liczba in range(0, len(liczby), 2):
        print(liczby[liczba])


liczby = list(range(10))
lista_liczb3(liczby)
