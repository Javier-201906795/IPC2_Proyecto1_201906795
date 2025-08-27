class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaSimple:
    def __init__(self):
        self.inicio = None
        self.tamanio = 0

    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.inicio is None:
            self.inicio = nuevo_nodo
        else:
            cursor = self.inicio
            while cursor.proximo:
                cursor = cursor.proximo
            cursor.proximo = nuevo_nodo
        self.tamanio += 1

    def obtener(self, posicion):
        if posicion < 0 or posicion >= self.tamanio:
            return None
        cursor = self.inicio
        for _ in range(posicion):
            cursor = cursor.proximo
        return cursor.valor

    def encontrar_posicion(self, id_objetivo):
        # Devuelve la posición de un nodo cuyo dato tenga atributo "id"
        cursor = self.inicio
        pos = 0
        while cursor:
            if hasattr(cursor.valor, 'id') and cursor.valor.id == id_objetivo:
                return pos
            cursor = cursor.proximo
            pos += 1
        return -1