# 01 - Crie duas variáveis em que A - 10 e B = 20
# em seguida faça A = B e B = A
# de modo a obter os resultados finais A = 20 e B = 10.

#usuario_1 = "Jose Caetano da Silva"
#usuario_2 = "Maria Souza Lemos"
#usuario_coringa = usuario_1

#usuario_1 = usuario_2
#usuario_2 = usuario_coringa

#print(usuario_1)
#print(usuario_2)



# 02 - Crie uma função que recebe um valor e retorna a
# informação dizendo se é um valor positivo, negativo ou nulo

#numero = float(input("Digite aqui o número: "))

#def verificacao_numero():
#    if numero > 0:
#        return 'O número é positivo'
#   elif numero < 0:
#        return "O número é negativo"
#    elif numero == 0:
#        return 'O número é nulo'
#    else:
#        return "valor inválido"

#print(verificacao_numero())


# 03 - O custo de um carro novo ao consumidor é a soma do custo de
# fábrica com a porcentagem do distribuidor e dos impostos
# (aplicados ao custo de fábrica). Supondo que o percentual do
# distribuidor seja de 28% e os impostos de 45%, escrever um
# algoritmo para ler o custo de fábrica de um carro,
# calcular e escrever o custo final ao consumidor.

#def calcular_custo(custo_fabrica):
#    imposto_distribuidor = custo_fabrica *0.28
#    imposto_geral = custo_fabrica*0.45
#    custo_total = custo_fabrica + imposto_distribuidor + imposto_geral
#   return custo_total

#print(calcular_custo(10000))



# 04 - Crie uma função que ler o nome de 2 times e o
# numero de gols marcados na partida (para cada time);
# Escrever o nome do vencedor. Caso não haja vencedor,
# deverá ser impressa a palavra EMPATE.

def calcula_resultado_partida(time1, time2, qtd_gols_time1, qtd_gols_time2):
    if qtd_gols_time1 > qtd_gols_time2:
        return 'O time 1 venceu'
    elif qtd_gols_time2 > qtd_gols_time1:
        return 'O time 2 venceu'
    else:
        return 'Os times empataram'...
    