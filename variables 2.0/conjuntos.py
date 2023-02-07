#creando un conjunto con set
conjunto = set(["dato1","dato2"])

#metiendo un conjunto dentro de otro conjunto

conjunto1 = frozenset(["dato1" , "dato2"])
conjunto2 = {conjunto1, "dato3"}

print(conjunto2)

#teoria de conjuntos

conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

#verificando si es un issubset (¿es un subconjunto?) devuelve true o false
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1


#verificando si es un issuperset (¿es un superconjunto?) devuelve true o false
resultado = conjunto1.issuperset(conjunto2)
resultado = conjunto1 > conjunto2




#verificar si hay algun numero en comun isdisjoint solo va a devolver true si todos los numeros entre los conjuntos son distintos
conjunto1 = {1,3,5,7}
conjunto2 = {2,4,6,8}
resultado = conjunto2.isdisjoint(conjunto1)


print(resultado)