
class No:
    def __init__(self,dado):
        self.dado = dado
        self.proximo = None
class Fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.__tamanho = 0
        self.__iterando = None

    def is_empty(self):
        return self.__tamanho == 0

    def __iter__(self):
        return self

    def __len__(self):
        return self.__tamanho

    def __repr__(self):
        return self.__str__()

    def __get__index(self,indice):
        if indice >= self.__tamanho:
            return None
        else:
            perc = self.__tamanho
            for i in range(self.__tamanho-1):
                if i == indice:
                    return perc.dado
                else:
                    perc = perc.proximo

    def __getitem__(self, indice):
        perc = self.__get__index(indice)
        if perc:
            return perc.dado
        else:
            raise IndexError(" list index out of range")

    def __next__(self):
        if self.__tamanho is None:
            self.__iterando = self.primeiro
        else:
            self.__iterando = self.__iterando.proximo

        if self.__iterando is not None:
            return self.__iterando.dado
        raise StopIteration

    def __setitem__(self, indice, dado):
        perc = self.__get__index(indice)
        if perc:
            perc.dado = dado
        else:
            raise IndexError(" list index out of range")

    def __str__(self):
        perc = self.primeiro
        dado = '['
        for i in range(self.__tamanho):
            dado += str(perc.dado) + ', '
            perc = perc.proximo
        dado = dado.strip(', ')
        dado += ']'
        return dado

    def enqueue(self,dado):
        novo = No(dado)
        if self.is_empty():
            self.primeiro = novo
            self.ultimo = novo

        else:
            self.ultimo.proximo = novo
            self.ultimo = novo
        self.__tamanho += 1

    def denqueue(self):
        if self.is_empty():
            return False
        else:
            aux = self.primeiro
            self.primeiro = aux.proximo
            aux = None
        self.__tamanho -= 1



