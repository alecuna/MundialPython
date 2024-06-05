from Productos import Productos

class Bebida(Productos):

    def __init__(self, name, quantity, tipo, price, alcoholica):
        super().__init__(name, quantity, tipo, price)
        self.alcoholica = alcoholica

    def show_attr(self):

        return f'''
        
        Nombre: {self.name}
        Inventario: {self.quantity}
        Tipo: {self.tipo}
        Price: {self.price}
        Alcoholica: {self.alcoholica}

        '''