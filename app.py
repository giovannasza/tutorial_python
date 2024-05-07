from flask import Flask, jsonify
from funcoes import maior_de_50
from randon_data import *
from funcoes import *
from funcoes import *
from funcoes import *
from funcoes import *


app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"status": 200, "message": "API da Giovanna De Souza Nunes"})
@app.route("/aleatorios")
def aleatorios():
    import random
    a = random.randint(49, 100)
    return jsonify({"status": 200, "data": a})

@app.route("/argumentos/<string:nome>")
def argumentos(nome: str):
    return jsonify({"status": 200, "data": nome})
# Dados das pessoas


# Rota para contar pessoas com mais de 50 anos
@app.route('/A', methods=['GET'])
def contar_pessoas_maiores_de_50_route():
    contador = maior_de_50(pessoas)
    return jsonify({'quantidade': contador})


# Rota para contar pessoas que ganham mais de R$ 2000 e calcular a porcentagem
@app.route('/B', methods=['GET'])
def contar_pessoas_mais_de_2000_route():
    count, porcentagem, total_registros = mais_2000(pessoas)
    return jsonify({'quantidade': count, 'porcentagem': porcentagem, 'total_registros': total_registros})

# Função para encontrar o menor salário entre as três pessoas com os maiores salários
def salario_mais_baixo(lista):
    if len(lista) < 3:
        return None
    return min(pessoa['salario'] for pessoa in lista)

# Rota para retornar as 3 pessoas com maiores salários
@app.route('/C', methods=['GET'])
def obter_tres_maiores_salarios():
    tres_maiores_salarios = []
    for _ in range(3):
        pessoa = maior_salario(pessoas, maior=salario_mais_baixo(tres_maiores_salarios))
        tres_maiores_salarios.append(pessoa)

    return jsonify(tres_maiores_salarios)

# Rota para retornar a média salarial de cada profissão
@app.route('/D', methods=['GET'])
def calcular_media_salarial_por_profissao():
    medias = media_profissoes(pessoas)
    return jsonify(medias)

# Rota para retornar o intervalo da maioria das idades e o sexo de quem ganha mais de R$ 2000
@app.route('/E', methods=['GET'])
def calcular_intervalo_idades_e_sexo():
    intervalo_idades, sexo = maior_2000_sexo(pessoas)
    return jsonify({'intervalo_idades': intervalo_idades, 'sexo': sexo})



if __name__ == '__main__':
    app.run(debug=True)
