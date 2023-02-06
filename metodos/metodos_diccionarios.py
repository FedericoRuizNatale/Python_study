diccionario = {
    "nombre" : 'Lucas',
    "apellido" : 'dalto',
    "subs" : 1000000
}

#nos devuelve un objeto dict_item
claves = diccionario.keys()


#obteniendo un elemento con get() (si no encuentra nada el programa continua)
valor_de_jajaja = diccionario.get("jajaja")

print("hola papa el programa continua")


#eliminando todo del diccionario
#diccionario.clear

#eliminando un elemento del diccionario
diccionario.pop("subs")

#obteniendo un elemento dict_items iterable (iterar es recorrer el elemento para acceder a cada uno d ellos)
diccionario_iterable = diccionario.items()

print(diccionario_iterable)