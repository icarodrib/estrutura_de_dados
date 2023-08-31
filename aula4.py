cartas = []
""" maxLenghtList = 3 """
# entrada de dados da quantidade
qtde = int(input("Declare quantas cartas pretende digitar: "))

# entrada de dados na lista
for i in range(qtde):
    cartas.append(int(input(f"Digite a carta Nº{i+1}: ")))

# imprimi as cartas digitadas
print("\nCartas na ordem de entrada:")
for i in range(qtde):
    print(f"A carta Nº{i+1} é:",cartas[i])

# ordenação das cartas
for i in range(qtde):
    for j in range(qtde-1):
        if cartas[j] > cartas[j+1]:
            cartas[j], cartas[j+1]=cartas[j+1], cartas[j]

# imprime as cartas ordenadamente
print("\nCartas ordem crescente:")
for i in range(qtde):
    print(f"A carta Nº{i+1} é:",cartas[i])