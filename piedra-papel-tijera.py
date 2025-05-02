       # JUEGO PIEDRA PAPEL O TIJERA
import random
def movimiento_compu():
  mov_random = random.random()
  if mov_random < 1/3:
    mov_compu = "Piedra"
  elif mov_random <= 2/3:
    mov_compu = "Papel"
  elif mov_random > 2/3:
    mov_compu = "Tijera"

  return mov_compu

mov_humano = input("¿Qúe elegís? Escribí Piedra, Papel o Tijera: ").capitalize()
mov_compu = movimiento_compu()

if mov_humano == "Piedra": 
  if mov_compu == "Piedra":
    print("Piedra. ¡Empate!")
  elif mov_compu == "Papel":
    print("Papel. Perdiste. La próxima vez será :[")
  elif mov_compu == "Tijera":
    print("Tijera. ¡Ganaste! ")

elif mov_humano == "Papel":
  if mov_compu == "Piedra":
    print("Piedra. ¡Ganaste!")
  elif mov_compu == "Papel":
    print("Papel. Empate.")
  elif mov_compu == "Tijera":
    print("Tijera. Perdiste. La próxima vez será :[")

elif mov_humano == "Tijera":
  if mov_compu == "Piedra":
    print("Piedra. Perdiste. La próxima vez será :[")
  elif mov_compu == "Papel":
    print("Papel. ¡Ganaste!")
  elif mov_compu == "Tijera":
    print("Tijera. Empate.")



  
