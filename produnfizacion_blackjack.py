# Numpy [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA
import numpy as np
import random

# Define variables globales
lista = [ ]
array_numero = []
suma_array = 0
respuesta = ' '
'''
Enunciado:
Black jack! [o algo parecido :)]

El objetivo es realizar una aproximación al juego de black jack,
el objetivo es generar una lista de 2 números aleatorios
entre 1 al 10 inclusive, y mostrar los "números" al usuario.

El usuario debe indicar al sistema si desea sacar más
números para sumarlo a la lista o no sacar más

A medida que el usuario vaya sacando números aleatorios que se suman
a su lista se debe ir mostrando en pantalla la suma total
de los números hasta el momento.

Cuando el usuario no desee sacar más números o cuando el usuario
haya superado los 21 (como la suma de todos) se termina la jugada
y se presenta el resultado en pantalla

BONUS Track: Realizar las modificaciones necesarias para que jueguen
dos jugadores y compitan para ver quien sacá la suma de números
más cercanos a 21 sin pasarse!
'''

def random_inicio(cantidad):
    global lista
    global array_numero
    global suma_array
    lista.clear
    # Genera numeros aleatorios
    lista = [random.randint(1, 10) for x in range(cantidad)]
    array_numero = np.asanyarray(lista)
    suma_array = np.sum(array_numero)

     # Presenta numeros aleatorios iniciales y Suma
    print('Lista Numero:', lista, 'Suma lista:', suma_array)
    print('Suma es', suma_array)

    return

if __name__ == '__main__':
    print("Ahora sí! buena suerte :)")
    # A partir de aquí escriba el código que resuelve el enunciado
    # Leer el enunciado con atención y consultar cualquier duda

     # Genera numeros aleatorios iniciales
    random_inicio(2)

    # Inicio de Juego    
    sigue = True  
    while sigue == True:  
     
        # Pregunta si desea JUGAR (S/N)
        respuesta = ''
        while not(respuesta == 'S') or not(respuesta == 'N'):
            respuesta = ' '
            respuesta = input('Desea sacar mas numeros (S/N): ')
            if (respuesta == 'N'):
                sigue = False
                break
            elif (respuesta == 'S'):
                sigue = True
                break

        # Genera nuevo numero aleatorio y lo agrega a lista  
        if (sigue == True):    
            # Genera nuevo numero aleatorio   
            nuevo_numero = [random.randint(1, 10) for x in range(1)] 

            # Agrega elemento a lista, antes convertie numero(lista) --> string --> Int 
            lista.append(int(' '.join(str(x) for x in nuevo_numero)))  

            # convierte lista en array y obtiene suma
            array_numero = np.asanyarray(lista)
            suma_array = np.sum(array_numero)
                
            # informa resultado de JUGADA
            print('Lista Numero:', lista, 'Suma lista:', suma_array)
            print('Suma es', suma_array)
        
            # Verifica resultado
            if (suma_array > 21):
                print('Uds ha PERDIDO')
                random_inicio(2)                
                
            elif (suma_array == 21):
                print('Ud ha GANADO!!!')
                random_inicio(2)            
                
    print("terminamos")