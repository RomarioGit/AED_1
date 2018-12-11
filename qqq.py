class funcionario:
    def __init__(self,nome,cpf,fone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = fone

funcionarios = []
lista = []
def cadastrar_funcionario(lista):
    nome = input("Informe o nome: ")
    cpf = input("Informe o CPF: ")
    fone = input("Informe a telefone: ")
    funcionarios = funcionario(nome, cpf, fone)
    lista.append(funcionarios)
    print("Funcionário cadastrado")

def listar_todos(lista):
    for i in range(len(lista)):
        print("Funcionário {}".format(i))
        print("Nome: {}".format(lista[i].nome))
        print("CPF: {}".format(lista[i].cpf))
        print("Telefone: {}".format(lista[i].telefone))

def buscar_cpf(lista):
    cpf = input("CPF >> ")
    for funcionario in lista:
        if lista(funcionario[1]) == cpf:
            print("Funcionário {}".format(funcionario))
            print("Nome: {}".format(lista[funcionario].nome))
            print("CPF: {}".format(lista[funcionario].cpf))
            print("Telefone: {}".format(lista[funcionario].fone))
        else:
            print("Funcionário não cadastrado!")
def menu():
    print("---Menu---")
    print("1_Cadastrar Funcionário;")
    print("2-Listar Todos;")
    print('3-Buscar pelo cpf;')
    print("4-Sair;")

def main():
    while True:
        menu()
        op = input("Opção>> ")
        if op == '1':
            cadastrar_funcionario(lista)
        elif op == '2':
            listar_todos(lista)
        elif op == '3':
            buscar_cpf(lista)
        elif op == '4':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")


main()
