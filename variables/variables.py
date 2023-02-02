numero = 10     
numero +=3    #el += significa q va a restar o sumar lo que indique
numero -=5

print()

# Concatenar variables
nombre = 5
bienvenido = f"Hola {nombre} ¿Como estas?"   #f strings: toma un dato y lo convierte en texto
#del bienvenido
print("ola" in bienvenido)  

#Operadores de pertenencia (in / not in)       




                                    #Para hacer q una variable no este mas definida usamos el operador "del", se utiliza por orden
                                    
#Definiendo una variable con camelCase
nombreCompletoDeTuTioMaster = "lucas Dalto"
#Definiendo una variable snake_case (mas recomendada por python)
nombre_completo_de_tu_tio_master = "Lucas"

#concatenar con +
bienvenido = "Hola " + " ¿Como Estás"

#concatenar con f-strings
bienvenido = f"Hola {nombre_completo_de_tu_tio_master} ¿Como estas? "

#operadores de pertenencia (in / not in)

print("Lucas" in bienvenido) #true
print("Lucas" not in bienvenido) #false