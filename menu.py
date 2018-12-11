from AED26 import *
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
            indice = int(input("Informe o indice >> "))
            analisa_nota(lista_alunos,indice)
        elif op == '3':
            listar_alunos(lista_alunos)
        elif op == '4':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")
main()