#EJERCICIO 2
#A)Pedirle al usuario que diga cualquier texto real y:

#-calcular cuanto tardaria en decir esa frase
#-cuantas palabras dijo

#B)si tarda mas de 1 minuto:
#-decirle "para flaco tampoco te pedi un testamento"

#C) dalto habla un 30% mas rapido: ¿cuanto tardaria en decirlo?

#cada persona habla por segundo 2 palabras

#a)
frase = input("decime una frase y calculo cuanto tardas en decirla ")
palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)
duracion_frase = cantidad_de_palabras / 2
duracion_dalto = duracion_frase * 0.3
print("-----------------")
print(f'dijo {cantidad_de_palabras} palabras')

print("-----------------")
print(f'tardarias {duracion_frase} segundos en decirlas')

print("-----------------")

if duracion_frase > 60:
    print("PARA FLACO TAMPOCO TE PEDI UN TESTAMENTO")

print(f'dalto tardaria {duracion_dalto} segundos en decirla')
print("-----------------")







