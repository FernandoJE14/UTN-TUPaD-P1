# 1)

# # Comenzamos en 4, terminamos en 100 (101 no se incluye), y avanzamos de 4 en 4
# lista = list(range(4, 101, 4))
# print(lista)

# 2)

# lista = [1, 2, 3, 4, 5]
# print(lista[-2]) # [-2] muestra el penultimo valor

# 3)

# # creo una lista vacia
# lista = []
# # agrego las palabras una por una
# lista.append("uno")
# lista.append("dos")
# lista.append("tres")
# print(lista)

# 4)

# animales = ["perro", "gato", "conejo", "pez"]
# # tomo el segundo y el ultimo elemento y los modifico
# animales[1] = "loro"
# animales[-1] = "oso"
# print(animales)

# 5)

# El programa crea una lista de numeros, luego con remove(max(numeros)), elimina el numero 
# mas garnde de la lista, por lo que se imprime [8, 15, 3, 7]

# 6)

# lista = list(range(10, 31, 5))
# # muestro los primeros dos numeros de la lista
# print(lista[0], lista[1])

# 7)

# autos = ["sedan", "polo", "suran", "gol"]
# # actualizo los elementos 1 y 2
# autos[1] = "vento"
# autos[2] = "golf"
# print(autos)

# 8)

# dobles = []
# # agrego a la lista el doble de 5, 10 y 15
# dobles.append(10)
# dobles.append(20)
# dobles.append(30)
# print(dobles)

# 9)

# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
# # Agrego "jugo" a la lista del tercer cliente usando append.
# compras[2].append("jugo")
# # Reemplazo "fideos" por "tallarines" en la lista del segundo cliente.
# compras[1][1] = "tallarines"
# # Elimino "pan" de la lista del primer cliente.
# compras[0].remove("pan")
# print(compras)

# 10)

# lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
# print(lista_anidada)