diccionario = {
    "nombre" : "lucas",
    "apellido" : "dalto",
    "suscriptores" : 1000000,
    
}

#recorriendo diccionario para obtener las claves
for key in diccionario:
    print(f'la clave es {key}')

print("----------------------------------------------------")

#recorriendo diccionario con items() para obtener la clave y el valor
for datos in diccionario.items():
    key = (datos[0])                 #la clave es lo de la izq
    value = (datos[1])
    print(f'la clave es: {key} y el valor es: {value}')