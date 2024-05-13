import random
contador = 0
encontrado = False

print('''Bienvenido al juego de adivinar el número secreto de 3 Feb.
Tienes que adivinar un número entre 1 y 50. ¡Buena suerte!''')

inicio = input("Ingrese el valor mínimo del rango de números: ")
fin = input("Ingrese el valor máximo del rango de números: ")

numero_secreto = random.randint(int(inicio),int(fin))

while contador < 5 and not encontrado:
    print(f"Turno: {contador + 1}")
    candidato = input(f"Ingrese un número entre  {inicio} y {fin} : ")
    if (candidato.isalpha()):   #pregunto si es una letra
       print("El valor ingresado no es numérico.")   
    elif (int(candidato) < int(inicio) or int(candidato) > int(fin)):  #pregunto si está fuera de rango
        print("El número ingresado está fuera del rango.")
    elif (int(candidato) == numero_secreto):
        encontrado = True
        print("Ganaste!! El número ingresado coincide con el número secreto!!")
    else:        
        contador += 1
        if (int(candidato) < numero_secreto):
           print("El número secreto es mayor al número ingresado.")
        else:
            print("El número secreto es menor al número ingresado.")

if(not encontrado):
    print(f"Perdiste! El número secreto era : {numero_secreto}")    
        