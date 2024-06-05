class Productos:

    def __init__(self, name, quantity, tipo, price):
        self.name = name
        self.quantity = quantity
        self.tipo = tipo
        self.price = price

    def show_attr(self):

        return f'''
        
        Nombre: {self.name}
        Inventario: {self.quantity}
        Tipo: {self.tipo}
        Price: {self.price}

        '''