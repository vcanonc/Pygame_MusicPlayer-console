""" Reproductor de Música .v2
    Grupo 3
    Programación Orientada a Objetos
    2021-2
"""
import os
from pygame import mixer
from random import choice


def reproducirCancion(c): 
    mixer.music.load(c)
    mixer.music.set_volume(0.7)
    mixer.music.play()


def pausarCancion(): 
    mixer.music.pause()


def reanudarCancion(): 
    mixer.music.unpause()


def detenerCancion(): 
    mixer.music.stop()


def modificarVolumen(v): 
    mixer.music.set_volume(v) # Unicamente pueden entrar números flotantes en el intervalo [0, 1]


# ======== Funciones de busqueda canciones ========
def lecturaContenido(r): 
    try: 
        contenido = os.listdir(r) # Obtiene la lista de elementos dentro del directorio
        return contenido
    except FileNotFoundError: 
        raise FileNotFoundError('¡La carpeta no existe!') #Excepción si la carpeta indicada no existe


def compruebaContenido(c): 
    if len(c) > 0: 
        return True
    else: 
        return False


def menuBusquedaCarpeta(): 
    ruta = input('Por favor ingrese la ruta de la carpeta: ')
    canciones = lecturaContenido(ruta) # Guarda nombres de los archivos encontrados en la ruta
    
    bandera = True
    while bandera: 
        # Comprueba si la carpeta esta vacia y si es así, pide una ruta nueva
        if compruebaContenido(canciones) == False: 
            print('ERROR: La carpeta dada se encuentra vacia. \n')
            ruta = input('Por favor, ingrese la ruta de la carpeta: ')
        else: 
            bandera = False

    return (ruta, canciones)


# ======== Funciones de lista de canciones ========
def imprimirListaCanciones(c):
    for i in range(len(c)): 
        print(str(i + 1) + ') ' + c[i])


def eligeCancion(canciones): 
    print('A continuación ingrese el número de la canción que desea reproducir')
    n = int(input('>> '))

    if n == 0: 
        # Elige un número en el rango del numero de elementos en la lista de elementos de la carpeta
        n = choice(range(1, len(canciones) + 1))
    else: 
        # Verifica que el número dado este dentro del rango de la lista
        while True: 
            if n > 0 and n <= len(canciones): 
                break
            else:
                print('ERROR: El número dado esta fuera de rango, por favor ingrese un valor valido: ')
                n = int(input('>> '))
    return n


def menuCanciones(rutaCanciones):
    ruta = rutaCanciones[0]
    canciones = rutaCanciones[1]

    print('\t === ♫ ᴛᴜs ᴄᴀɴᴄɪᴏɴᴇs ♫ === \n')
    print('0) ► ALEATORIO')
    imprimirListaCanciones(canciones)
    n = eligeCancion(canciones)

    print('\n')
    rutaCompleta = ruta + '/' + canciones[n - 1] # Arma la cadena de la ruta completa para el mixer
    reproducirCancion(rutaCompleta)
    return n

# ======== Función de menú de reproductor principal ========
def menuReproductor(): 
    mixer.init() # Inicializa el mixer
    print('\t **** ♬ REPRODUCTOR DE MÚSICA ♬ **** \n')
    rutaCanciones = menuBusquedaCarpeta()

    canciones = rutaCanciones[1]
    bandera = True
    while bandera == True:
        n = menuCanciones(rutaCanciones)
        while True: 
            print('♪ Estas escuchando: ' + canciones[n-1] + ' ♪')
            print(''' 
            0 - Cambiar volumen 
            1 - Pausar. 
            2 - Reanudar.
            3 - Detener y elegir otra canción. 
            4 - Salir.''')
            opcion = int(input(' >> '))
            print('\n')

            if opcion == 0: 
                # Se pide un número de 0 a 10 y este se divide por 10
                vol = float(input('Inserte el volumen donde 0 es el mínimo y 10 es el máximo: '))
                if vol <=10 and vol >= 0:
                    modificarVolumen(vol/10) 
                else:
                    print('ERROR: Valor invalido, intentelo de nuevo.\n')
            elif opcion == 1: 
                pausarCancion()
            elif opcion == 2: 
                reanudarCancion()
            elif opcion == 3: 
                detenerCancion()
                break
            elif opcion == 4: 
                detenerCancion()
                bandera = False
                mixer.quit()
                break
            else: 
                print('ERROR: Ingrese una opción valida')


def main():  
    menuReproductor()


if __name__ == '__main__':
    main()
