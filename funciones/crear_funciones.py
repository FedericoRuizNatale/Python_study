#creando una funcion simple

#def saludar():
   # print("Hola Lucas, mi maestro ¿como andas?")

#ejecutando la funcion simple
#saludar()

#crear una funcion que tenga parametro (son variables dentro de una funcion)
def saludar (nombre,sexo):
    sexo = sexo.lower()
    if(sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "titan"
    else:
        adjetivo = 'amor'
    
    print(f"Hola {nombre}, mi {adjetivo} ¿como andas?")
    
saludar("camila","mujer")
saludar("dalto", "hombre")
saludar("fede","x")

#crear una funcion que nos retorne valores
def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    print(contraseña)
    
crear_contraseña_random(1)
    
