# Carlos está desenvolvendo um conversor de temperaturas
# Crie um programa que receba uma temperatura em graus Celsius 
# digitada pelo usuário e converta para Fahrenheit ou o contrário.
# Celsius para Fahrenheit => (celsius * 9/5) + 32
# Fahrenheit para Celsius => (fahrenheit - 32) * 5/9

# escolha = float(input("Você quer converter de Celsius para Fahrenheit [1] ou Fahrenheit para Celsius [2]? "))

# if escolha == 1:

#     valor_celsius = float(input("Qual o valor desejado para transformar em Fahrenheit? "))
#     resultado_para_fah = float(valor_celsius * 9/5) + 32

#     print(f"O valor {valor_celsius}°C para Fahrenheit é {resultado_para_fah}")

# elif escolha == 2:

#     valor_fahrenheit = float(input("Qual o valor desejado para transformar em Celsius? "))
#     resultado_para_cel = float(valor_fahrenheit - 32) * 5/9

#     print(f"O valor {valor_fahrenheit}°F para Celsius é {resultado_para_cel}")

# else:
#     print("Esse valor é inválido, tente novamente!")

# ---------------------------------------------------------------------------------

# Uma loja online cobra frete com base na distância até o cliente.
# Crie um programa que pergunte:
    # A distância (em km) até o endereço do cliente
    # O peso da encomenda (em kg)
# E aplique as seguintes regras:
    # Se a distância for até 100 km, o frete base é de R$ 10,00;
    # Senão, é R$ 20,00
    # Para cada quilo acima de 5 kg, cobra-se R$ 2,00 adicionais
    # Se o item for frágil, aumentar 10 reas no frete
    # Se o item for perecível, enviar mensagem negando a realização da entrega.
# Ao final, exiba o valor do frete.

distancia = float(input("Qual a distância (em km) até o endereço do cliente? "))
peso = float(input("Qual o peso da encomenda (em kg)? "))
fragilidade = input....

if distancia <= 100:
    frete_distancia = float(10)
    print(f"Como a distância é menor que 100km, o valor adicional da distância é {frete_distancia}")
    
    if peso > 5:
        print(f"Logo, com os adicionais do peso, o valor total a ser pago é de: ", 10 + (peso-5) *2)

else:
    frete_distancia = float(20)

    print(f"Como a distância é maior do que 100km, o valor adicional da distância é {frete_distancia}")
    
    if peso > 5:
        print(f"Logo, com os adicionais do peso, o valor total a ser pago é de: ", 20 + (peso-5) *2)


