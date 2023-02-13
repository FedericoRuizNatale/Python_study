#importando un modulo y asignandole el nombre "m_saludar"
#import modulo saludar as m_saludar

#desde ese modulo, importamos dos funciones
from modulo_saludar import saludar,saludar_raro as saludar_como_coscu

#creamos las variables con los saludos
saludo = saludar("Lucas")
saludo_raro = saludar_como_coscu("Fede")

#mostramos los resultados
print(saludo)
print(saludo_raro) 

#para ver las propiedades y metodos de el namespace
#print(dir(m_saludar))



