# pesquisa binaria - considerando uma lista ordenada

def pesquisa_binaria(lista, item):
    lista = sorted(lista)
    baixo = 0
    alto = len(lista) - 1
    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[int(meio)]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1  # pesquisa na metade inferior
        else:
            baixo = meio + 1

        return None


# teste
numeros = [1, 4, 2, 3, 5, 7, 6, 8, 9, 10]
item = 5
index = print(pesquisa_binaria(numeros, item))
