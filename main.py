"""
Questão 01
Usuário tiver mais de 18 (mensagem) - Usuário menor de 18 (mensagem)

idade = 20

if idade >= 18:
    print("Você é maior de idade, portanto, pode passar!")

else:
    print("Você é menor de idade, portanto, proibido passar!")
"""
"""

Questão 02
Usuário tiver mais de 18 (mensagem) - Usuário menor de 18 (mensagem) - Usuário negativo (mensagem)
idade = 10

if(idade >=18):
    print("Você é maior de idade, portanto, pode passar!")

elif idade < 0:
    print("Você colocou um número inválido, tente novamente!")

else:
    print("Você é menor de idade, portanto, proibido passar!")

"""
"""
Questão 03
Usuário tiver mais de 18 (mensagem) - Usuário menor de 18 (mensagem) - Usuário negativo (mensagem) - Usuário menor que 18 e maior que 16 (mensagem)

idade = 2
acompanhante = True

if idade >= 18:
    print("Você é maior de idade, então, pode entrar!")

elif idade < 0:
    print("Valor inválido, insira novamente!")

elif 16 <= idade < 18 and acompanhante == True:
    print("Você é menor de idade, porém, está acopanhado. Portanto, pode entrar!")

elif 16 <= idade < 18 and acompanhante == False:
    print("Você é menor de idade e não está acompanhado. Logo, proibido entrar!")

else:
    print("Você é menor de idade, portanto, proibido entrar!")
"""

"""
Questão 04
Usuário tiver mais de 18 (mensagem) - Usuário menor de 18 (mensagem) - Usuário negativo (mensagem) - Usuário menor que 18 e maior que 16 (mensagem) -
Checar a idade do acompanhante, deve ser maior que 18 

idade = 17
acompanhante = True
idade_acompanhante = 10

if idade >= 18:
    print("Você é maior de idade, então, pode entrar!")

elif idade < 0:
    print("Valor inválido, insira novamente!")

elif 16 <= idade < 18 and acompanhante == True:

    if idade_acompanhante >= 18:
        print("Você é de menor e está acompanhado com um maior de idade. Portanto, podem entrar!")

    else:
        print("Você é de menor e está acompanhado com um de menor também. Portanto, proibido entrar!")

elif 16 <= idade < 18 and acompanhante == False:
    print("Você é menor de idade e não está acompanhado. Logo, proibido entrar!")

else:
    print("Você é menor de idade, portanto, proibido entrar!")
"""