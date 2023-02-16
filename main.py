print("Bienvenido al juego 'Welcome to the Jungle'. Un videojuego de acción y de elección de ruta en el que deberás escapar de la muerte.\n                        Escoge tu personaje:\n- Warwick (El hombre lobo).\n- neeko (La réptil mágica).\n- Jax (El maestro de armas).")
personaje = input("").lower()

if personaje == "warwick":
    print("Has escogido a 'Warwick'. Este personaje tiene la capacidad de regenerar su vida cuando pelea cuerpo a cuerpo, por lo que te beneficia usar armas blancas.")
    print("\n")
    print("Has aparecido en mitad de un bosque. Tienes para elegir dos caminos. Derecha e izquierda. ¿Cúal eliges?")
    camino = input("")
    
    if camino == "derecha":
        print("Has elegido el camino de la derecha. En este sendero te encuentras a un Monstruo que te impide el paso. Desconoces su nivel de duerza. ¿Peleas o vuelves por dónde has venido?")
        print("- Pelear\n- Volver")
        decision = input("").lower()
        if decision == "pelear":
          print("Peleas, pero el Monstruo es más fuerte que tu por lo que tras una ardua pelea caes desfallecido por el cansancio.")
          print("GAME OVER")

        if decision == "volver":
          print("Intentas retroceder pero ese Monstruo es más rápido que tu. Te alcanza y te mata.")
          print("GAME OVER")    
    if camino == "izquierda":
        print("Has elegido el camino de la izquierda. En este sendero tras andar varios km sin obtener señal de vida, te encuentras con una pequeña niña. Esta te pide que la sigues, y así lo haces. Tras una larga caminata os adentrais dentro de una cueva donde descubres que aquella niña a la que decidiste seguir te ha engañado y te ha llevado a una trampa.\'n5 rizes' se encuentran allí para que libres batalla con ellos. Tienes para elegir entre varias armas. ¿Cúal eliges? ")
        print("\n- pistola\n- cuchillo\n- ametralladora")
    gun1 = input("")
    if gun1 == "pistola":
      print("Has escogido la pistola, pero esta solo tiene una bala. Por lo que tras agotar la única munición que tienes solo te queda pelear cuerpo a cuerpo. Por desgracia estas debilitado tras haber tenido que andar durante tanto tiempo sin probar bocado. Debido a esto mueres")
      print("GAME OVER")
    if gun1 == "cuchillo":
      print("Has elegido pelear con el cuchillo como un valiente. Gracias a esto te beneficias de tu pasiva de recuperar vida cada vez que te encuentras en una situación de cuerpo a cuerpo.")
      print("GOOD ENDING")

    if gun1 == "ametralladora":
      print("Tras escoger la ametralladora te das cuenta de que esta no tiene munición por lo que asumes tu muerte y dejas que te maten.")
      print("GAME OVER")