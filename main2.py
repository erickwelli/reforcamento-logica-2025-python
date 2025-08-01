"""
#01 - Utilizando if/else simular a operação de uma calculadora
deverá receber dois números e um operador
se o operador for + vai somar, se for - vai subtrair, se for * vai multiplicar e se for / vai dividir

valor1 = 10
valor2 = 2

operador = "/"

if operador == "+":
    soma = valor1 + valor2
    print("O resultado é:",soma)

elif operador == "-":
    subtracao = valor1 - valor2
    print("O resultado é:",subtracao)

elif operador == "*":
    multiplicacao = valor1 * valor2
    print("O resultado é:",multiplicacao)

elif operador == "/":
    divisao = valor1 / valor2
    print("O resultado é:",divisao)

else:
    print("Operador inválido, tente novamente.")
"""

"""
#02 - Utilizando if/else simular a operação de uma calculadora
deverá receber dois números e um operador
se o operador for + vai somar, se for - vai subtrair, se for * vai multiplicar e se for / vai dividir
validar se o divisor é igual a zero e colocar uma mensagem

valor1 = 10
valor2 = 2

operador = "/"

if operador == "+":
    soma = valor1 + valor2
    print("O resultado é:",soma)

elif operador == "-":
    subtracao = valor1 - valor2
    print("O resultado é:",subtracao)

elif operador == "*":
    multiplicacao = valor1 * valor2
    print("O resultado é:",multiplicacao)

elif operador == "/":
    if valor2 == 0:
        print("Não é possível dividir por zero")
    else:
        divisao = valor1 / valor2
        print("O resultado é:",divisao)
else:
    print("Operador inválido, tente novamente.")
"""

""" #03 -  Receber as notas dos 4 bimestres de um aluno, calcule a media e informe se ele está aprovado (>=60)
em recuperacao (media >=3 e media < 6) ou reprovado (media < 3)
"""
nota1 = 10
nota2 = 6
nota3 = 6
nota4 = 2

media = (nota1 + nota2 + nota3 + nota4) / 4

print(media)

if media >= 6:
    print("Aprovado")

elif 3 <= media < 6:
    print("Recuperação")

else:
    print("Reprovado")