from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    iguales = player == ai
    resultado = "Perdiste!"
    if iguales == True:
        resultado = "Empate!"
    else:
        if player == "Piedra":
            if ai == "Tijeras":
                resultado = "Ganaste!"
        elif player == "Papel":
            if ai == "Piedra":
                resultado = "Ganaste!"
        elif player == "Tijeras":
            if ai == "Papel":
                resultado = "Ganaste!"

    return resultado

# Entry Point
def Game():
    # Generamos un valor aleatorio para la ai
    ai = options[randint[0, 2]]
    
    # Obtenemos la opción del usuario
    player = input("Piedra, Papel o Tijeras? ")

    winner = quienGana(player, ai)

    print(winner)
