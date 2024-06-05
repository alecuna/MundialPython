class Team():

    def __init__(self, name, fifa_code, group):
        self.name = name
        self.fifa_code = fifa_code
        self.group = group

    def show_attr(self):

        return(f'''
        
        Nombre: {self.name}
        Codigo FIFA: {self.fifa_code}
        Grupo: {self.group}
        
        ''')