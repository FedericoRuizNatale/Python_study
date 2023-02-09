numeros = [1,2,3,4,5,6,7,8,9,14,15,20]


#lambda es una forma de crear una funcion anonima (ya que no tiene nombre)
#se usa para hacer cosas sensillas y rapidas de una sola expresion
multiplicar_por_dos = lambda x : x*2


#creando una funcion comun que diga si es par o no
#def es_par(num):
 #   if (num%2==0):
 #       return True


#usando filter con una funcion comun
#numeros_pares = filter(es_par,numeros)

#creando lo mismo que antes pero con lambda (simplifica td el codigo anterior)
#filter ejecuta cada uno de los valores pero muestra los true
numeros_pares = filter(lambda numero:numero%2 == 0,numeros)
print(list(numeros_pares))