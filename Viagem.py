# Algoritmo para calcular o tempo de viagem com base na distância e velocidade fornecidas pelo usuário

# Solicita a distância e a velocidade de viagem ao usuário
distancia = float(input("Digite a distância a percorrer (em km): "))
velocidade = float(input("Digite a velocidade de viagem (em km/h): "))

# Calcula o tempo de viagem (tempo = distância / velocidade)
tempo = distancia / velocidade

# Exibe o tempo de viagem na tela
print(f"O tempo de viagem será de aproximadamente {tempo:.2f} horas.")