#!/usr/bin/python
                                            
#
# Practica 3
# Nava Badillo Yessica Isabel
#

## Importar librerias
import sys
import pandas as pd

## Abrir archivo Excel utilizando pandas
# Si el archivo no se especifico en el argumento de linea de comandos...
if len(sys.argv) < 2:
    # Pedir el archivo
    excel = pd.read_excel(input("Ingresar archivo de Excel para crear el trie: "), dtype = str)
# Si se especifico...
else:
    # Usar el archivo proporcionado
    excel = pd.read_excel(sys.argv[1], dtype = str)

# Seleccionar solo las columnas que nos interesan de el archivo
df = pd.DataFrame(excel, columns=["Letras", "Cadenas"])

## Definir variables
# Clase de nodo de nuestra estructura trie, donde:
# - zero: nodo que queda a la "izquierda" de el nodo.
# - uno: nodo que queda a la "derecha" de el nodo.
# - final: si es "False" la cadena no termina aqui. Si tiene algun
#          valor, es la letra en la que acaba nuestra cadena.
class nodoTrie:
    def __init__(self, zero, uno, final):
        self.zero = zero
        self.uno = uno
        self.final = final

# Nuestras listas de codigos y letras
codes = []
chars = []

# Importamos los valores de la tabla a las listas
for char in df["Letras"].values:
    chars.append(char)
for char in df["Cadenas"].values:
    codes.append(char)

# Nuestra lista de nodos
nodos = []

# Nuestro nodo "root" o la raiz, el primer nodo
root  = nodoTrie( 0, 0, False)
# Agregar el nodo a nuestra lista
nodos.append(root)

### --- Iniciar creacion de trie ---
# Por cada codigo en nuestra lista...
for i in range(len(codes)):
    # Nuestro nodo actual es "root" ya que empezamos desde el inicio
    nodoAhora = root

    # Leemos nuestro codigo caracter por caracter
    for char in range(len(codes[i])):
        # Si en nuestro codigo damos vuelta a la izquierda...
        if codes[i][char] == "0":
            # Y el nodo a nuestra izquierda no existe...
            if nodoAhora.zero == False:
                # Y no es el fin de nuestro codigo...
                if char != len(codes[i]) - 1:
                    # Crear nuevo nodo y asignar que esta a la izquierda de el nodo actual
                    nodos.append(nodoTrie(0, 0, False))
                    nodoAhora.zero = nodos[len(nodos)-1]
                # Si es el fin de nuestro codigo...
                else:
                    # Crear nuevo nodo y asignar que esta a la izquierda de el nodo actual, tambien darle valor a su "final"
                    nodos.append(nodoTrie(0, 0, chars[i]))
                    nodoAhora.zero = nodos[len(nodos)-1]
                # Actualizar en que nodo estamos
                nodoAhora = nodoAhora.zero
            # Y el nodo a nuestra izquierda si existe...
            else:
                # Actualizar en que nodo estamos
                nodoAhora = nodoAhora.zero

        # Si en nuestro codigo damos vuelta a la derecha...
        if codes[i][char] == "1":
            # Y el nodo a nuestra derecha no existe...
            if nodoAhora.uno == False:
                # Y no es el fin de nuestro codigo...
                if char != len(codes[i]) - 1:
                    # Crear nuevo nodo y asignar que esta a la derecha de el nodo actual
                    nodos.append(nodoTrie(0, 0, False))
                    nodoAhora.uno = nodos[len(nodos)-1]
                # Si es el fin de nuestro codigo...
                else:
                    # Crear nuevo nodo y asignar que esta a la derecha de el nodo actual, tambien darle valor a su "final"
                    nodos.append(nodoTrie(0, 0, chars[i]))
                    nodoAhora.uno = nodos[len(nodos)-1]
                # Actualizar en que nodo estamos
                nodoAhora = nodoAhora.uno
            # Y el nodo a nuestra derecha si existe...
            else:
                # Actualizar en que nodo estamos
                nodoAhora = nodoAhora.uno

### --- Fin de creacion de trie ---

### Verificar la creacion de nuestro trie
## Por cada codigo...
#for i in range(len(codes)):
#    # Empezamos en "root"
#    nodoAhora = root
#
#    # Por cada caracter en nuestro codigo...
#    for char in range(len(codes[i])):
#        # Si damos vuelta a la izquierda...
#        if codes[i][char] == "0":
#            # Actualizar nodo actual a el nodo a nuestra izquierda
#            nodoAhora = nodoAhora.zero
#            # Mostrar la parte de el codigo en la que vamos y el nodo actual
#            print(codes[i][char], nodoAhora)
#        # Si damos vuelta a la derecha...
#        if codes[i][char] == "1":
#            # Actualizar nodo actual a el nodo a nuestra derecha
#            nodoAhora = nodoAhora.uno
#            # Mostrar la parte de el codigo en la que vamos y el nodo actual
#            print(codes[i][char], nodoAhora)
#
#        # Si nuestro nodo actual es el final...
#        if nodoAhora.final != False:
#            # Mostrar el valor de el "final"
#            print(nodoAhora.final)

