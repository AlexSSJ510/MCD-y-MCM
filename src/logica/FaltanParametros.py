class FaltanParametros(Exception):
    def __init__(self, mensaje="Se requieren al menos dos números para realizar la operación."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)