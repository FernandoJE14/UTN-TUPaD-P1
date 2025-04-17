# 1)

# # Definir funciones
# def imprimir_hola_mundo():
#     print("Hola mundo!")

# # Programa principal
# imprimir_hola_mundo()

# 2)

# # Definir funciones
# def saludar_usuario(nombre):
#     print(f"Hola {nombre}!")


# # Programa principal
# nombre = input("Ingrese su nombre: ")
# saludar_usuario(nombre)

# 3)

# # Definir funciones
# def informacion_personal(nombre, apellido, edad, residencia):
#     print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# # Programa principal
# nombre = input("Ingrese su nombre: ")
# apellido = input("Ingrese su apellido: ")
# edad = input("Ingrese su edad: ")
# residencia = input("Ingrese su residencia: ")
# informacion_personal(nombre, apellido, edad, residencia)

# 4)

# # Definir funciones
# def calcular_area_circulo(radio):
#     import math
#     area = math.pi * (radio)**2
#     print(f"El area del circulo es: {round(area, 2)}")

# def calcular_perimetro_circulo(radio):
#     import math
#     perimetro = 2 * math.pi * radio
#     print(f"El perimetro del circulo es: {round(perimetro, 2)}")    

# # Programa principal
# radio = float(input("Ingrese el radio: "))
# calcular_area_circulo(radio)
# calcular_perimetro_circulo(radio)

# 5)

# # Definir funciones
# def segundos_a_horas(segundos):
#     horas = segundos / 3600
#     print(f"{segundos} segundos = {round(horas, 2)} horas")

# # Programa principal
# segundos = int(input("Ingrese la cantidad de segundos: "))
# segundos_a_horas(segundos)

# 6)

# # Definir funciones
# def tabla_multiplicar(numero):
#     for i in range(11):
#         print(f"{numero} x {i} = {numero * i}")

# # Programa principal
# numero = int(input("Ingrese el numero a multiplicar: "))
# tabla_multiplicar(numero)

# 7)

# # Definir funciones
# def operaciones_basicas(a, b):
#     print(f"{a} + {b} = {a + b}")
#     print(f"{a} - {b} = {a - b}")
#     print(f"{a} x {b} = {a * b}")
#     print(f"{a} / {b} = {round((a / b), 2)}")

# # Programa principal
# a = float(input("Ingrese el primer numero: "))
# b = float(input("Ingrese el segundo numero: "))
# operaciones_basicas(a, b)

# 8)

# # Definir funciones
# def calcular_imc(peso, altura):
#     print(f"IMC = {round((peso / altura**2), 2)}")

# # Programa principal
# peso = float(input("Ingrese el peso en Kg: "))
# altura = float(input("Ingrese la altura en metros: "))
# calcular_imc(peso, altura)

# 9)

# # Definir funciones
# def celsius_a_fahrenheit(celsius):
#     fahrenheit = (celsius * 9/5) + 32
#     print(f"{celsius}° celsius = {fahrenheit}° fahrenheit")

# # Programa principal
# celsius = float(input("Ingrese la temperatura en Celsius: "))
# celsius_a_fahrenheit(celsius)

# 10)

# # Definir funciones
# def calcular_promedio(a, b, c):
#     promedio = (a + b + c)/3
#     print(f"El promedio es = {round(promedio, 2)}")

# # Programa principal
# a = float(input("Ingrese el primer numero: "))
# b = float(input("Ingrese el segundo numero: "))
# c = float(input("Ingrese el tercer numero: "))
# calcular_promedio(a, b, c)