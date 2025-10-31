# Crie uma função que ler 3 valores (A,B,C)
# representando as medidas dos lados de um triângulo
# e escrever se formam ou não um triângulo.
# OBS: para formar um triângulo, o valor de cada lado deve ser menor
# que a soma dos outros 2 lados.

import math

A = 4
B = 5
C = 5

def verifica_triangulo(A, B, C):
    if A < B + C and B < A + C and C < A + B:
        print("Essa figura forma um triângulo")

        if A != B and A != C and C != B:
            print("Forma um triângulo Escaleno")
            s = (A + B + C) / 2
            area = math.sqrt(s * (s - A) * (s - B) * (s - C))
            print(f"A área do triângulo é: {area}")

        elif A == B == C:
            print("Forma um triângulo Equilátero")
            area = (math.sqrt(3)*pow(A,2))/4
            print(f"A área do triângulo é: {area}")

        else:
            print("Forma um triângulo Isosceles")
            if (A == B):
                base = C/2
                altura = math.sqrt(base**2 + A**2)
                area = (C * altura) / 2
                print(f"O valor da área é: {area}")

            elif (A == C):
                base = B/2
                altura = math.sqrt(base**2 + A**2)
                area = (B * altura) / 2
                print(f"O valor da área é: {area}")

            elif (B == C):
                base = A/2
                altura = math.sqrt(base**2 + B**2)
                area = (A * altura) / 2
                print(f"O valor da área é: {area}")
    else:
        print("Essa figura não forma um triângulo")

verifica_triangulo(A, B, C)