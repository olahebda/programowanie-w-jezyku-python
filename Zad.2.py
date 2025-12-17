#Zad 2a.
def lista_imion(imiona):
    for imie in imiona:
        print(imie)

imiona = ["Jan", "Jacek", "Bartłomiej", "Krzysztof", "Piotr"]
lista_imion(imiona)

#Zad 2b.
#i.
def lista_liczb(liczby):
    wynik = []
    for liczba in liczby:
        wynik += [liczba*2]
    return wynik

liczby = [1, 2, 3, 4, 5]
print(lista_liczb(liczby))

#ii.
def lista_liczb(liczby):
    return [liczba * 2 for liczba in liczby]

liczby = [1, 2, 3, 4, 5]
print(lista_liczb(liczby))


