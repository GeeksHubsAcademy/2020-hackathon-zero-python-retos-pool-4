#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen=10):
    resultado = ""
    letras = string.ascii_letters
    digitos = string.digits
    signosDePuntuacion = string.punctuation
    
    n = 0
    while n < passLen:
        resultado += random.choice(letras)

        n += 1

    return resultado
