class Match():

    def __init__(self, local_team, visiting_team, date, hour, location):
        self.local_team = local_team
        self.visiting_team = visiting_team
        self.date = date
        self.hour = hour
        self.location = location
        self.seats_vip = []
        self.seats_general = []
        self.asistencia = []

    def show_attr(self):

        return(f'''
        
    ---{self.local_team.name} VS {self.visiting_team.name}---

    Equipo local: {self.local_team.show_attr()}
    Equipo visitante: {self.visiting_team.show_attr()}
    Estadio: {self.location.show_attr()}
    Fecha: {self.date} {self.hour}
        
        ''')