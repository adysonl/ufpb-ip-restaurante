import funcoes as f

opcoes = ["Restaurante Brizolinha", "Cadastrar Prato", "Ver Pratos", "Alterar Prato", "Deletar Pratos", "Lixeira"] 
while True:
    escolha = f.menu(opcoes)
    f.cls()
    if escolha == "6":
        print("Obrigado, volte sempre.")
        break
    elif escolha == "1":
        f.cadastrar()
    elif escolha == "2":
        f.cardapio("cadastrodepratos.txt", "CADASTRO")
    elif escolha == "3":
        f.alterar()
    elif escolha == "4":
        f.deletar()
    elif escolha == "5":
        f.cardapio("lixeira.txt", "LIXEIRA")
    else:
        print("Opção Inválida. Tente Novamente.")
