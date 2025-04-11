def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b

def calcular(operacao, a, b):
    if operacao == "soma":
        return somar(a, b)
    elif operacao == "subtrai":
        return subtrair(a, b)
    elif operacao == "multiplica":
        return multiplicar(a, b)
    elif operacao == "divide":
        return dividir(a, b)
    else:
        raise ValueError("Operação inválida")
