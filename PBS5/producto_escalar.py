def capturar_vector(tamano):
    vector = []
    print(f"Introduce los {tamano} elementos del vector:")
    for i in range(tamano):
        valor = float(input(f"Elemento {i+1}: "))
        vector.append(valor)
    return vector

def producto_escalar(vector1, vector2):
    producto = 0
    for i in range(len(vector1)):
        producto += vector1[i] * vector2[i]
    return producto

tamano = int(input("Introduce el tamaño de los vectores: "))
print("Captura del primer vector:")
vector1 = capturar_vector(tamano)

print("\nCaptura del segundo vector:")
vector2 = capturar_vector(tamano)
resultado = producto_escalar(vector1, vector2)
print(f"\nEl producto escalar de los vectores es: {resultado}")