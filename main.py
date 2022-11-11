import csv
import random
import interfaz


# def add_word(word):
#     with open('palabras.csv', 'r') as csvfile:
#         words = list(csv.DictReader(csvfile))

def leer_palabra_secreta(palabra): # FUNCION COMPLETADA, FUNCIONA BIEN.
    with open('palabras.csv', 'r') as csvfile:
        data = list(csv.DictReader(csvfile))
        lista_de_palabras = []
        for i in range(len(data)):
            words = data[i]
            lista_de_palabras.append(words['palabras'])
    palabra_secreta = random.choice(lista_de_palabras)
    
    return palabra_secreta

def pedir_letra(letras_usadas): # FUNCION COMPLETADA, FUNCIONA BIEN
    while True:
        letra = input('Ingreses una letra: ')
        letra = letra.lower()
        if letra in letras_usadas:
            continue
        elif len(letra) > 1:
            print('Ingrese una sola letra')
            continue        
        else:
            letras_usadas.append(letra)
            return letra
            break
    
def verificar_letra(letra, palabra_secreta):
    if letra in palabra_secreta:
        return True
    else:
        return False    

def validar_palabra(letras_usadas, palabra_secreta):
    verificar = len(palabra_secreta)
    salida = verificar
    while salida > 0:
        for letra in palabra_secreta:
            if letra not in letras_usadas:
                print('No se adivino la palabra')
                return False
                break
            else:
                salida -= 1
    return True            

            


    




if __name__ == "__main__":
    print("\n¡Aquí comienza el juego del ahorcado!\n")
    # Inicializo las variables y listas a utilizar.
    max_cantidad_intentos = 7
    intentos = 0
    letras_usadas = []
    es_ganador = False

    # Leer la palabra secreta de un archivo csv.
    palabra_secreta = leer_palabra_secreta('palabras.csv')
    
    # Esto se realiza para que el jugador pueda ver al principio
    # la cantidad de letras de la palabra a adivinar.
    interfaz.dibujar(palabra_secreta, letras_usadas, intentos)
    
    while intentos < max_cantidad_intentos == 7 and not es_ganador:
        # Pedir una nueva letra
        letra = pedir_letra(letras_usadas)

        # Verificar si la letra es parte de la palabra secreta        
        if verificar_letra(letra, palabra_secreta) == False:
            # En caso de no estar la letra ingresada en la palabra
            # a adivinar incremento en 1 la variable intentos.
            intentos += 1
        
        # Dibujar la interfaz
        interfaz.dibujar(palabra_secreta, letras_usadas, intentos)

        # Validar si la palabra secreta se ha adivinado
        if validar_palabra(letras_usadas, palabra_secreta) == True:
            es_ganador = True
            break

    if es_ganador:
        print(f'\n¡Usted ha ganado la partida!, palabra secreta {palabra_secreta}!\n')
    else:
        print('\n¡Ahorcado!')
        print(f'\n¡Usted ha perdido la partida!, palabra secreta {palabra_secreta}!\n')