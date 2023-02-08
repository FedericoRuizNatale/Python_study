numeros = [4,7,1,42,15]


#Encontrando el numero mayor de una lista (si o si numeros)
numero_mas_alto = max(numeros)
print(numero_mas_alto)

print("-------------------------")

#Encontrando el num mas bajo
numero_mas_bajo = min(numeros)
print(numero_mas_bajo)

#redondeando a 6 decimales
numero = round(12.3456789,2)

print(numero)

#retorna false -> 0, vacio, False, ninguno(none)/ True -> distinto a 0,True,cadena,datos no vacios
resultado = bool("hola")
print(resultado)

#retorna True, si todos los valores son verdaderos(si o si tds tienen q ser verdaerso)
resultado_all = all([234,"true",[344,12]])

#suma todos los valores de un iterable ( si o si numeros)
suma_total = sum(numeros)
print(suma_total)
