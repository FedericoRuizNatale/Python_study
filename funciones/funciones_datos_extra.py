#creando una funcion de 3 parametros
#def frase(nombre,apellido,adjetivo):
    #return f'Hola {nombre} {apellido}, sos muy {adjetivo}'

#utilizando keyword arguments
#frase_resultante = frase(apellido = "Ruiz",adjetivo ="atractivo",nombre ="Fede")




#creando la misma funcion con un parametro opcional y un valor por defecto
def frase(nombre,apellido,adjetivo = "tonto"):
    return f'Hola {nombre} {apellido}, sos muy {adjetivo}'

frase_resultante = frase("Fede", "Ruiz",adjetivo = "inteligente")

print(frase_resultante)