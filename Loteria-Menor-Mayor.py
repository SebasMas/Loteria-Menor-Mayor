#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.


list = []

cantidad = int(input("Cúantos números ganadores hay?: "))

while cantidad > 1:
    for i in range(cantidad):
        numero = int(input("Ingrese uno de los números ganadores: "))
        list.append(numero)
    newlist = sorted(list)
    print(reversed(newlist))
            
    
    