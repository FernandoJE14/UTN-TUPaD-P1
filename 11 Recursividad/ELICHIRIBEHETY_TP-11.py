# 1)

# def factorial(num):
#     # Caso base: el factorial de 0 es 1
#     if num == 0:
#         return 1
#     else:
#         return num * factorial(num-1)

# def factorial_numeros(num):
#     # Bucle desde 1 hasta el número ingresado (inclusive)
#     for i in range(1, num+1):
#         # Calcula e imprime el factorial de cada número i
#         print(f"Factorial de {i}: {factorial(i)}")

# num = int(input("Ingrese un numero: "))
# factorial_numeros(num)

#///////////////////////////////////////////////////////////

# 2)

# def fibonacci(posicion):
#     # Caso base: si la posición es 0, devuelve 0
#     if posicion == 0:
#         return 0
#     # Segundo caso base: si la posición es 1, devuelve 1
#     elif posicion == 1:
#         return 1
#     else:
#         return fibonacci(posicion-1) + fibonacci(posicion-2)

# def fibonacci_posicion(posicion):
#     # Recorre desde la posición 0 hasta la ingresada (inclusive)
#     for i in range(0, posicion+1):
#         print(f"El valor de Fibonacci en la posicion {i} es: {fibonacci(i)}")    

# posicion = int(input("Ingrese la posicion: "))
# fibonacci_posicion(posicion)

#///////////////////////////////////////////////////////////

# 3)

# def potencia(num,exp):
#     # Caso base: cualquier número elevado a 0 es 1
#     if exp == 0:
#         return 1
#     else:
#         return num * potencia(num, exp-1)
    
# num = int(input("Ingrese un numero: "))
# exponente = int(input("Ingrese el exponente: "))

# print(f"{num} elevado a la {exponente} es: {potencia(num,exponente)}")

#///////////////////////////////////////////////////////////

# 4)

# def decimal_binario(num):
#     # Caso base: si el número es 0 o 1, lo devolvemos como cadena
#     if num == 0:
#         return "0"
#     elif num == 1:
#         return "1"
#     else:
#         # Dividimos el número por 2 y llamamos recursivamente
#         # Luego concatenamos el residuo (n % 2) al resultado
#         return decimal_binario(num // 2) + str(num % 2)

# print("Conversor de decimal a binario")
# num = int(input("Ingrese un numero entero positivo: "))

# if num < 0:
#     print("El numero debe ser positivo.")
# else:
#     print(f"La representacion binaria de {num} es: {decimal_binario(num)}")    

#///////////////////////////////////////////////////////////

# 5)

# def es_palindromo(palabra):
#     # Caso base: si la palabra tiene 0 o 1 letras, es un palíndromo
#     if len(palabra) <= 1:
#         return True
#     # Comparamos la primera y la última letra
#     if palabra[0] != palabra[-1]:
#         return False
#     # Llamada recursiva con la subcadena sin la primera y la última letra
#     return es_palindromo(palabra[1:-1])

# palabra = input("Ingrese una palabra sin espacios ni tildes: ").lower()
# print(es_palindromo(palabra))

#///////////////////////////////////////////////////////////

# 6)

# def suma_digitos(num):
#     # Caso base: si el número es 0, ya no hay más dígitos que sumar
#     if num == 0:
#         return 0
#     else:
#         # Nos aseguramos de trabajar con un número positivo
#         num = abs(num)
#         # Obtenemos el último dígito del número
#         digito = num % 10
#         # Quitamos un digito al número
#         return digito + suma_digitos(num // 10)

# num = int(input("Ingrese un numero entero positivo: "))
# print(f"La suma de los digitos del numero {num} es: {suma_digitos(num)}")

#///////////////////////////////////////////////////////////

# 7)

# def contar_bloques(num):
#     # Caso base: si el número es 0, no hay bloques para contar
#     if num == 0:
#         return 0
#     else:
#         # Sumamos el número con la llamada recursiva del numero anterior
#         return num + contar_bloques(num-1)

# num = int(input("Ingrese la cantidad de bloques: "))
# print(f"Para construir la piramide se necesitan {contar_bloques(num)} bloques")

#///////////////////////////////////////////////////////////

# 8)

# def contar_digito(num, digito):
#     # Caso especial: si el número es 0 y el dígito también es 0, devolver 1
#     if num == 0 and digito == 0:
#         return 1
#     # Caso base general: si el número llegó a 0, terminar la recursión
#     elif num == 0:
#         return 0
#     else:
#         num = abs(num)
#         # Obtener el último dígito del número
#         digito_num = num % 10
#         # Si coincide con el dígito buscado, sumamos 1
#         if digito == digito_num:
#             return 1 + contar_digito(num // 10, digito)
#         else:
#             return contar_digito(num // 10, digito)
        
# num = int(input("Ingrese un numero entero positivo: "))
# digito = int(input("Ingrese un digito entre el 0 y el 9: "))

# if digito >= 0 and digito <= 9:
#     print(f"El numero {digito} está {contar_digito(num, digito)} veces dentro del numero {num}")
# else:
#     print("El digito debe estar entre 0 y 9") 

