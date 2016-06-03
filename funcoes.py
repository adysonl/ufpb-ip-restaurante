def arqLista(arquivo):
    file = open(arquivo, "r")
    lista = file.readlines()
    for i in range(len(lista)):
        lista[i] = lista[i][:-1]
    file.close()
    return lista

def cardapio():
    lista = arqLista("cadastrodepratos.txt")
    larg = larguraDaColuna(lista)
    
    for i in range(0,len(lista),4):
            

def cls():
    for i in range(50):
        print()
        
def porcao():
    print("Digite as porções que vem no prato [para finalizar digite 0]")
    porcao = ""
    while True:
        entrada = input(">>>")
        if entrada == "0":
            break
        porcao +=entrada+", "
    return porcao

def cadastrar():
    arquivo = open("cadastrodepratos.txt", "a")
    arquivo.write(input("Código: ")+"\n")
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
