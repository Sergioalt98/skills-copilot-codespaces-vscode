import random

while True:
    # Pedir al usuario que ingrese su elección
    user_choice = input("Elige piedra, papel o tijera en minúsculas: ")

    # Verificar si la elección del usuario está en minúsculas
    while user_choice.islower() == False:
        user_choice = input("Por favor, ingresa tu elección en minúsculas: ")

    # Generar aleatoriamente la elección del oponente
    options = ["piedra", "papel", "tijera"]
    opponent_choice = random.choice(options)

    # Comparar las elecciones del usuario y del oponente
    if user_choice == opponent_choice:
        result = "Empate"
    elif user_choice == "piedra" and opponent_choice == "tijera":
        result = "Ganaste"
    elif user_choice == "papel" and opponent_choice == "piedra":
        result = "Ganaste"
    elif user_choice == "tijera" and opponent_choice == "papel":
        result = "Ganaste"
    else:
        result = "Perdiste"

    # Imprimir el resultado del juego
    print(f"Elegiste {user_choice} y el oponente eligió {opponent_choice}. {result}!")
    
    # Preguntar al usuario si desea seguir jugando
    play_again = input("¿Quieres seguir jugando? (s/n): ")
    if play_again.lower() != "s":
        break
