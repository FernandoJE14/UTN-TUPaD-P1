# TP 1
# FERNANDO JAVIER ELICHIRIBEHETY

#1)

print("Hola Mundo!")

#2)

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

#3)

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#4)

import math
radio = float(input("Ingrese el radio: "))
area = math.pi * (radio)**2
perimetro = 2 * math.pi * radio
print(f"El area del circulo es: {round(area, 2)}")
print(f"El perimetro del circulo es: {round(perimetro, 2)}")

#5)

segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos / 3600
print("Equivale a:", horas, "hs")

#6)

num = int(input("Ingrese un numero: "))
print(f"{num} x 1 = {num * 1}")
print(f"{num} x 2 = {num * 2}")
print(f"{num} x 3 = {num * 3}")
print(f"{num} x 4 = {num * 4}")
print(f"{num} x 5 = {num * 5}")
print(f"{num} x 6 = {num * 6}")
print(f"{num} x 7 = {num * 7}")
print(f"{num} x 8 = {num * 8}")
print(f"{num} x 9 = {num * 9}")
print(f"{num} x 10 = {num * 10}")

#7)

num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
print(f"Suma = {num1 + num2}")
print(f"Resta = {num1 - num2}")
print(f"Multiplicacion = {num1 * num2}")
print(f"Division = {round((num1 / num2), 2)}")

#8)

altura = float(input("Ingrese la altura en (m): "))
peso = float(input("Ingrese el peso en (kg): "))
imc = peso / (altura)**2
print(f"IMC = {round(imc, 2)} kg/m^2")

#9)

celsius = int(input("Ingrese la temperatura en (°C): "))
fahrenheit = 9/5 * celsius + 32
print(f"{celsius} °C = {fahrenheit} °F")

#10)

num1 = float(input("Ingrese un numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))
print(f"El promedio es = {(num1 + num2 + num3)/3}")
