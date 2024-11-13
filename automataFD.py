"""Deterministic Finit State M (DFSM)"""
class automataFD:

    def __init__(self) :
        """"Inicializar la quintupla para el DFSM"""
        self.Q = self.definir_estados()
        self.SIGMA = self.definir_alfabeto()
        self.DELTA = self.definir_transicion()
        self.START_STATE, self.ACCEPT_STATES = self.set_start_accept()
        self.EstadoActual = None

    def set_start_accept(self):
        """Pedir al usuario el START_STATE y los ACCEPT_STATES. Validar que están en Q"""
        while (True):
            start = input("Dame el estado inicial del Autómata: ")
            accept = input('Dame el o los estados de aceptación: ').split()
            #Asegurate que los estados proporcionados por el usuario son válidos
            if(start in self.Q ) and (set(accept).issubset(set(self.Q))):
                return start,accept
            else:
                print("Favor de proporcionar estados estados inicial y finales válidos que deben estar en Q:{}.".format(self.Q))

    def definir_estados(self):
        """Pedir al usuario el conjunto de esta Q"""
        Q_in = input("Dame el conjunto de estado, separados por espacios en blanco: ").split()
        print("STATES : {}".format(Q_in))
        return Q_in

    def definir_alfabeto(self):
        """Pedir al usuario el alfabeto(SIGMA) del automata """
        SIGMA_in = input("Dame el alfabeto del automata, separados por espacios en blanco: ").split()
        print("ALPHABET : {}".format(SIGMA_in))
        return SIGMA_in

    def definir_transicion(self):
        """Crear las funciónes de transición(Q x SIGMA) del automata"""
        transi_dict = {q:{a:"JACHI" for a in self.SIGMA} for q in self.Q}

        for key, dic_val in transi_dict.items():
            print("Estoy en el estado {}. Escribir JACHI si no existe un estado de transicion ".format(key))
            for alphabet_in, transi_state in dic_val.items():
                transi_dict[key][alphabet_in] = input("Estoy en {} y veo {} a que estado voy: ".format(key,alphabet_in))

        print("TRANSITION FUNCTION Q X SIGMA -> Q ")
        print("CURRENT STATE \t INPUT ALPHABET \t NEXT STATE")
        for key, dic_val in transi_dict.items():
            for alphabet_in, transi_state in dic_val.items():
                print("\t{} \t {} \t {}".format(key,alphabet_in,transi_state))
        return transi_dict
    
    def checar_estado_aceptacion(self):
        """Verifica si el estado actual pertenece a F"""
        if self.EstadoActual in self.ACCEPT_STATES:
            return True
        else:
            return False 
    
    def recorrer_automata(self, w):
        """Recorre el automata para ver si w llega a un estado final"""
        self.EstadoActual = self.START_STATE
        for x in w:
            self.EstadoActual = self.DELTA[self.EstadoActual][x]
            if(self.EstadoActual == "JACHI"):
                return False
        return self.checar_estado_aceptacion()

if __name__ == "__main__":
    print("Automata de estado finito determinista")
    m = automataFD()
    input_w = list(input("Proporcione la cadena: "))
    print(input_w, type(input_w))
    print("Cadena aceptada" if m.recorrer_automata(input_w) else "Cadena rechazada")