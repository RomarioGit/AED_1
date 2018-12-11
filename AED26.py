
class aluno:
    def __init__(self,nome,cpf,nota):
        self.nome = nome
        self.cpf = cpf
        self.nota = nota

    def get_nota(self):
        if not self.nota == 0:
            return True
        return False

def cadastrar_aluno(lista_alunos):
    nome = input("Informe o nome: ")
    cpf = input("Informe o CPF: ")
    nota = float(input("Informe a Nota: "))
    alunos = aluno(nome,cpf,nota)
    lista_alunos.append(alunos)

lista_alunos = []


def listar_alunos(lista_alunos):
    for i in range(len(lista_alunos)):
        print('Aluno:{}'.format(i))
        print("Nome:{}".format(lista_alunos[i].nome))
        print("CPF:{}".format(lista_alunos[i].cpf))
        if lista_alunos[i].get_nota():
            print("Nota: {}".format(lista_alunos[i].nota))



def menu():
    print("-----MENU------")
    print("1-Cadastrar Aluno;")
    print('2-Analisar Nota;')
    print("3-Listar  Alunos;")
    print("4-Sair;")


def main():
    while True:
        menu()
        op = input("Opção>> ")
        if op == '1':
            cadastrar_aluno(lista_alunos)
        elif op == '2':
            analisa_nota(lista_alunos)
        elif op == '3':
            listar_alunos(lista_alunos)
        elif op == '4':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")



main()