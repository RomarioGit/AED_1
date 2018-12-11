
class Nó:
    def __init__(self,dado):#valor que sera armazenado
        self.dado = dado
        self.proximo =  None #variavel que armazena o local que se encontra o proximo nó
        self.anterior = None

class Lista_dupla_encadeada:
    def __init__(self):
        self._primeiro = None
        self._ultimo = None
        self._tamanho = 0

    def __len__(self):
        return self._tamanho

    def inserir(self,indice,dado):
        novo = Nó(dado)
        if self.is_empty():
            self._primeiro = novo
            self._ultimo = novo

        elif indice <= 0:
            novo.proximo = self._primeiro
            self._primeiro.anterior = novo
            self._primeiro = novo

        elif indice >= self._tamanho:
            self._ultimo.proximo = novo
            novo.anterior = self._ultimo
            self._ultimo = novo

        else:
            perc = self._primeiro
            for i in range(self._tamanho):
                if i == indice -1:
                    print("achou")
                    aux = perc.proximo
                    novo.anterior = perc

                    perc.proximo = novo
                    aux.anterior = novo

                    novo.proximo = aux
                    break
                else:
                    perc = perc.proximo
        self._tamanho+=1

    def __getitem__(self, indice):
        perc = self.get_index(indice)
        if perc:
            return perc.dado
        else:
            raise IndexError("List index out of range")  # tratando a exeção

    def __setitem__(self, indice, dado):
        perc = self.get_index(indice)
        if perc:
            perc.dado = dado
        else:
            raise IndexError("List index out of range")  # tratando a exeção


    def remover(self,indice):
        if self.is_empty():
            return False
        elif indice == 0:
            perc = self._primeiro
            perc.proximo = self._primeiro
            perc = None

        elif indice == self._tamanho -1:
            perc = self._primeiro
            for i in range(self._tamanho-1):
                if i != self._tamanho-1:
                    perc = perc.proximo
                else:
                    aux = self._ultimo
                    aux = None
                    perc = self._ultimo

        else:
            perc = self._primeiro
            for i in range(self._tamanho-1):
                if i != self._tamanho-1:
                    perc = perc.proximo
                else:
                    aux = self._primeiro
                    perc.proximo = aux.proximo
                    aux = None
        self._tamanho -= 1
        return True

    def get_index(self,indice):
        if self._tamanho <= indice:
            return None
        else:
            perc = self._primeiro
            for i in range(self._tamanho-1):
                if i == indice:
                    return perc.dado
                else:
                    perc = perc.proximo

    def __str__(self):
        perc = self._primeiro
        dado = '['
        while perc != None :
            dado += str(perc.dado) + ' ,'
            perc =  perc.proximo

        dado = dado.strip(', ')
        dado += ']'
        return dado

    def __repr__(self):
        return self.__str__()

    def is_empty(self):
        return self._tamanho == 0