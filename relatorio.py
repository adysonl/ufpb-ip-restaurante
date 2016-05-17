dados = open("postdata.ads", "r")
lista = dados.readlines()
print("Relatório do Posto")
for i in range(0,len(lista)-1,5):
    print("Dia",
          "\nValor Inicial:", lista[i],
          "Valor Final:", lista[i+1],
          "Valor Unitário: R$", lista[i+3],
          "Total em Dinheiro: R$", lista[i+4])


    
    
