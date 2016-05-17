bombafinal = int(input("Digite: "))


dados = open("postdata.ads", "r")
lista = dados.readlines()
bombainicial = lista[-1][0:-1]
lista.append(str(bombafinal)+"\n")
ttllitros = int(bombafinal)-int(bombainicial)
lista.append(str(ttllitros)+"\n")
unitario = float(input("Digite o Valor Unitário: "))
lista.append(str(unitario)+"\n")
lista.append(str(ttllitros*unitario)+"\n")
bombainicial = int(bombafinal)
lista.append(str(bombainicial)+"\n")
dados.close()

dados = open("postdata.ads", "w")
for i in range(len(lista)):
    x = str(lista[i])
    dados.write(x)
dados.close()

print(lista)
