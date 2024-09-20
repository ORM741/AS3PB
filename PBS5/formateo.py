def obtener_iniciales(nombre_completo):
    partes = nombre_completo.split()
    iniciales = ''.join([parte[0].upper() for parte in partes])
    
    return iniciales

nombre_completo = "Juan Pérez Gómez"
print(obtener_iniciales(nombre_completo))