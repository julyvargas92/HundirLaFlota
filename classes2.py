import random
""" La clase Tablero es el centro del juego.
En crear_tablero, inicializamos una matriz vacía que creará el tablero con "-" para el agua y "O" para los barcos
Con el método disparo_coordenada, se debería actualizar el tablero y avisar la situación resultante del disparo
Colocar_barcos utiliza un diccionario para definir el tamaño de los barcos y colocarlos en el tablero de manera aleatoria


"""
class Tablero:
    def __init__(self, id_jugador):
       
        self.id_jugador = id_jugador
        # Con esta tupla como atributo defino las dimensiones del tablero
        self.dimensiones = (10, 10)
        # Un atributo que llama a la creación del tablero desde el momento en el que se usa la clase
        self.tablero = self.crear_tablero()
        self.colocar_barcos() # Este método se llama desde el constructos automaticamente para colocar los barcos en la board.
        # Matrices para rastrear los disparos de la máquina y del jugador
        # El tablero se inicializa con "---" para indicar que no se ha hecho disparo en esas posiciones
        self.tablero_maquina = [["---" for _ in range(self.dimensiones[1])] for _ in range(self.dimensiones[0])]
        self.tablero_disparos = [["___" for _ in range(self.dimensiones[1])] for _ in range(self.dimensiones[0])]
        self.barcos_colocados = []

    def crear_tablero(self):
        tablero = []
        for _ in range(self.dimensiones[0]):
            fila = ["~"] * self.dimensiones[1]
            tablero.append(fila)
        return tablero

    def imprimir_tablero(self):
        print("  A B C D E F G H I J")
        for i, fila in enumerate(self.tablero):
            fila_str = " ".join(fila)
            print(f"{i + 1} {fila_str}")

    def disparo_coordenada(self, x, y):
        if self.tablero[x][y] == "B":
            self.tablero_disparos[x][y] = "X"  # Marcar como "tocado"
            if all(self.tablero_disparos[i][j] == "X" for i in range(self.dimensiones[0]) for j in range(self.dimensiones[1])):
                return "hundido"  # Si todos los barcos han sido hundidos
            return "tocado"  # Si el disparo acertó
        elif self.tablero_disparos[x][y] == "X":
            return "repetido"  # Si el disparo ya se hizo en esa coordenada
        else:
            self.tablero_disparos[x][y] = "O"  # Marcar como "agua"
            return "agua"  # Si el disparo falló
# Con este método me debería reconocer las coordenadas en formato letra número A3
    def formato_coordenadas(self, coordenadas):
        x = ord(coordenadas[0].upper()) - 65
        y = int(coordenadas[1:]) - 1
        return x, y
# Colocarem
    def colocar_barcos(self):
        barcos = {
            "barco1": 1,
            "barco2": 2,
            "barco3": 3,
            "barco4": 4
        }

        for nombre_barco, eslora in barcos.items():
            print(f"Colocando {nombre_barco} ({eslora} posiciones)")
            for _ in range(eslora):
                while True:
                    x = random.randint(0, 9)
                    y = random.randint(0, 9)
                    if self.tablero[x][y] == "~":
                        self.tablero[x][y] = nombre_barco[0]
                        break

    def jugar_turno_maquina(self):
        x = random.randint(0, self.dimensiones[0] - 1)
        y = random.randint(0, self.dimensiones[1] - 1)

        if self.tablero[x][y] != "~":
            print("La máquina tocó uno de tus barcos.")
            self.tablero[x][y] = "X"
        else:
            print("La máquina falló.")


