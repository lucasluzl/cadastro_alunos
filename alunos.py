import os

alunos = []

def cadastro():
    os.system("cls")
    aluno = input("Insira o nome do aluno:")
    alunos.append(aluno)
    print(f"O {aluno} foi cadastrado com sucesso!")

def listar():
    os.system("cls")
    for i in enumerate(alunos):
        print(i)

while True:
    print("\n\n\n")
    print("Cadastro de Alunos \n")

    print("1 - Cadastrar Alunos")
    print("2 - Listar Alunos")
    print("1 - Sair")

    opcoes = int(input("Insira a opção desejável:"))

    if opcoes == 1:
        cadastro()

    elif opcoes == 2:
        listar()

    elif opcoes == 3:
        print("Saindo do sistema...")
        break

    else:
        print("Insira um valor válido.")