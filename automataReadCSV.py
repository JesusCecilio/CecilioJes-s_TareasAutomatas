import csv

class automataReadCSV:
    """Inicializar la quintupla de los datos desde un archivo CSV"""
    def __init__(self, file_csv):
        self.Q, self.SIGMA, self.DELTA, self.START_STATE, self.ACCEPT_STATES = self.readcsv(file_csv)
        self.EstadoActual = None

    """Leer el archivo CSV y obtener los Q, SIGMA, DELTA, START_STATE y ACCEPT_STATE"""
    def readcsv(self, file_csv):
        Q = []
        SIGMA = []
        DELTA = {}
        START_STATE = None
        ACCEPT_STATES = []

        try:
            with open(file_csv, mode='r') as file:
                reader = csv.reader(file)
                header = next(reader)
                SIGMA = header[1:]  

                for row in reader:
                    state= row[0]
                    tran = row[1:]

                    if state.startswith('+'):
                        START_STATE = state[1:]
                        state= state[1:]
                    if state.startswith('*'):
                        ACCEPT_STATES.append(state[1:])
                        state= state[1:]
                    if state.startswith('+*'):
                        START_STATE = state[2:]
                        ACCEPT_STATES.append(state[2:])
                        state= state[2:]

                    Q.append(state)
                    DELTA[state] = {SIGMA[i]: tran[i] for i in range(len(SIGMA))}

            print(f"STATES (Q): {Q}")
            print(f"ALPHABET: {SIGMA}")
            print(f"START STATE: {START_STATE}")
            print(f"ACCEPT STATES: {ACCEPT_STATES}")
            print(f"TRANSITIONS: {DELTA}")

            return Q, SIGMA, DELTA, START_STATE, ACCEPT_STATES
        
        except FileNotFoundError:
            print("Archivo no encontrado")
            raise

    """Verificación de si el EstadoActual es un estado de aceptación"""
    def verificacion(self):
        return self.EstadoActual in self.ACCEPT_STATES

    def precesarCadena(self, w):
        self.EstadoActual = self.START_STATE
        for x in w:
            if x in self.DELTA[self.EstadoActual]:
                self.EstadoActual = self.DELTA[self.EstadoActual][x]
            else:
                return False
            
            if self.EstadoActual == "NO":
                return False
            
        return self.verificacion()

def menu():
    AFD = None

    while True:
        print("\nOpciones a elejir:")
        print("1. Leer el archivo CSV")
        print("2. Probar con otra cadena")
        print("3. Exit")

        opcion = input("\nSeleciona una opción: ").upper()

        match opcion:
            case '1':
                archivo_csv = input("\nProporcione el nombre del archivo CSV: ")
                try:
                    AFD = automataReadCSV(archivo_csv)
                    input_w = list(input("\nProporcione la cadena a usar: "))
                    resultado = AFD.precesarCadena(input_w)
                    print("\nCadena aceptada" if resultado else "\nCadena rechazada")
                except FileNotFoundError:
                    print("\nArchivo no encontrado. Verifique el nombre y vuelva a intentarlo.")
            case '2':
                if AFD:
                    input_w = list(input("\nProporcione la nueva cadena: "))
                    resultado = AFD.precesarCadena(input_w)
                    print("\nCadena aceptada" if resultado else "\nCadena rechazada")
                else:
                    print("\nPrimero debe cargar un archivo CSV con la opción 1.")
            case '3':
                print("\nExit")
                break
            case _:
                print("\nOpción inválida, por favor elige entre 1, 2 o 3.")

if __name__ == "__main__":
    print("\nProcesador de cadenas con autómata determinista\n")
    menu()
