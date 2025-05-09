import random

def get_computer_choice():
  return random.choice(['Piedra', 'Papel', 'Tijera'])

def determine_winner(player_choice, computer_choice):
  if player_choice == computer_choice:
    return "Empate"
  elif (player_choice == 'Piedra' and computer_choice == 'Tijera') or \
       (player_choice == 'Papel' and computer_choice == 'Piedra') or \
       (player_choice == 'Tijera' and computer_choice == 'Papel'):
    return "¡Ganaste!"
  else:
    return "Perdiste. La próxima vez será :["

while True:
  player_choice = input("¿Qué elegís? Escribí Piedra, Papel o Tijera (o 'salir' para terminar): ").capitalize()

  if player_choice.lower() == 'salir':
    break 

  if player_choice not in ['Piedra', 'Papel', 'Tijera']:
    print("Entrada inválida. Por favor, elige Piedra, Papel o Tijera.")
    continue 

  computer_choice = get_computer_choice()
  result = determine_winner(player_choice, computer_choice)
  print(f"{computer_choice}. {result}")
