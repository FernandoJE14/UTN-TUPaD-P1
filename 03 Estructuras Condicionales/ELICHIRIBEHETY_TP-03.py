# 1)

# edad = int(input("Ingrese su edad: "))

# if edad >= 18:
#     print("Es mayor de edad")

# 2)

# nota = int(input("Ingrese la nota: "))

# if nota >= 6:
#     print("Aprobado")
# else:
#     print("Desaprobado")

# 3)
      
# num = int(input("Ingrese un numero par: "))

# if num % 2 == 0:
#     print("Ha ingresado un numero par")
# else:
#     print("Por favor, ingrese un numero par")             

# 4)

# edad = int(input("Ingrese su edad: "))

# if edad < 12:
#     print("Niño/a")
# elif edad >= 12 and edad < 18:
#     print("Adolescente")
# elif edad >= 18 and edad < 30:
#     print("Adulto/a joven")
# else:
#     print("Adulto/a")        

# 5)

# clave = input("Ingrese una contraseña de entre 8 y 14 caracteres: ")

# if len(clave) >= 8 and len(clave) <= 14:
#     print("Ha ingresado una contraseña correcta")
# else:
#     print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6)

# from statistics import mode, mean, median
# import random
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# moda = mode(numeros_aleatorios)
# media = mean(numeros_aleatorios)
# mediana = median(numeros_aleatorios)

# if (media > mediana) and (mediana < moda):
#     print("Hay sesgo positivo")
# elif (media < mediana) and (mediana < moda):
#     print("Hay sesgo negativo")
# elif media == moda == mediana:
#     print("Sin sesgo")
# else:
#     print("No se puede determinar si esta distribución tiene sesgo o no")

# 7)

# string = input("Ingrese una frase o palabra: ")
# ultima_letra = string[-1].lower()

# if ultima_letra in ("aeiou"):
#     print(f"{string} !")
# else:
#     print(string)

# 8)

# nombre = input("Ingrese su nombre: ")
# opcion = int(input("Ingrese opcion 1 (mayusculas), 2 (minusculas) o 3 (primera letra mayuscula): "))

# if opcion == 1:
#     print(nombre.upper())
# elif opcion == 2:
#     print(nombre.lower())
# else:
#     print(nombre.title())

# 9)

# num = int(input("Ingrese la magnitud del terremoto: "))

# if num < 3:
#     print("Muy leve (imperceptible)")
# elif num >= 3 and num < 4:
#     print("Leve (ligeramente perceptible)")   
# elif num >= 4 and num < 5:
#     print("Moderado (sentido por personas, pero generalmente no causa daños)")
# elif num >= 5 and num < 6:
#     print("Fuerte (puede causar daños en estructuras débiles)") 
# elif num >= 6 and num < 7:
#     print("Muy Fuerte (puede causar daños significativos)")   
# else:
#     print("Extremo (puede causar graves daños a gran escala)") 

# 10)

# hemisferio = input("Por favor, ingrese el hemisferio (Norte/Sur): ")
# hemisferio = hemisferio.lower()

# mes = int(input("Por favor, ingrese el mes del año en números: "))

# dia = int(input("Por favor, ingrese el día del mes en números: "))

# if hemisferio == "sur":
#   if (mes == 12 and dia >= 21) or (mes in (1,2)) or (mes == 3 and dia <= 20):
#     print("Verano")
#   elif (mes == 3 and dia >= 21) or (mes in (4,5)) or (mes == 6 and dia <= 20):
#     print("Otoño")
#   elif (mes == 6 and dia >= 21) or (mes in (7,8)) or (mes == 9 and dia <= 20):
#     print("Invierno")
#   elif (mes == 9 and dia >= 21) or (mes in (10,11)) or (mes == 12 and dia <= 20):
#     print("Primavera")   
# elif hemisferio == "norte":
#   if (mes == 12 and dia >= 21) or (mes in (1,2)) or (mes == 3 and dia <= 20):
#     print("Invierno")
#   elif (mes == 3 and dia >= 21) or (mes in (4,5)) or (mes == 6 and dia <= 20):
#     print("Primavera")
#   elif (mes == 6 and dia >= 21) or (mes in (7,8)) or (mes == 9 and dia <= 20):
#     print("Verano")
#   elif (mes == 9 and dia >= 21) or (mes in (10,11)) or (mes == 12 and dia <= 20):
#     print("Otoño")

