def tamanho(lista):
    maior = len(lista[0])
    if maior % 2 != 0:
        lista[0]+= " "
    for cada in lista[1]:
        if len(cada) > maior:
            maior = len(cada)
    if maior % 2 != 0:
        maior += 1
    if maior < 30:
        maior = 30
    return maior

def esp(nome, tam):
    tama = tam - len(nome)
    return nome + " "*tama

def menu(lista):
    tam = tamanho(lista)
    print(tam)
    print("﻿╔═══","═"*tam,"═══╗", sep = "")
    print("║   "," "*int((tam-len(lista[0]))/2), lista[0], " "*int((tam-len(lista[0]))/2), "   ║", sep = "")
    print("╠═══╦", tam*"═","══╣", sep = "")
    for i in range(len(lista[1])):
        print("║ ", i+1," ║ ", esp(lista[1][i], tam)," ║", sep = "")
        print("╠═══╬", tam*"═","══╣", sep = "")
    print("║ ", i+1," ║ ", esp("Sair", tam)," ║", sep = "")   
    print("╚═══╩", tam*"═","══╝", sep = "")

mn = ["MENU", ["Cadápio", "Pedido", "Produtos", "Relatórios"]]
menu(mn)