### --- Empieza menu ---
## Variables
# Entrada y salida
# - cadena: una cadena binaria
# - caracteres: una cadena de caracteres
cadena = ""
caracteres = ""
# Seleccion para menu
menu = "0"

## Bucle de menu
while True:
    # Mostrar opciones
    print("===== Codificiacion y Decodificacion de trie =====")
    print("\t1) Codificacion")
    print("\t2) Decodificacion")
    if menu == "1":
        print("\t3) Decodificacion con valor resultante de codificacion:")
        print(f"\t   {cadena}")
    if menu == "2":
        print("\t4) Codificacion con valor resultante de decodificacion:")
        print(f"\t   {caracteres}")
    if menu == "4":
        print("\t3) Decodificacion con valor resultante de codificacion:")
        print(f"\t   {cadena}")
    if menu == "3":
        print("\t4) Codificacion con valor resultante de decodificacion:")
        print(f"\t   {caracteres}")
    print()
    print("\t0) Salir")
    print()
    menu = input("Que desea hacer? (ingresar numero): ")[0]
    print()

### --- Empieza codificacion y decodificacion ---
    ## Manejar la opcion que nos pidieron
    match menu:
        # En caso de...
        case "1":
            ## Codificacion
            # Limpiar variable de salida
            cadena = ""
            # Pedir cadena de caracteres al usuario
            caracteres = input("Ingresar cadena de caracteres: ")

            # Por cada caracter en la cadena ingresada...
            for char in range(len(caracteres)):
                # Si el caracter no existe en nuestro trie...
                if caracteres[char] not in chars:
                    # Darle un error al usuario, reiniciar seleccion de menu y salir de el bucle para regresar a las opciones
                    print("Error! Caracter no valido en la cadena de caracteres")
                    menu = 0
                    break
                # Si existe, concatenar el codigo correspondiente a nuestra variable "cadena"
                cadena += codes[chars.index(caracteres[char])]

            # Mostrar resultado
            print()
            print(f"Resultado: {cadena}")

        # En caso de...
        case "2":
            ## Decodificacion
            # Limpiar variable de salida
            caracteres = ""
            # Pedir cadena binaria al usuario
            cadena = input("Ingresar cadena binaria: ")
            # Empezamos en nodo "root"
            nodoAhora = root
            
            # Por cada caracter en nuestra cadena...
            for char in range(len(cadena)):
                # Si damos vuelta a la izquierda...
                if cadena[char] == "0":
                    # Actualizar nodo actual
                    nodoAhora = nodoAhora.zero
                # Si damos vuelta a la derecha...
                if cadena[char] == "1":
                    # Actualizar nodo actual
                    nodoAhora = nodoAhora.uno
            
                # Si el nodo actual es un nodo final...
                if nodoAhora.final != False:
                    # Concatenar el valor de "final" a nuestra variable de caracteres
                    caracteres += nodoAhora.final
                    # Actualizar nodo actual a "root" para volver a iniciar
                    nodoAhora = root

            # Mostrar resultado
            print()
            print(f"Resultado: {caracteres}")
        
        # En caso de...
        case "3":
            ## Decodificacion utilizando resultado
            # Limpiar variable de salida
            caracteres = ""
            # Empezamos en nodo "root"
            nodoAhora = root
            
            # Por cada caracter en nuestra cadena...
            for char in range(len(cadena)):
                # Si damos vuelta a la izquierda...
                if cadena[char] == "0":
                    # Actualizar nodo actual
                    nodoAhora = nodoAhora.zero
                # Si damos vuelta a la derecha...
                if cadena[char] == "1":
                    # Actualizar nodo actual
                    nodoAhora = nodoAhora.uno
            
                # Si el nodo actual es un nodo final...
                if nodoAhora.final != False:
                    # Concatenar el valor de "final" a nuestra variable de caracteres
                    caracteres += nodoAhora.final
                    # Actualizar nodo actual a "root" para volver a iniciar
                    nodoAhora = root

            # Mostrar resultado
            print()
            print(f"Resultado: {caracteres}")

        # En caso de...
        case "4":
            ## Codificacion con utilizando resultado
            # Limpiar variable de salida
            cadena = ""

            # Por cada caracter en la cadena...
            for char in range(len(caracteres)):
                # Concatenar el codigo correspondiente a nuestra variable "cadena"
                cadena += codes[chars.index(caracteres[char])]

            # Mostrar resultado
            print()
            print(f"Resultado: {cadena}")

        # En caso de...
        case "0":
            ## Salir
            quit()

        # En caso de...
        case _:
            ## Opcion no especificada
            print("Error! Opcion incorrecta")

    # Dar tiempo para que el usuario vea el resultado
    input("(enter para continuar)")
    print()
