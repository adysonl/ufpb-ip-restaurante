def tamanho(lista): #recebe uma lista com padrão [titulo[opcao1, opcao2, ...]]
    maior = len(lista[0]) #maior = tamanho do titulo
    if maior % 2 != 0: # se o tamanho do titulo for impar
        lista[0]+= " " # adicionar 1 espaço ao titulo
    for cada in lista[1]: # p/ cada opção
        if len(cada) > maior: #se o tamanho da opcao for maior que 'maior'
            maior = len(cada) # maior vai ser igual ao tamanho da opcao
    if maior % 2 != 0: #se maior for ímpar
        maior += 1 # adiciona 1 para ficar par
    if maior < 30: #se o maior for menor que 30(tamanho minimo)
        maior = 30 #maior = 30
    return maior #retorna o tamanho da maior palavra ou o tam minimo

def esp(nome, tam): #recebe uma palavra e o tamanho da tabela
    tamanho = tam - len(nome) #subtrai o tamanho da palavra do tamanho da tabela
    return nome + " "*tamanho #retorna a palavra + o resto da subração em espaços

def menu(lista): #recebe uma lista
    tam = tamanho(lista) # chama a funçao tamanho para definir o tamanho da tabela
    
    print("﻿╔═══","═"*tam,"═══╗", sep = "")
    etitulo = int((tam-len(lista[0]))/2)*" " #margens do titulo = tamanho da tabela menos o tamanho do titulo, divididos por 2, em espaços
    print("║   ", etitulo, lista[0], etitulo, "   ║", sep = "")
    print("╠═══╦", tam*"═","══╣", sep = "")
    for i in range(len(lista[1])): #para cada indice de opção
        print("║ ", i+1," ║ ", esp(lista[1][i], tam)," ║", sep = "")
        print("╠═══╬", tam*"═","══╣", sep = "")
    print("║ ", len(lista[1])+1," ║ ", esp("Sair", tam)," ║", sep = "") # o indice do sair = tamanho da lista + 1   
    print("╚═══╩", tam*"═","══╝", sep = "")

#para teste
mn = ["MENNU", ["Cadápio", "Pedido", "Produtos", "Relatórios"]]
menu(mn)
