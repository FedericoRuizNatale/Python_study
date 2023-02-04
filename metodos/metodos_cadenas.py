cadena1 = "Hola,soy,Dalto"
cadena2 = "Bienvenido Maquinola"


#el dato. el nombre del metodo ()
#resultado = cadena1.upper()

#buscamos una cadena en otra cadena(devuelve la posicion en la q la encuentra), -1 cuando no encuentra el valor
busqueda_find = cadena1.find("D")

#buscamos una cadena en otra cadena, si no encuentra coincidencia nos lanza un error llamada "excepcion"
busqueda_index = cadena1.index("a")

#si es numerico, devolvemos true, sino false
es_numerico = cadena1.isnumeric()

#si es alfa numerico devuelve true, sino false (no se pueden poner espacios ni caracteres especiales)
es_alfanumerico = cadena1.isalpha()

#contamos las coincidencias de una cadena dentro de otra cadena, devuelve la cantidad de veces que encuentra esa coincidencia
contar_coincidencias = cadena1.count("a")

# contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve true
empieza_con = cadena1.startswith("H")

#verificamos si una cadena termina con otra cadena dada, si es asi devuelve true
termina_con = cadena1.endswith("o")

#si el valor 1, se encuentra en la cadena original, remplaza el valor 1 de la misma , por el valor 2
cadena_nueva = cadena1.replace("," , " ")
cadena_nueva_2 = cadena_nueva.capitalize()

#separar cadenas con la cadena que le pasemos formando una lista
cadena_separada = cadena1.split(",")


print(cadena_separada[0])