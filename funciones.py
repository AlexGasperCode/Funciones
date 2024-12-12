# Ejercicio 1
def potencia(base,exponente):
    res = print(base ** exponente)
    return res
potencia(5,2)
# Ejercicio 2
def valor(dolares):
    con = print(dolares * 0.90)
    return con
valor(90)
# Ejercicio 3
def sum_values(a, b ,c):
    result = a + b * c
    return result
print(sum_values(4, 3 , 2))
# Ejercicio 4
def multiple():
    num = int(input("Ingrese un número: "))
    for _ in range(num):
        print("Programación con python")
multiple()
# Ejercicio 5
def sum(numeros):
    total = 0
    for x in numeros:
        total += x
    return total
print(sum((8, 2, 3, 0, 9))) 

