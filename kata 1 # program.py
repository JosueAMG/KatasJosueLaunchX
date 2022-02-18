# nombre del programa y terminacion  .py
sum = 1 + 2
print(sum)
print('se usa print para sacar mensaje')
sum = 1 + 5 # 3
product = sum * 3
print(product)



planetas_en_el_sistema_solar = 8              # int, plutón era considerado un planeta pero ya es muy pequeño
distancia_a_alfa_centauri = 4.367                  # float, años luz
puede_despegar = True
transbordador_que_aterrizo_en_la_luna = "Apollo 11"   #string
type(distancia_a_alfa_centauri)


# Declaramos la variable
distancia_a_alfa_centauri = 4.367
# Descubrimos su tipo de dato
type(distancia_a_alfa_centauri)

left_side = 10
right_side = 5
left_side / right_side # 2



   
from datetime import date
from sysconfig import parse_config_h             #asi Importamos la biblioteca   
date.today()                          #Asi otenemos la fecha de hoy
print(date.today())                   # usamos print para mostar la fecha

   #para escibir hoy + fecha, convertir fecha en cadena. mediante  la función de utilidad   +  str(    )
print("Hoy es: " + str(date.today()))


#  Para capturar información con  input()
print("Mensaje de Bienvenida ")
name = input("Introduzca su nombre ")                   # name se usa como valor al igualar con lo que se introduce usando imput x=#  X= palabra
print("Saludos: " + name)


#Trabajar con números

print("Calculadora que agrega numero")
first_number = input("Primer número: ")
second_number = input("Segundo número: ")
print(first_number + second_number)            #asi agrega 5 y 2 =52 como  cadenas de texto. y no los suma matemanticamente(5+2=7)

print("Calculadora que suma")
first_number = input("Primer número: ")
second_number = input("Segundo número: ")
print(int(first_number) + int(second_number))     #para que sume cambiar esas cadenas a números mediante la función    int( )



                     #Kata 1
print("Kata1")
from datetime import date
print("Today's date is: " + str(date.today()))
 
    
    
     #combertidor de parcec a años luz

print("comvertidor parsec a años luz")
parsec = 11
lightyears = 3.26156 * parsec

print(str(parsec) + " parsec, is " + str(lightyears) + " lightyears")


      #kata con combertidor per con imput (experimento)

parsec = input("parsec: ")
añosluz = 3.26156 
print(int(parsec) * int(añosluz)) 



