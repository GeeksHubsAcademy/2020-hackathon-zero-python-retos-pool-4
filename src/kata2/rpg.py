#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen=10):
    resultado = ""
    letras = string.ascii_letters
    digitos = string.digits
    signosDePuntuacion = string.punctuation
    
    # Generamos una contrseña simplemente de letras
    n = 0
    while n < passLen:
        resultado += random.choice(letras)

        n += 1

    # Le añadimos un digito y un singo de puntuación siempre y cuando la longitud de la contraseña es mayor/igual a 3
    if passLen >= 3:
        # Vamos a calcular en que posiciones ponemos el dígito y  el signo de puntuación
        indices = [0, 0]
        # Calculamos la primera posición
        indices[0] = random.randint(1, passLen - 1)
        # Calculamos la segunda posición
        # No queremos la primera y no queremos que pisemos la del dígito
        while indices[1] == 0 or indices[1] == indices[0]:
            indices[1] = random.randint(1, passLen - 1)
        
        # Reemplazamos dichas posiciones
        tmpResultado = list(resultado)
        tmpResultado[indices[0]] = random.choice(digitos)
        tmpResultado[indices[1]] = random.choice(signosDePuntuacion)

        # Volvemos a asignar el resultado
        resultado = "".join(tmpResultado)    

    return resultado