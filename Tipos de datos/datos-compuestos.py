#Creando una lista que sirve para agrupar datos, se usan [] --- una matriz es un conjunto de datos
# se Pueden modificar

lista = ["Lucas Dalto", "Soy Dalto", True, 1.85]

#La tupla es igual a la lista pero no se puede modificar 
tupla = ("Lucas Dalto", "Soy Dalto", True, 1.85)

#esto es válido
lista[3] = "maquinola"

#esto no
#tupla[3] = "maquinola"

#Creando un conjunto (set) (podemos reconstruirlo pero no modificarlo)
#no se puede acceder por el indice a un elemento del conjunto (se muestra completo)
#no almacena datos duplicados
#son datos desordenados
conjunto = {"Lucas Dalto", "Soy Dalto", True, 1.85}

#print(conjunto[3]) -> no puede acceder al elemento

# Creando un diccionario (dict) (la estructura es key : value y separamos con comas)
diccionario = {
    'key' : "value",
    'nombre' : "Lucas Dalto",
    'canal' : "Soy dalto",
    'esta_emocionado' : True,
    'altura' : 1.84,
    'dato_duplicado' : "Soy Dalto"
}
print(diccionario ['nombre']) 