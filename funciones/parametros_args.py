#forma no optima de sumar valores
#def suma(lista):
   # numeros_sumados = 0
   # for numero in lista:
   #     numeros_sumados = numeros_sumados + numero
   # return numeros_sumados

#resultado = suma ([5,9,8,10,15,20])
#forma optima de sumar valores
def suma_total(numeros):
    return sum([*numeros])

resultado2 = suma_total([5,9,8,10,15,20])

print(resultado2)



#Utilizandoel parametro args(*) -- es el unico parametros que podemos usar (se usa al final)
#Utilizando el operador * como argumento (*args)
def suma(nombre,*numeros):
    return f"{nombre}, la suma de tus numeros es: {sum(numeros)}" 





resultado = suma("Fede",4,5,8,7,6,3)
print(resultado)



