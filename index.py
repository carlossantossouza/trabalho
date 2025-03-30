def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero"
    return a / b


print("Resultado da soma:", somar(5, 3))
print("Resultado da subtração:", subtrair(5, 3))
print("Resultado da multiplicação:", multiplicar(5, 3))
print("Resultado da divisão:", dividir(5, 0))
