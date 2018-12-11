from Listas_AED.lista import Nó
#sequencial = []
#sequencial.append(7)
class lista_encadeada:
    def __init__(self):#criando a lista sempre vazia
        self.cabeça = None  #referencia para o primeiro nó
        self._tamanho = 0 #tamanho da lista, para cntabilizar os nós

    def append(self,elemento):#adicionar ao final da lista,existe dois casos possiveis ------- complexidade o(n)
        if self.cabeça:#há algum elemento
            ponteiro = self.cabeça# os dois estão apontamdo para o mesmo espaço de memeoria
            while(ponteiro.proximo): #enquanto o ponteiro tiver um proximo nó
                ponteiro = ponteiro.proximo # proximo nó
            ponteiro.proximo = Nó(elemento) #chegou no ultimo elemento

        else:#inserindo o primeiro elemento na lista
            #primeira inserção
            self.cabeça = Nó(elemento)
        self._tamanho = self._tamanho + 1

    def __len__(self):#define o que vai acontecer e retorna um numero inteiro
        return self._tamanho#retorna o tamanho da lista

    def _get_nó(self,indice): #acessar elementos da lista
        # a = lista.get(6)
        ponteiro = self.cabeça  # percorredor da lista
        for i in range(indice):  # quantidade de execuções
            if ponteiro:  # verificar se é None
                ponteiro = ponteiro.proximo
            else:  # se for None
                raise IndexError("List index out of range")#tratando a exeção
        return ponteiro

    def set(self,item, elemento):# modificar um indice da lista
        #lista.set(5,9)
        pass

    def __getitem__(self, indice):#recuperar um valor-------------- complexidade O(n)
        #a = lista[6]
        #a = lista.get(6)
        ponteiro = self._get_nó(indice)#percorredor da lista
        #verificar ponteiro
        if ponteiro:# se não tiver no vazio
            return ponteiro.dado #posição do ponteiro
        # se tiver no vazio
        else:
            raise IndexError("List index out of range")  # tratando a exeção

    def __setitem__(self, indice, elemento):#modificar-----------complexidade O(n)
        #lista[5] = 9
        #lista.set(5,9)
        ponteiro = self._get_nó(indice)  # percorredor da lista
        # verificar ponteiro
        if ponteiro:  # se não tiver no vazio
            ponteiro.dado = elemento #modificar posição do ponteiro
        # se tiver no vazio
        else:
            raise IndexError("List index out of range")  # tratando a exeção

    def busca(self,elemento):# buscar elemento da lista, retorna seu indice
        ponteiro = self.cabeça # variavel auxilia
        i = 0
        while(ponteiro):# percorrer enquanto tiver um nó valido
            if ponteiro.dado == elemento:#verificar se o dado do ponteiro é igual ao o elemento que procuro
                return i
            # se nao for igual
            ponteiro = ponteiro.proximo #avança para o proximo nó para continuar a busca
            i += 1
        raise ValueError("{} is not in list".format(elemento))


    def inserir(self,indice,elemento):#inserir na lista
        novo_no = Nó(elemento)
        if indice == 0:#inserir no inicio da lista
            Nó.proximo = self.cabeça
            self.cabeça = novo_no
        else:
            #inserir no final da lista
            ponteiro = self._get_nó(indice-1)
            novo_no.proximo = ponteiro.proximo
            ponteiro.proximo = novo_no

        self._tamanho = self._tamanho + 1#aumentar tamanho da lista

    def remover(self,elemento):
        if self.cabeça == None:
            raise ValueError("{} is not in list".format(elemento))
        elif self.cabeça.dado == elemento:
            self.cabeça = self.cabeça.proximo
            self._tamanho = self._tamanho - 1  # aumentar tamanho da lista
            return True
        else:
            antecessor = self.cabeça
            ponteiro = self.cabeça
            while(ponteiro):
                if ponteiro.dado == elemento:
                    antecessor.proximo = ponteiro.proximo
                    ponteiro.proximo = None
                antecessor = ponteiro
                ponteiro = ponteiro.proximo
            self._tamanho = self._tamanho - 1  # aumentar tamanho da lista
            return True
        raise ValueError("{} is not in list".format(elemento))

    def __str__(self):
        pass