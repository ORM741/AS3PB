def es_conjunto_vacio(conjunto):
    return len(conjunto) == 0

conjunto1 = set()
conjunto2 = {1, 2, 3}

print(f"¿El conjunto1 está vacío? {es_conjunto_vacio(conjunto1)}")
print(f"¿El conjunto2 está vacío? {es_conjunto_vacio(conjunto2)}")