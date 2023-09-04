# Input do valor das cartas pela quantidade de cartas
def declararCartas(quantidade):
    cartas = []
    for i in range(quantidade):
        cartas.append(int(input(f"Digite a carta Nº{i+1}: ")))
    return cartas

# Função para a ordenação das cartas
def ordenarCartas(quantidade,lista):
    for i in range(quantidade):
        for j in range(quantidade-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1]=lista[j+1], lista[j]
