from lista_treino import Lista_treino

lista = Lista_treino()
lista.inserir(0, 'HELDONJOSE')
lista.inserir(1, 'Jose')
lista.inserir(0, 'pedro')
lista.inserir(3, 'Carlos')
print(len(lista))
#print(lista._primeiro.dado)
# lista.inserir(2, 'joao')
# print(lista._len_())
print(lista)
#
lista.remover(5)
print(lista)
#lista.remover()

#print(lista)



'''novo.próximo = anterior.próximo


                    anterior.próximo = novo

                    #ADICIONA ESSAS DUAS LINHAS
                    atual.anterior = novo
                    novo.anterior = anterior
'''