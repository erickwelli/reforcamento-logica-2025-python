#01 Um estacionamento com cobra R$ 4 por hora nas primeiras 2 horas e R$ 3 por hora nas demais
# Elabore um algoritmo que:
# Peça a hora de entrada e a hora de saída (entre 0 e 23)
# Calcule o valor total a pagar
# Valide a entreada (asaaída não pode ser inferior à entrada)
# Exiba uma mensagem como: "Permanência de X horas. Total a pagar? R$ Y."

def reconhecer_hora():
    entrada = int(input('Qual é a hora de entrada? '))
    if entrada < 0 or entrada > 23:
        print('Você inseriu uma hora inválida!')
    else:
        saida = int(input('Qual é a hora de saída? '))
        return calcula_estacionamento(entrada, saida)


def calcula_estacionamento(entrada, saida):
    if entrada > saida:
        print('Você inseriu os parâmetros incorretamente!')
        return
    if entrada > 23 or entrada < 0 or saida < 0 or saida > 23:
        print('Você inseriu uma hora inválida!')
        return

    diferenca_horario = saida - entrada
    if diferenca_horario <= 2:
        valor = 4 * diferenca_horario
        return valor
    else:
        valor = 3 * (diferenca_horario-2) + 8
        return valor

print(reconhecer_hora())
