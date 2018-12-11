class No:
    def __init__(self,dado):
        self.dado = dado
        self.proximo = None

class Lista_simples:
    def __init__(self):
        self.__primeiro = None
        self.__ultimo = None
        self.__tamanho = 0
        self.__interando = None

    def __len__(self):
        return self.__tamanho

    def inserir(self,indice,dado):
        novo = No(dado)
        if self.is_empty():
            self.__primeiro = novo
            self.__ultimo = novo

        elif indice <= 0:
            novo.proximo = self.__primeiro
            self.__primeiro = novo

        elif indice >= self.__tamanho:
            self.__ultimo.proximo = novo
            self.__ultimo = novo

        else:
            perc = self.__primeiro
            for i in range(self.__tamanho):
                if i == indice -1:
                    aux = perc.proximo
                    perc.proximo = novo
                    novo.proximo = aux

                else:
                    perc = perc.proximo
        self.__tamanho += 1

    def remover(self,indice):
        if self.is_empty():
            return False

        elif indice == 0:
            perc = self.__primeiro
            self.__primeiro = perc.proximo
            perc = None

        elif indice >= self.__tamanho:
            perc = self.__primeiro

            for i in range(self.__tamanho):
                if i == self.__tamanho-2:
                    perc.proximo = None
                    self.__ultimo = perc
                else:
                    perc = perc.proximo
        else:
            perc = self.__primeiro
            for i in range(self.__tamanho):
                if i == indice -1:
                    aux = perc.proximo
                    perc.proximo = aux.proximo
                    aux = None
                else:
                    perc = perc.proximo

        self.__tamanho -= 1

    def __getitem__(self, indice,dado):
        perc = self._get_index_(indice)
        if perc:
            return perc.dado
        else:
            raise IndexError("List index out of range")

    def __setitem__(self, indice, dado):
        perc = self._get_index_(indice)
        if perc:
            perc.dado = dado
        else:
            raise IndexError("List index out of range")

    def _get_index_(self, indice):
        if self.__tamanho <= indice:
            return None
        else:
            perc = self.__primeiro
            for i in range(self.__tamanho-1):
                if i == indice:
                    return perc.dado
                else:
                    perc = perc.proximo
    def __next__(self):
        if self.__interando is None:
            self.__interando = self.__primeiro
        else:
            self.__interando = self.__interando.proximo

        if self.__interando is not None:
            return self.__interando.dado

        raise StopIteration

    def __str__(self):
        perc = self.__primeiro
        dado = '[ '
        while perc != None:
            dado += str(perc.dado) + ' ,'
            perc = perc.proximo
        dado = dado.strip(', ')
        dado += ']'
        return dado

    def is_empty(self):
        return self.__tamanho == 0

    def __repr__(self):
        return self.__str__()
