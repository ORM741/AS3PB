def consonantes_en_cadena(cadena):
    consonantes = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
    return set(c for c in cadena if c in consonantes)

cadena = "Hola Mundo!"
consonantes_presentes = consonantes_en_cadena(cadena)

print(f"Consonantes en la cadena '{cadena}': {consonantes_presentes}")