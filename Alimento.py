from Productos import Productos

class Alimento(Productos):

    def __init__(self, name, quantity, tipo, price, formato):
        super().__init__(name, quantity, tipo, price)
        self.formato = formato

    def show_attr(self):

        return f'''
        
        Nombre: {self.name}
        Inventario: {self.quantity}
        Tipo: {self.tipo}
        Price: {self.price}
        Formato: {self.formato}

        '''