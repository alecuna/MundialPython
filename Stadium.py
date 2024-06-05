class Stadium():

    def __init__(self, name, capacity, location, id, restaurants):
        self.name = name
        self.capacity = capacity
        self.location = location
        self.id = id
        self.restaurants = restaurants


    def show_attr(self):

        return(f'''
        
        Nombre: {self.name}
        Capacidad: {self.capacity}
        Ubicacion: {self.location}
        id: {self.id}

        ''')


    def map(self, taken, i):

        asientos = self.capacity[i]

        for a in range(int(asientos/10)):
            fila = ["(x)" if f"{a}{b}" in taken else "( )" for b in range(10)]
            print(" ".join(fila))
