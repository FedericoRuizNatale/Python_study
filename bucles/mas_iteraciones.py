#Creando las listas
frutas = ["banana", "manzana","ciruela","pera","naranja","granada","durazno"]
cadena = "hola dalto"
numeros = [2,5,8,10]

#evitando que se coma una granad con la sentencia continue
for fruta in frutas:
    if fruta == "granada":
        continue
    print(f'me voy a comer una {fruta}')

print("----------------------------------------------------")


#evitar que el bucle siga ejecutandose con el break (con el break no se ejecuta el else ni nada mas)
for fruta in frutas:
    print(f'me voy a comer una {fruta}')
    if fruta == "pera":
        break
print("bucle terminado")


print("----------------------------------------------------")

#recorrer una cadena de texto (recorrer = iterar)


for letra in cadena:
    print(letra)
    


#for en una sola linea d codigo
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)
