import os

# Lista
nomes = []

while True:
    print(f"{"="*20} LISTA DE OPÇÕES {"="*20}\n")

    print("1 -Adicionar nome")
    print("2 - Visualizar os nomes que adicionei")
    print("3 - Sair")

    opcao = input("Informe a opção desejada: ")

    os.system("cls")

    match opcao:
        case "1":
            novo_nome = input(
                "Informe o nome o qual deseja adicionar: ").capitalize()
            nomes.append(novo_nome)
            os.system("cls")
        case "2":
            print(f"{"="*20} LISTA DE NOMES {"="*20}")
            for nome in nomes:
                print(nome)
        case "3":
            break
        case _:
            print("Opção inválida!")
