# hoy falto el profesor de clase y los chicos se organizaron para hacer su clase propia 
#-1 alumno es profesor
#-1 alumno es asistente

#A) pedir la edad de los compañeros que vinieron hoy a clase y ordenar los datos de menor a mayor

#B) El mayor es el profesor y el menor es el asistente ¿Quien es quien?

#funcion para obtemer al asistente y al profesor segun la edad
def obtener_compañeros(cantidad_de_compañeros):
    
    
    #creando la lista de compañeros
    compañeros = []
    
    
    #ejecutando un for para pedir informacion de cada compañero
    for i in range(cantidad_de_compañeros):
        nombre = input ("ingrese el nombre del compañero ")
        edad = int(input("ingrese su edad "))
        compañero = (nombre,edad)
    #agregando informacion a la lista
        compañeros.append(compañero)
        
    #ordendolos de menor a mayor segun su edad
    compañeros.sort(key=lambda x:x[1])
    
    #compañeros[x] devuelve una tupla con (nombre,edad) y despues accedemos al nombre para definir al asistente y al profesor
    asistente = compañeros[0][0]
    profesor = compañeros [-1][0] #accedemos al ult elem y al nombre
    
    #retornamos la tupla
    return asistente,profesor

#desempaquetamos lo que nos retorna la funcion
asistente,profesor = obtener_compañeros(5)

#mostrando el resultado
print(f"El profesor es: {profesor} y su asistente es: {asistente}")


