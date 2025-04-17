# 1)

# # imprimo los numeros del 0 al 100
# for cont in range(101):
#     print(cont)

# //////////////////////////////////////////////////////////////////////////

# 2)

# num = int(input("Ingrese un numero entero: "))

# # uso la funcion len() para contar los caracteres, str() para convertir el numero a cadena y abs() para no contar el signo - 
# print(f"El numero tiene {len(str(abs(num)))} digitos")

# //////////////////////////////////////////////////////////////////////////

# 3)

# print("Ingrese dos numeros enteros: ")
# num1 = int(input("Numero 1: "))
# num2 = int(input("Numero 2: "))
# suma = 0

# if num1 < num2:
#     # rango excluyendo ambos numeros
#     for cont in range(num1+1,num2):
#         suma += cont
        
#     print(f"Suma: {suma}")
# else:
#     print("El primer numero debe ser menor al segundo")

# //////////////////////////////////////////////////////////////////////////    

# 4)

# num = int(input("Ingrese un numero entero: "))
# suma = 0

# # ciclo while que se interrumpe cuando el usuario ingresa 0
# while num != 0:
#     suma += num
#     num = int(input("Ingrese otro numero: "))

# # muestro la suma de todos los numeros ingresados
# print(f"Suma total: {suma}")

# //////////////////////////////////////////////////////////////////////////

# 5)

# # importo la libreria para numeros aleatorios
# import random
# num = int(input("Ingrese un numero entre 0 y 9: "))
# num_aleatorio = random.randint(0,9)
# intentos = 0

# while num != num_aleatorio:
#     num = int(input("Ingrese otro numero entre 0 y 9: "))
#     intentos += 1

# print(f"Se necesitaron {intentos} intentos")

# //////////////////////////////////////////////////////////////////////////

# 6)

# # rango de 100 hasta -1 no incluido, y que baja de a -2 para mostar solo los pares
# for cont in range(100,-1,-2):
#     print(cont)

# //////////////////////////////////////////////////////////////////////////

# 7)

# num = int(input("Ingrese un numero entero positivo: "))
# suma = 0

# # valido si el numero ingresado es positivo
# if num >= 0:
#     # rango entre 0 y el numero ingresado, num+1 no esta incluido
#     for cont in range(0,num+1):
#         suma += cont
#     print(f"Suma: {suma}")        
# else:
#     print("El numero debe ser positivo") 

# //////////////////////////////////////////////////////////////////////////

# 8)

# # inicializo cant_num para poder probar el programa con un numero mas bajo
# cant_num = 100
# positivos = 0
# negativos = 0
# pares = 0
# impares = 0

# for cont in range(1,cant_num+1):
#     num = int(input(f"Ingrese el {cont} numero: "))
#     if num > 0:
#         positivos += 1
#     elif num < 0:
#         negativos += 1
#     # chequeo sin el resto es 0 para saber si el num es par o impar    
#     if num % 2 == 0:
#         pares += 1
#     elif num % 2 != 0:
#         impares +=1

# print(f"Positivos: {positivos}")   
# print(f"Negativos = {negativos}") 
# print(f"Pares = {pares}")
# print(f"Impares = {impares}")        

# //////////////////////////////////////////////////////////////////////////

# 9)

# cant_num = 100
# suma = 0

# for cont in range(1,cant_num+1):
#     num = int(input(f"Ingrese el {cont} numero: "))
#     suma += num

# print(f"La media es: {suma/cant_num}")

# //////////////////////////////////////////////////////////////////////////

# 10)

# num = int(input("Ingrese un numero entero: "))
# num = abs(num)
# invertido = 0

# while num != 0:
#     digito = num % 10   # para seleccionar el ultimo digito del numero
#     num = num // 10     # para quitarle un digito al numero
#     invertido = invertido * 10 + digito  # invierte el numero

# print(f"Numero invertido: {invertido}")