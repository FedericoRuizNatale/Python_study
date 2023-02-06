#Creando una lista con list()
lista = list([65,34, 56 , 23, True, 2023])

#Devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

#agregando un elemento a la lista
#lista.append("JAJAJAJA")


#agregando un elemento a la lista en un indice especifico
lista.insert(2, "mama")


#agrega varios elementos a la lista (se agg como una lista dentro de corchetes)
lista.extend([False, 2023])



#eliminando un elemento de la lista por su indice

lista.pop(-1)  #el -1 elimina el ultimo elemento -2 el penultimo etc


#removiendo un elemento de la lista por su valor

lista.remove("mama")

#eliminando todos los elemtnos de la lista
#lista.clear()


#sort()ordena la lista de forma ascendente (si usamos el parametro reverse=true lo ordena en reversa) no tiene que haber cadenas de texto ("mama")
lista.sort()

#invirtiendo los elementos de una lista sin ordenarla
lista.reverse()

#verificando si un elemento se encuentra en la lista
elemento_encontrado = lista.index(True)

print(elemento_encontrado)


