from Listas_AED.lista_ligada import *
#from Listas_AED.lista_encadeada import lista_encadeada

#lista = lista_encadeada()
#lista.append(7)
#lista.append(80)
#lista.append(56)
#lista.append(67)
#lista.append(10)
#print(lista.busca(80))
#lista.inserir(0,22)
#print(lista[0])
#lista.inserir(3,88)
#print(lista[1])
#print(lista[2])
#print(lista[3])
#lista.remover(80)
#print(lista[1])

nomes = Lista(['Fulano', 'Beltrano', 'Sicrano'])

print(nomes)

for i, e in enumerate(nomes):
    print('i - {} | Nome: {}'.format(i, e))
