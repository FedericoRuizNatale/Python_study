#creanmdo diccionarios con dict()
diccionario = dict(nombre="Lucas", apellido="Dalto")


#otra forma d hacerlo
#{
    #'nombre': "dalto"
    #'apellido': "Dalto"}
    
#las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["dalto","rancio"]):"jajaja"}

#creando diccionarios con fromtkeys()  --- 
diccionario = dict.fromkeys(["nombre","apellido","suscriptores"], "no se")
diccionario = dict.fromkeys("ABCDE", "algun valor fijo") #(primer dato es un iterable y el segundo es a lo q vamos a iterar)
    
print(diccionario)