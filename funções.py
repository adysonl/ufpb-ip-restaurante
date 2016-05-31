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
