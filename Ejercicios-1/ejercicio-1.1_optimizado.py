# EJERCICIO 1 
#a) cuanta diferencia en porcentaje hay entre el curso actual y: 
#-el mas rapido de los otros cursos 
#-el mas lento de los otros cursos
#-el promedio de los otros cursos


#b)que porcentaje de material inservible que se reduce en:
#el promedio de los cursos
#- el curso actual (este curso)

#c)ver 10 horas de este curso a cuantas horas de otros cursos equivale?¿y al reves?

#promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#creando las variables de crudos
crudo_promedio = 5
crudo_dalto = 3.5


#a) diferencia de duración 
diferencia_con_min = 100 - dalto_curso / otros_cursos_min * 100
diferencia_con_max = 100 - dalto_curso / otros_cursos_max * 100                #(para que de un numero redondo)
diferencia_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100

#redondeando con funcion
diferencia_con_max_redondeada = round(diferencia_con_max,2)
print("------------------------")
print("El curso de dalto dura: ")
print(f'- un {diferencia_con_min}% menos que el más rapido')
print(f'- un {diferencia_con_max_redondeada}% menos que el más lento')
print(f'- un {diferencia_con_promedio}% menos que el promedio')

print("------------------------")

#b) calculando el tiempo vacio promedio
tiempo_vacio_promedio = 100 - otros_cursos_promedio / crudo_promedio * 100
tiempo_vacio_dalto = 100 - dalto_curso / crudo_dalto *100

#redondeando con funcion
tiempo_vacio_dalto_redondeado = round(tiempo_vacio_dalto,2)

#mostrando la cantidad de espacios vacios que se remueven (ejercicio b)
print(f'un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio')
print(f'este curso eliminó el {tiempo_vacio_dalto_redondeado}% de tiempo vacio')

print("------------------------")

#c)Mostrando diferencias si los cursos duran 10 horas
equivalencia_10_horas_de_curso_dalto = otros_cursos_promedio / dalto_curso *10
equivalencia_10_horas_de_otros_cursos = 10 * dalto_curso / otros_cursos_promedio

#redondeando con funcion
equivalencia_10_horas_de_curso_dalto_redondeada = round(equivalencia_10_horas_de_curso_dalto,2)

print(f'ver 10 horas del curso de dalto equivale a ver {equivalencia_10_horas_de_curso_dalto_redondeada} horas de otros cursos')
print(f'ver 10 horas de otros cursos equivale a ver {equivalencia_10_horas_de_otros_cursos} horas del curso de dalto')

print("------------------------")

#OPTIMICE TODO EL CODIGO 

