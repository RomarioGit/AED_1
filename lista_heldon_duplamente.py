class No:
    def _init_(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None


class ListaEncadeada:
    def _init_(self):
        self.__primeira = None
        self.__ultima = None
        self.__tamanho = 0

    def _len_(self):
        return self.__tamanho

    def inserir(self, indice, valor):
        novo = No(valor)

        if self.is_empty():
            self.__primeira = novo
            self.__ultima = novo

        elif indice <= 0:  # Inserindo no inicio
            novo.proximo = self.__primeira
            self.__primeira.anterior = novo
            self.__primeira = novo

        elif indice >= self.__tamanho:  # Inserindo no fim
            self.__ultima.proximo = novo
            novo.anterior = self.__ultima
            self.__ultima = novo

        else:  # Inserindo no meio da lista
            perc = self.__primeira

            for i in range(self.__tamanho):

                if i == indice - 1:  # Achou a posição

                    aux = perc.proximo
                    novo.anterior = perc

                    perc.proximo = novo
                    aux.anterior = novo

                    break
                else:
                    perc = perc.proximo

        self.__tamanho += 1

    def get_index(self, indice):

        if indice >= self.__tamanho:
            return None

        else:
            perc = self.__primeira

            for i in range(self.__tamanho):
                if i == indice:
                    return perc.valor
                else:
                    perc = perc.proximo

    def remover(self, indice):

        if self.is_empty():  # Está vazia
            return False

        elif (indice == 0):
            perc = self.__primeira
            self.__primeira = perc.proximo
            perc = None

        elif (indice == self.__tamanho - 1):  # Remover no final

            perc = self.__primeira
            for i in range(self.__tamanho - 1):
                if i != indice - 1:  # Não chegou no elemento
                    perc = perc.proximo

                else:  # Encontrou o elemento a ser removido
                    aux = self.__ultima
                    aux = None
                    self.__ultima = perc


        else:
            perc = self.__primeira
            for i in range(self.__tamanho - 1):
                if i != indice - 1:  # Não achou
                    perc = perc.proximo
                else:
                    aux = perc.proximo
                    perc.proximo = aux.proximo
                    aux = None

        self.__tamanho -= 1
        return True

    def _str_(self):
        valor = '[ '
        perc = self.__primeira
        while perc:
            print(perc.valor)
            perc = perc.proximo
        return valor

    def is_empty(self):
        return self.__tamanho == 0


lista = ListaEncadeada()
lista.inserir(0, 'HELDONJOSE')
lista.inserir(0, 'Carlos')
# lista.inserir(10, 'pedro')
# lista.inserir(2, 'joao')
# print(lista._len_())
# print(lista)
#
# lista.remover(1)
print(lista)