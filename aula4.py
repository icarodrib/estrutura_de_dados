# Importação da Biblioteca
from lib_aula4 import *

# ---Início do programa----------------------------------------------------------------------------------------------------------------------------------
cartas = []

# Declaração da quantidade de cartas
qtde = int(input("Declare quantas cartas pretende digitar: "))

# Declaração dos valores das cartas
cartas = declararCartas(qtde)

# Mostra as cartas na ordem em que foram digitadas
print("\nCartas na ordem em que foram digitadas: ")
for i in range(qtde):
    print(f"A carta Nº{i+1} é:",cartas[i])

# Chamada de função para realizar a ordenação
ordenarCartas(qtde,cartas)

# Mostra as cartas na ordem crescente
print("\nCartas na ordem crescente: ")
for i in range(qtde):
    print(f"A carta Nº{i+1} é:",cartas[i])

# PARA FAZER EM CASA:
# Fazer uma função para ordenar e outra para o usuario digitar os valores, fazer isso em uma biblioteca.