#Los bucles son for - in 
#en este ejemplo se puede observar q el bucle se ejecuta cuantos animales haya. 
animales = ["perro","gato","Loro","cocodrilo"]
numeros = [10,62,12,72]



#recorriendo la lista animales
for animal in animales:
    print(f'ahora la variable animal es igual a : {animal}')

print("----------------")

#recorriendo la lista multiplicando el valor por 10  
for numero in numeros:
    resultado = numero * 10
    print(resultado)
    
print("----------------")

#iterar dos listas del mismo tamaño al mismo tiempo 
for numero, animal in zip(animales,numeros):
    print(f"recorriendo lista 1: {animal}")
    print(f"recorriendo lista 2: {numero}")
    
print("----------------")

#mostrar un rango de numeros (el primer numero se muestra y el segundo el penultimo)
for num in range(5):
    print(num)
    
#forma no optima de correr una lista con su indice (no funciona en conjuntos)
for num in range (len(numeros)):
    print(numeros[num])


print("----------------")

#forma optima de recorrer una lista obteniendo su indice
for num in enumerate(numeros):
    indice = (num[0])
    valor = (num[1])
    print(f'el indice es {indice} y el valor es : {valor}')


print("----------------")

for num, i in enumerate(numeros):
    print(num)

print("----------------")


#usando el for/else (el else siempre se muestra solo una vez y al final del bucle)
for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual {numero}")
else:
    print("el bucle termino")
    
#TODO LO ANTERIOR FUNCIONA EXACTAMENTE IGUAL CON TUPLAS, LISTAS Y CONJUNTOS
    