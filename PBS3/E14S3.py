def evaluar_polinomio(coeficientes, x):
    resultado = 0
    grado = len(coeficientes) - 1 
    for i, coef in enumerate(coeficientes):
        resultado += coef * (x ** (grado - i))
    return resultado
coeficientes = [2, -3, 0, 5]
x = 2
valor_polinomio = evaluar_polinomio(coeficientes, x)

print(f"El valor del polinomio en x = {x} es {valor_polinomio}")