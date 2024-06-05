from Ticket import Ticket

class General(Ticket):

    def __init__(self, ticket_id, match, seat, descuento):
        super().__init__(ticket_id, match, seat)
        self.sub_total = 50
        self.descuento = descuento
        self.iva = (self.sub_total - self.descuento) * 0.16
        self.total = self.sub_total - self.descuento + self.iva

    def show_attr(self):

        return f'''
        
        *** General ***

        Partido: {self.match.local_team.name} VS {self.match.visiting_team.name}
        Fecha: {self.match.date} {self.match.hour}
        
        Ticket_id: {self.ticket_id}
        Asiento: {self.seat}
        
        Sub-total: {self.sub_total}
        Descuento: {self.descuento}
        Iva: {self.iva}
        
        Total: {self.total}
        
        '''
