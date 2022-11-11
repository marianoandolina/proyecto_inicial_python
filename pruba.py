letras_usadas = ['d', 'a', 'c', 'f', 'e', 'o']
palabra_secreta = 'dado'

def validar_palabra(letras_usadas, palabra_secreta):
    verificar = len(palabra_secreta)
    salida = verificar
    while salida > 0:
        for letra in palabra_secreta:
            if letra not in letras_usadas:
                print('No se adivino la palabra')
                break
            else:
                salida -= 1

validar_palabra(letras_usadas, palabra_secreta)