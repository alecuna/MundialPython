class Ticket():

    def __init__(self, ticket_id, match, seat):

        self.ticket_id = ticket_id
        self.match = match
        self.seat = seat

    def show_attr(self):

        return f'''

        Partido: {self.match.local_team} VS {self.match.visiting_team}
        Fecha: {self.match.date} {self.match.hour}
        
        Ticket_id: {self.ticket_id}
        Seat: {self.seat}
        
        '''