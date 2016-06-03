def arqLista(arquivo):
    file = open(arquivo, "r")
    lista = file.readlines()
    for i in range(len(lista)):
        lista[i] = lista[i][:-1]
    file.close()
    return lista

def separar(lista, posicao, pulo):
    novalista = []
    for i in range(posicao, len(lista), pulo):
        novalista.append(lista[i])
    return novalista

def cardapio():
    lista = arqLista("cadastrodepratos.txt")
    larguranome = larguraDaColuna(separar(lista, 1, 4))
    larguravalor = 7
    larguratotal = larguranome + larguravalor
    print("╔═══════", "═"* larguratotal, "═══════╗", sep = "")
    print("║        ", centralizarPalavra("CARDAPIO", larguratotal),"       ║", sep="")
    print("╠═══════╦═","═"* larguranome,"═╦══════════╣", sep = "")
    for i in range(0,len(lista),4):
        print("║ ",lista[i]," ║ ",palavraEspaco(lista[i+1], larguranome)," ║ R$ %2.2f" %float(lista[i+2])," ║", sep = "")
        print("╠═══════╬═","═"*larguranome,"═╬══════════╣", sep = "")
    print("╚═══════╩═","═"*larguranome,"═╩══════════╝", sep = "")
    print("Para mais detalhes sobre o prato, digite abaixo o seu código.")
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
def cls():
    for i in range(50):
        print()
        
def codigodacomida():
    while True:
        codigo = input("Código: ")
        if len(codigo) < 5:
            codigo = ((5 - len(codigo))*"0") + codigo
            break
        if len(codigo) > 5:
            print("ERRO: O código deve ser composto por até 5 números")
        if len(codigo) == 5:
            break
    return codigo

def cadastrar():
    arquivo = open("cadastrodepratos.txt", "a")
    arquivo.write(input("Descreva o prato: ")+"\n")
    arquivo.write(input("Nome: ")+"\n")
    arquivo.write(input("Valor: ")+"\n")
    arquivo.write(porcao()+"\n")
    arquivo.close()

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
