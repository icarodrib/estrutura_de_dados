# Função para a ordenação das cartas
def ordenar():
    for i in range(qtde):
        for j in range(qtde-1):
            if cartas[j] > cartas[j+1]:
                cartas[j], cartas[j+1]=cartas[j+1], cartas[j]

# ---Início do programa----------------------------------------------------------------------------------------------------------------------------------
cartas = []
""" maxLenghtList = 3 """
# Entrada da quantidade de cartas
qtde = int(input("Declare quantas cartas pretende digitar: "))

# Entrada de dados na lista
for i in range(qtde):
    cartas.append(int(input(f"Digite a carta Nº{i+1}: ")))

# Imprimi as cartas digitadas
print("\nCartas na ordem de entrada:")
for i in range(qtde):
    print(f"A carta Nº{i+1} é:",cartas[i])

# Chamada de função para realizar a ordenação
ordenar()

# Imprime as cartas ordenadamente
print("\nCartas na ordem crescente:")
for i in range(qtde):
    print(f"A carta Nº{i+1} é:",cartas[i])

# PARA FAZER EM CASA:
# Fazer uma função para ordenar e outra para o usuario digitar os valores, fazer isso em uma biblioteca.