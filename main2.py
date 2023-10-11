from classes2 import Tablero
# Esta es la función principal que ejecutará el juego, trabajando con tod lo que he creado en la class Tablero
def main():
    jugador = Tablero("Jugador") #Estos serán mi tablero y el de la máquina
    maquina = Tablero("Máquina")
    jugador.colocar_barcos() # LLñamo al método colocar_barcos para obvio colocar los barcos en cada tablero 
    maquina.colocar_barcos() # E iniciar el juego con los barcos en su lugar

    while True:
        print("\n--- Tablero del Jugador ---")
        jugador.imprimir_tablero()
        print("\n--- Tablero de la Máquina ---")
        maquina.imprimir_tablero()

        coordenadas = input("\nIngresa coordenadas para disparar (ejemplo: A3): ")
        x, y = jugador.parsear_coordenadas(coordenadas)

        resultado = maquina.disparo_coordenada(x, y)

        if resultado == "hundido":
            print("¡Hundiste un barco de la máquina! ¡Ganaste!")
            break
        elif resultado == "tocado":
            print("¡Tocaste un barco de la máquina!")
        elif resultado == "agua":
            print("¡Agua! La máquina esquiva tus disparos.")
        elif resultado == "repetido":
            print("Ya habías disparado en estas coordenadas. Intenta de nuevo.")

        maquina.jugar_turno_maquina()



if __name__ == "__main__":
    main()
