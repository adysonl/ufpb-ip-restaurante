import funcoes as f

opcoes = ["Restaurante Brizolinha", "Cadastrar Prato", "Ver Pratos", "Alterar Prato", "Deletar Pratos"] 
while True:
    escolha = f.menu(opcoes)
    f.cls()
    if escolha == "5":
        print("Obrigado, volte sempre.")
        break
    elif escolha == "1":
        f.cadastrar()
        f.cls()
    elif escolha == "2":
        f.cardapio()
    elif escolha == "3":
        f.alterar()
    elif escolha == "4":
        f.deletar()
    else:
        print("Opção Inválida. Tente Novamente.")
