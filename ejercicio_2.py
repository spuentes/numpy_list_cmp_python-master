# Numpy [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con lambda


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Lambda expression
    # 1)
    # Realizar una funcion lambda que retorne el tamaño
    # (len) de un string pasado como parámetro
    dato_ok = False
    while dato_ok == False:
            data = input('Ingrese iun string: ')
            if len(data) > 0:
                dato_ok = True
            else:
                print('Error.. dato esta vacio')

    largo_string = lambda x: len(data)
    print('String', data, ' su longitud es ', largo_string(data))

    # len_string = lambda......

    # 2)
    # Lista de string
    palabras = ['Inove', 'casa', 'programacion']

    # Utilice la función map para mapear una lambda expression
    # que retorne el tamaño (len) de cada texto em cata iteración
    # de la lista de textos
    # El resultado (el len de cada palabra) se debe ir almacenando
    # en una nueva lista
    # Nota: realizar la lambda expression "in line"
    # Copiar la lambda creada en el paso anterior dentro del map
    # NOTA: No debe usar "len_string" dentro del map, debe colocar
    # directamente la lambda.

    # palabras_len = list(map....)
    largo = lambda palabra: len(palabra)
    palabras_len = list(map(largo, palabras))
    print('Longitud palabras', palabras, palabras_len)

    print("terminamos")