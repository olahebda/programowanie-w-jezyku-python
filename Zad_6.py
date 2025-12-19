def funkcja6(lista1:list, lista2:list):
    lista3 = lista1 + lista2
    lista3_bez_duplikatow = list(set(lista3))
    lista3_do_szescianiu = [x**3 for x in lista3_bez_duplikatow]
    return lista3_do_szescianiu

lista1 = [2,5,5]
lista2 = [3,4,5]
funkcja6(lista1, lista2)
print(funkcja6(lista1, lista2))