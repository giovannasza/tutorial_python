
def maior_de_50(lista):
    count = 0 # contador
    for l in lista:
        if l['idade'] > 50:
            count += 1

    return count

def mais_2000(lista):
    count = 0 # contador
    total_registros = len(lista)
    
    for l in lista:
        if float(l['salario']) > 2000:
            count += 1

    # porcentagem é uma regra de 3, logo
    # total_registros = 100% e count = X%
    # x = count * 100/total_registros
    x = count * 100/total_registros

    return (count, x, total_registros)

def maior_salario(lista, maior=None):
    """
    maior: é o maior salário para fim de comparação
    se usuário quiser saber o 2 maior por exemplo
    precisa passar o salário maior que o segundo
    """
    pessoa = None # pessoa que recebe maior salário
    for l in lista:
        if maior:
            if pessoa == None:
                pessoa = l # primeira pessoa é maior salario
            elif float(l['salario']) > float(pessoa['salario']) and float(l['salario']) < maior: # se o salário da lista for maior que o anterior
                pessoa = l # atualiza pessoa
        else:
            if pessoa == None:
                pessoa = l # primeira pessoa é maior salario
            elif float(l['salario']) > float(pessoa['salario']): # se o salário da lista for maior que o anterior
                pessoa = l # atualiza pessoa

    return pessoa

def media_profissoes(lista):
    # Preciso criar uma estrutura que armazene o somatório de salarios e a quantidade
    # de pessoas trabalhando nessa profissão
    profissoes = {} # armazena as profissões, técnico: {"qtd":11, "soma": 10393.99, media}, arquiteto: {"qtd":8, "soma": 1393.99}
    for l in lista:
        if l['profissao'] not in profissoes: # se 'Técnico" não existe em profissoes
            soma = float(l['salario'])
            media = float(l['salario'])
            dado = {"qtd":1, "soma": soma, "media": media }
            profissoes[l['profissao']] = dado # cria uma nova chave com o nome da profissão

        else:
            qtd = profissoes[l['profissao']]['qtd'] + 1 # incrementa quantidade
            soma += float(l['salario']) # somana os salários
            media = soma/qtd # faz a média aritimética
            dado = {"qtd": qtd, "soma": soma, "media": media } # atualiza valores
            profissoes[l['profissao']] = dado

    return profissoes
    

def formato_moeda(valor):
    valor = "R$ {:.2f}".format(valor)
    # troca ponto por virgula
    valor = valor.replace(".", ",")
    return f"{valor}"

def filtrar(lista, salario_de=None, sexo=None):
    """
    Retorna uma nova lista somente com quem ganha mais de 2000
    sexo: Masculino ou Feminino
    """
    nova_lista = []
    for l in lista:
        if salario_de and float(l["salario"]) > salario_de:
            nova_lista.append(l)
        elif sexo and l["sexo"] == sexo:
            nova_lista.append(l)

    return nova_lista 

def maior_2000_sexo(lista, sexo='Masculino'):
    """
    lista: lista de dados
    sexo: sexo F ou M
    Para não ficar complexo é melhor fazer um filtro
    """
    lista = filtrar(lista, salario_de=2000) # somente quem ganha mais de 2000, para economizar um if
    lista = filtrar(lista, sexo=sexo) # filtra novamente por sexo
    menor_idade=0
    maior_idade = 0
    for l in lista:
        if menor_idade == 0: # a menor idade é sempre a primeira
            menor_idade = l["idade"]
        elif l['idade'] < menor_idade:
            menor_idade = l['idade']
        
        # precisa comparar a maior idade agora
        if maior_idade == 0:
            maior_idade = l["idade"]
        elif l['idade'] > maior_idade:
            maior_idade = l['idade']
    return (menor_idade, maior_idade)