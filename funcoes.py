def arqLista(arquivo):
    file = open(arquivo, "r")
    lista = file.readlines()
    for i in range(len(lista)):
        lista[i] = lista[i][:-1]
    file.close()
    return lista

def regravar(arquivo, lista):
    arq = open(arquivo, "w")
    for linha in lista:
        arq.write(linha+"\n")
    arq.close()

def separar(lista, posicao, pulo):
    novalista = []
    for i in range(posicao, len(lista), pulo):
        novalista.append(lista[i])
    return novalista

def larguraDaColuna(lista):
    maior = len(lista[0])
    for opcao in lista[1:]:
        if maior < len(opcao):
            maior = len(opcao)
    if maior % 2 != 0:
        maior += 1
    return maior

def palavraEspaco(palavra, largura):
    espacos = (largura-len(palavra))*" "
    return palavra + espacos

def centralizarPalavra(palavra, largura):
    if len(palavra) % 2 != 0:
        palavra += " "
    espaco = int((largura - len(palavra))/2)*" "
    return espaco + palavra + espaco

def menu(lista):
    larg = larguraDaColuna(lista)
    print("﻿╔═══","═"*larg,"═══╗", sep = "")
    print("║   ", centralizarPalavra(lista[0], larg),"   ║", sep="")
    print("╠═══╦", larg*"═","══╣", sep = "")
    num = 1
    for i in lista[1:]:
        print("║ ", num," ║ ", palavraEspaco(i, larg) , " ║",sep = "")
        print("╠═══╬", larg*"═","══╣", sep = "")
        num+=1
    print("║ ", len(lista)," ║ ", palavraEspaco("Sair", larg)," ║", sep = "")
    print("╚═══╩", larg*"═","══╝", sep = "")
    print("Digite o nº correspondente a opção desejada.")
    escolha = input(">>>")
    return escolha

def minitabela(nome):
    larg = 40
    print("╔","═"*larg,"╗",sep = "")
    print("║", centralizarPalavra(nome, larg),"║", sep = "")
    print("╚", larg*"═","╝", sep = "")

def cls():
    for i in range(50):
        print()
        
def codigodacomida():
    while True:
        codigo = input("Código: ").upper()
        if len(codigo) < 5:
            codigo = ((5 - len(codigo))*"0") + codigo
            break
        elif len(codigo) > 5:
            print("ERRO: O código deve ser composto por até 5 números")
        else:
            break
    return codigo

def codigo():
    lista = arqLista("cadastrodepratos.txt")
    code = codigodacomida()
    for i in range(0, len(lista), 4):
            if code == lista[i]:
                print("Código já cadastrado! Tente novamente!")
                code = codigodacomida()
            else:
                return code

def cardapio(arquivo, titulo):
    lista = arqLista(arquivo)
    larguranome = larguraDaColuna(separar(lista, 1, 4))
    larguravalor = 7
    larguratotal = larguranome + larguravalor
    print("╔═══════", "═"* larguratotal, "═══════╗", sep = "")
    print("║        ", centralizarPalavra( titulo, larguratotal),"       ║", sep="")
    print("╠═══════╦═","═"* larguranome,"═╦══════════╣", sep = "")
    for i in range(0,len(lista),4):
        print("║ ",lista[i]," ║ ",palavraEspaco(lista[i+1], larguranome)," ║ R$ %2.2f" %float(lista[i+2])," ║", sep = "")
        print("╠═══════╬═","═"*larguranome,"═╬══════════╣", sep = "")
    print("╚═══════╩═","═"*larguranome,"═╩══════════╝", sep = "")
    print("Para mais detalhes sobre os pratos, digite abaixo o seu código.")
    print("Para voltar ao menu inicial, digite 0.")
    while True:
        codigo = input(">>>")
        if codigo == "0":
           cls()
           break
        elif codigo not in separar(lista, 0, 4):
                print("ERRO - Código não encontrado. Tente Novamente.")
        for i in range(len(lista)):
            if codigo == lista[i]:
                print(lista[i+3])
                
def cadastrar():
    minitabela("CADASTRAR PRATO")
    print("Favor inserir as seguintes informações:")
    arquivo = open("cadastrodepratos.txt", "a")
    arquivo.write(codigo()+"\n")
    arquivo.write(input("Nome: ")+"\n")
    arquivo.write(input("Valor: ")+"\n")
    arquivo.write(input("Descrição: ")+"\n")
    arquivo.close()
    cls()
    print("Cadastrado com sucesso!")

def deletar():
    arquivo = "cadastrodepratos.txt"
    lista = arqLista(arquivo)
    minitabela("DELETAR PRATO")
    while True:
        codigo = input("Digite o codigo: ")
        if codigo not in lista:
            print("ERRO - Código não encontrado. Verifique o código e tente novamente!")
        else:
            for i in range(0,len(lista)-1,4):
                if codigo == lista[i]:
                    print("Código: %s" %lista[i], "Nome: %s" %lista[i+1], "Valor: %s" %lista[i+2], "Descrição: %s" %lista[i+3], sep = "\n")
                    print("Deseja realmente apagar o prato? [s/n]")
                    opcao = input(">")
                    if opcao == "s":
                        lixo = open("lixeira.txt", "a")
                        for x in range(4):
                            lixo.write(lista[i]+"\n")
                            del lista[i]
                        cls()
                        print("Deletado com sucesso!")
                        lixo.close()
                        break
            break
        regravar(arquivo,lista)
        
        
    
def opcaoalterar():
    while True:
        form = input(">")
        if form == "0":
            print("Digite o novo ", end = "")
            nova = codigodacomida()
            break
        elif form == "1":
            nova = input("Digite o novo nome: ")
            break
        elif form == "2":
            nova = input("Digite o novo valor: ")
            break
        elif form == "3":
            nova = input("Digite a nova descrição: ")
            break
        else:
            print("Opção inválida, tente novamente.")
    return [int(form), nova]

def alterar():
    minitabela("ALTERAR PRATO")
    arquivo = "cadastrodepratos.txt"
    lista = arqLista(arquivo)
    while True:
        codigo = input("Digite o código atual: ")
        if codigo not in lista:
            print("ERRO - Código não encontrado. Verifique o código e tente novamente!")
        else:
            for i in range(len(lista)-1):
                if codigo == lista[i]:
                    print("0 - Código: %s" %lista[i], "1 - Nome: %s" %lista[i+1], "2 - Valor: %s" %lista[i+2], "3 - Descrição: %s" %lista[i+3], sep = "\n")
                    print("\nO que deseja alterar?[0,1,2,3]")
                    novas = opcaoalterar()
                    i2 = novas[0]
                    novo = novas[1]
                    lista[i+i2] = novo
                    cls()
                    print("Alterado com sucesso!")  
                    break
        regravar(arquivo,lista)
        break        
    
