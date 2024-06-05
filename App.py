import pickle
import requests
from itertools import permutations
from Team import Team
from Match import Match
from Stadium import Stadium
from Client import Client
from Ticket import Ticket
from General import General
from Vip import Vip
from Bebida import Bebida
from Alimento import Alimento
from Restaurant import Restaurant
from Factura import Factura


class App():

    def __init__(self):
        self.matches = []
        self.teams = []
        self.stadiums = []
        self.clients = []
        self.tickets = []

    # API functions

    def api_matches(self):

        url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/matches.json"
        response = requests.request("GET", url)
        return response.json()

    def api_teams(self):

        url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/teams.json"
        response = requests.request("GET", url)
        return response.json()

    def api_stadiums(self):

        url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/stadiums.json"
        response = requests.request("GET", url)
        return response.json()


    # Inicio
    def inicio(self):
        
        '''
        Da la opcion de iniciar con la creacion de los objetos a partir de la api o de leer los archivos txt creados en sesiones anteriores
        '''

        op_inicio = input("1. Iniciar una nueva sesion \n2. Continuar con los datos existentes\n")
        while not op_inicio.isnumeric() or int(op_inicio) < 1 or int(op_inicio) > 2:
            op_inicio = input("1. Iniciar una nueva sesion \n2. Continuar con los datos existentes\n")

        if int(op_inicio) == 1:
            self.create_obj()
            self.menu()

        elif int(op_inicio) == 2:
            try:
                self.matches = pickle.load(open("matches.txt", "rb"))
            except EOFError:
                self.matches = list()
            try:
                self.stadiums = pickle.load(open("stadiums.txt", "rb"))
            except EOFError:
                self.stadiums = list()
            try:
                self.teams = pickle.load(open("teams.txt", "rb"))
            except EOFError:
                self.teams = list()
            try:
                self.clients = pickle.load(open("clients.txt", "rb"))
            except EOFError:
                self.clients = list()
            try:
                self.tickets = pickle.load(open("tickets.txt", "rb"))
            except EOFError:
                self.tickets = list()
            self.menu()

    # MENU
    def menu(self):

        '''
        Funcion menu que inicia el programa con la creacion de los objetos a partir de la API o de los archivos txt
        '''

        while True:

            print('''
        
      _,...,_
    .'@/~~~\@'.
   //~~\___/~~\\
  |@\__/@@@\__/@|   ¡Bienvenidos al mundial 
  |@/  \@@@/  \@|         Qatar 2022!
   \\__/~~~\__//
    '.@\___/@.'  
      `"""""`
        
1. Buscar partidos
2. Registrar
3. Comprar entradas
4. Confirmar asistencia
5. Restaurante
6. Estadisticas
7. Salir y guardar
        
            ''')

            op_menu = input("Ingrese una opcion valida: ")
            while not op_menu.isnumeric() or int(op_menu) < 1 or int(op_menu) > 7:
                op_menu = input("Error. Ingrese una opcion valida: ")

            # option for search functions
            if int(op_menu) == 1:
                
                print('''
    
1. Buscar por pais
2. Buscar por estadio
3. Buscar por fecha
    
                ''')

                op_search = input("Ingrese una opcion valida: ")
                while not op_search.isnumeric() or int(op_search) < 1 or int(op_search) > 3:
                    op_search = input("Error. Ingrese una opcion valida: ")

                if int(op_search) == 1:
                    self.search_by_country()

                elif int(op_search) == 2:
                    self.search_by_stadium()

                elif int(op_search) == 3:
                    self.search_by_date()

            #register client function
            elif int(op_menu) == 2:
                self.register_client()

            #check user and buy tickets
            elif int(op_menu) == 3:
                self.check_user()

            #confirmar asistencia al partido
            elif int(op_menu) == 4:
                self.asistencia()

            #compra y busqueda en el restaurante
            elif int(op_menu) == 5:
                self.manage_rest()

            #mostrar todas las estadisticas
            elif int(op_menu) == 6:
                self.estadisticas()
            
            #guardar datos en archivos txt
            elif int(op_menu) == 7:
                pickle.dump(self.matches, open("matches.txt", "wb"))
                pickle.dump(self.stadiums, open("stadiums.txt", "wb"))
                pickle.dump(self.teams, open("teams.txt", "wb"))
                pickle.dump(self.clients, open("clients.txt", "wb"))
                pickle.dump(self.tickets, open("tickets.txt", "wb"))
                break
    
    def create_obj(self):
        
        '''
        Crea objetos para teams, matches y stadiums a partir de la informacion descargada de la API. Estos objetos se guardan en las listas del innit
        '''

        teams = self.api_teams()
        matches = self.api_matches()
        stadiums = self.api_stadiums()


        # TEAMS creacion objetos
        for team in teams:
            for key, value in team.items():
                current_team = Team(team["name"], team["fifa_code"], team["group"])
            self.teams.append(current_team)


        
        # STADIUMS Y RESTAURANTES creacion objetos
        for stadium in stadiums:
            restaurantes = []
            for restaurant in stadium["restaurants"]:
                productos = []
                for products in restaurant["products"]:
                    for key, value in products.items():
                        name = products["name"]
                        quantity = products["quantity"]
                        price = products["price"]
                        tipo = products["type"]
                    if tipo == "beverages":
                        if products["adicional"] == "alcoholic":
                            alcoholica = True
                        else:
                            alcoholica = False
                        current_product = Bebida(name, quantity, tipo, price, alcoholica)
                    elif tipo == "food":
                        formato = products["adicional"]
                        current_product = Alimento(name, quantity, tipo, price, formato)

                    productos.append(current_product)
                current_restaurant = Restaurant(restaurant["name"], productos)
                restaurantes.append(current_restaurant)

                current_stadium = Stadium(stadium["name"], stadium["capacity"], stadium["location"], stadium["id"], restaurantes)
            self.stadiums.append(current_stadium)
            
    
        #  MATCHES creacion objetos
        for match in matches:
            for key, value in match.items():
                for team in self.teams:
                    if match["home_team"] == team.name:
                        home_team = team
                    if match["away_team"] == team.name:
                        away_team = team
                for stadium in self.stadiums:
                    if match["stadium_id"] == stadium.id:
                        play_stadium = stadium
                list_date = match["date"].split(" ")
                date = list_date[0]
                hour = list_date[1]
                current_match = Match(home_team, away_team, date, hour, play_stadium)
            self.matches.append(current_match)


    # buscadores
    def search_by_country(self):

        '''
        Buscador de partidos por pais
        '''
        
        print("*** Paises ***")
        print()
        for i, team in enumerate(self.teams):
            print(f"{i+1}. {team.name}")

        while True:
            try:
                found = False
                op_country = input("Ingrese el nombre del pais: ").capitalize()
                for team in self.teams:
                    if op_country == team.name:
                        found = True
                        break
                if found == False:
                    raise Exception
                else:
                    break
            except:
                print("Ingreso invalido. Intente de nuevo!")

        if found:
            for match in self.matches:
                if match.local_team.name == op_country:
                    print(match.show_attr())
    
                if match.visiting_team.name == op_country:
                    print(match.show_attr())


    def search_by_stadium(self):

        '''
        Buscador de partidos por estadio
        '''

        print("*** Stadios ***")
        print()
        for stadium in self.stadiums:
            print(f'''
            ID: {stadium.id} 
            Estadio: {stadium.name}
            ''')

        while True:
            try:
                found = False
                op_location = input("Ingrese el ID del estadio: ")
                while not op_location.isnumeric() or int(op_location) < 1 or int(op_location) > 8:
                    raise Exception
                for stadium in self.stadiums:
                    if stadium.id == int(op_location):
                        found = True
                        break
                if found == False:
                    raise Exception
                else:
                    break
            except:
                print("Ingreso invalido. Intente de nuevo!")

        if found:
            for match in self.matches:
                if match.location.id == int(op_location):
                    print(match.show_attr())
    

    def search_by_date(self):

        '''
        Buscador de partidos por fecha
        '''

        print("*** Fechas disponibles ***")
        print("11/21/2022 -- 12/2/2022")

        while True:
            try:
                found = False
                op_date = input("Indique la fecha del partido en el formato mm/d/aaaa: ")
                
                for match in self.matches:
                    if match.date == op_date:
                        found = True
                        print(match.show_attr())
                if found == False:
                    raise Exception
                else:
                    break
            except:
                print("Ingreso invalido. Intente de nuevo!")
        
    
    # registro usuario
    def register_client(self):

        '''
        Registrar al cliente y crear objeto "Cliente"
        '''

        name = input("Nombre: ").capitalize()
        while name.isnumeric():
            name = input("Ingreso invalido. Nombre: ").capitalize()

        dni = input("Cedula: ")
        while not dni.isnumeric() or len(dni) > 9 or int(dni) < 1:
            dni = input("Ingreso invalido. Cedula: ")
        for client in self.clients:
            if dni == client.dni:
                print("El cliente ya se encuentra registrado.")
                self.menu()

        age = input("Edad: ")
        while not age.isnumeric() or int(age) < 1 or int(age) > 100:
            age = input("Ingreso invalido. Edad: ")

        current_client = Client(name, dni, age)
        self.clients.append(current_client)
        print("\nUsuario registrado exitosamente!\n")


    # checkear usuario
    def check_user(self):

        '''
        Funcion para chequear si la cedula ya esta registrada. Se usa antes de comprar las entradas y en ella se llama la funcion "buy_tickets()"
        '''

        # objeto client
        client_dni = input("Ingrese la cedula del usuario: ")
        while not client_dni.isnumeric() or len(client_dni) > 9 or int(client_dni) < 1:
            client_dni = input("Error. Ingrese la cedula del usuario: ")
        
        for client in self.clients:
            if client_dni == client.dni:
                self.buy_ticket(client_dni)
            else:
                print("El usuario no se encuentra registrado")


    # compra tickets
    def buy_ticket(self, client_dni):

        '''
        Comprar las entradas para los partidos. Se crean objetos de tipo vip o general
        '''

        #ticket_id
        ticket_id = (len(self.tickets)+1)

        #match selection
        for i, match in enumerate(self.matches):
            print(f"***{i+1}***\n")
            print(match.show_attr())

        op_match = input("Ingrese el numero correspodiente al partido que desea atender: ")
        while not op_match.isnumeric() or int(op_match) > len(self.matches) or int(op_match) < 1:
            op_match = input("Error. Ingrese el numero correspodiente al partido que desea atender: ")
        
        match = self.matches[int(op_match)-1]

        for client in self.clients:
            if client_dni == client.dni:
                for ticket in client.tickets:
                    if match == ticket.match:
                        op_match = input("Error. Usted ya compro una entrada para este partido: ")
                        match = self.matches[int(op_match)-1]

        #general o VIP
        op_ticket = input("Ingrese 'G' para adquirir una entrada general o 'V' para adquirir una entrada VIP: ").upper()
        while not op_ticket == 'G' and not op_ticket == 'V':
            op_ticket = input("Error. Ingrese 'G' para adquirir una entrada general o 'V' para adquirir una entrada VIP: ").upper()


        if op_ticket == "G":

            #descuentos
            descuento = 0
            # if self.vampiro(client_dni):
            #     descuento = 50/2

            #seats
            taken_seats = match.seats_general

            i = 0
            match.location.map(taken_seats, i)

            chosen_seat = input("Ingrese el numero de asiento que desea: ")
            while not chosen_seat.isnumeric() or chosen_seat in taken_seats:
                chosen_seat = input("Este asiento ya esta ocupado. Ingrese el numero de asiento que desea: ")

            ticket = General(ticket_id, match, chosen_seat, descuento)
            print(ticket.show_attr())

        elif op_ticket == "V":

            #descuentos
            descuento = 0
            # if self.vampiro(client_dni):
            #     descuento = 120/2
            # else:
            #     descuento = 0

            #seats
            taken_seats = match.seats_vip

            i = 1
            match.location.map(taken_seats, i)

            chosen_seat = input("Ingrese el numero de asiento que desea: ")
            while not chosen_seat.isnumeric() or chosen_seat in taken_seats:
                chosen_seat = input("Este asiento ya esta ocupado. Ingrese el numero de asiento que desea: ")

            ticket = Vip(ticket_id, match, chosen_seat, descuento)
            print(ticket.show_attr())


        #confirmacion
        op_buy = input("Desea proceder con la compra de entradas?\n1. Si\n2. No\n")

        while not op_buy.isnumeric() or int(op_buy) < 1 or int(op_buy) > 2:
            op_buy = input("Error.Ingreso invalido. Desea proceder con la compra de entradas?\n1. Si\n2.No\n")

        if int(op_buy) == 1:
            self.tickets.append(ticket)

            if isinstance(ticket, General):
                match.seats_general.append(chosen_seat)
            elif isinstance(ticket, Vip):
                match.seats_vip.append(chosen_seat)
            
            for client in self.clients:
                if client_dni == client.dni:
                    client.tickets.append(ticket)
                    print(client.show_attr())


            print("Su compra ha sido procesada exitosamente!")

        else:
            print("Su compra ha sido cancelada!")
            self.menu

    
    def vampiro(self, id):

        '''
        determina si un numero es vampiro o no. Utilizado para el descuento del ticket

        return: bool
        '''

        try:
            if len(id) == 7:
                id = (f'0{id}')
                
            p = permutations(id, len(id))
            pl = list(p)
            for num in pl:
                c = "".join(num)
                x, y = c[:int(len(c)/2)], c[int(len(c)/2):]
                if x[-1] == 0 and y[-1] == 0:
                    continue
                if int(x)*int(y == int(id)):
                    return False

            return True
        except:
            return False

    # asistencia al partido
    def asistencia(self):

        '''
        Utilizado para ingresar al estadio y agrega un ticket a la lista de asistencias que tiene cada partido
        '''

        ticket_id = input("Ingrese el ticket ID: ")
        for ticket in self.tickets:
            if int(ticket_id) == int(ticket.ticket_id):
                if not ticket_id in ticket.match.asistencia:
                    print("Asistencia validada")
                    ticket.match.asistencia.append(ticket_id)
                    break
                else:
                    print("Error. Este ticket ya fue utilizado para entrar al partido.")
            else:
                print("Error. Ticket ID invalido")

    # restaurante
    def manage_rest(self):

        '''
        Da la opcion de buscar o comprar productos en los restaurantes
        '''

        print(f'''
        
        1. Buscar productos
        2. Comprar productos
        
        ''')

        op_rest = input("Ingrese una opcion valida: ")
        while not op_rest.isnumeric() or int(op_rest) < 1 or int(op_rest) > 2:
            op_rest = input("Error. Ingrese una opcion valida: ")

        if int(op_rest) == 1:
            self.search_products()

        elif int(op_rest) == 2:
            self.buy_products()

    def search_products(self):

        '''
        Buscador de productos para cada uno de los restaurantes en los diferentes estadios
        '''
        
        op_product = input("Ingrese el producto que desea buscar: ").capitalize()
        while op_product.isnumeric():
            op_product = input("Ingrese el producto que desea buscar: ").capitalize()

        found = False
        for stadium in self.stadiums:
            for restaurant in stadium.restaurants:
                for product in restaurant.products:
                    if product.name == op_product:
                        found = True
                        print(f'''
                        
    {stadium.name}:
        {restaurant.name}

        {product.show_attr()}
        ''')
        
        if not found:
            print()
            print(f"El producto {op_product} no se encuentra disponible")

    def buy_products(self):

        '''
        Comprar productos luego de validar que el usuario este en el estadio y posea un ticket vip
        '''

        # Validar ticket VIP

        dni_cliente = input("Ingrese su cedula: ")

        compra = False
        for client in self.clients:
            if int(client.dni) == int(dni_cliente):
                current_client = client
                for ticket in client.tickets:
                    print(ticket.show_attr())
                ticket_id = input("Ingrese el ticket ID del partido en que se encuentra: ")
                if isinstance(ticket, Vip):
                    # if ticket_id in ticket.match.asistencia:
                        compra = True
                    # else:
                    #     print("Aun no ha confirmado su asitencia al estadio!")
                    #     break
                else:
                    print("El ticket seleccionado no es VIP y por lo tanto no tiene acceso a los restaurantes!")
                    break

        if compra:
            for ticket in self.tickets:
                if ticket.ticket_id == int(ticket_id):
                    current_ticket = ticket
                    for restaurant in ticket.match.location.restaurants:
                        for i, products in enumerate(restaurant.products):
                            print(f"{i+1}. {products.show_attr()}")
                            current_restaurant = restaurant
                            current_products = restaurant.products

            op_compra = input("Numero del producto: ")
            while not op_compra.isnumeric() or int(op_compra) > len(current_products) or int(op_compra) < 1:
                op_compra = input("Error. Numero del producto: ")
            
            compra = current_products[int(op_compra)-1]
            for product in current_products:
                if product == compra:
                    if product.tipo == "beverages":
                            if product.alcoholica == True:
                                if int(current_client.age) < 18:
                                    print("Usted no tiene la edad para comprar bebidas alcoholicas.")
                                    break
                    descuento = 0
                    if self.numero_perf(int(current_client.dni)):
                        descuento = compra.price * 0.15
                    current_factura = Factura(compra, descuento)
                    print(current_factura.show_attr())

                    confirmation = input(f"Desea comprar {product.name}?\n1. Si\n2. No\n")
                    while not confirmation.isnumeric() or int(confirmation) < 1 or int(confirmation) > 2:
                        confirmation = input(f"Error. Desea comprar {product.name}?\n1. Si\n2. No\n")
                    
                    if int(confirmation) == 1:
                        current_ticket.compras.append(current_factura)
                        print("Su compra ha sido registrada!")
    
    def numero_perf(self, dni):

        '''
        Determina si un num es perfecto y es utilizado para el descuento en la compra de productos

        parametros: int
        return: bool
        '''

        divisores = []
        for n in range(1, dni):
            if dni % n == 0:
                divisores.append(n)

        if sum(divisores) == dni:
            return True
        else:
            return False              

    # estadisticas
    def estadisticas(self):

        '''
        Menu para estadisticas
        '''

        print('''
            
    1. Promedio gastos VIP
    2. Asistencias
    3. Boletos vendidos
    4. Productos vendidos
    5. Clientes
            
            ''')

        op_estadisticas = input("Ingrese una opcion valida: ")
        while not op_estadisticas.isnumeric or int(op_estadisticas) < 1 or int(op_estadisticas) > 5:
            op_estadisticas = input("Error. Ingrese una opcion valida: ")

        if int(op_estadisticas) == 1:
            self.gastos_vip()

        elif int(op_estadisticas) == 2:
            self.orden_asistencia()

        elif int(op_estadisticas) == 3:
            self.ticket_sales()

        elif int(op_estadisticas) == 4:
            print("Disculpe. Esta funcion no se encuenta disponible ")
            self.best_sellers()
        
        elif int(op_estadisticas) == 5:
            self.best_client()

    def gastos_vip(self):

        '''
        Muestra el gasto total de entradas vip y el promedio de gasto por cliente
        '''

        total_entradas_vip = 0
        total_rest = 0
        cant_tickets_vip = 0
        for ticket in self.tickets:
            if isinstance(ticket, Vip):
                    cant_tickets_vip += 1
                    total_entradas_vip += ticket.total
                    for compra in ticket.compras:
                        total_rest += compra.total
                    total_vip = total_entradas_vip + total_rest

        print(f'''
        
        --- Total ventas VIP ---
        
        Entradas: {total_entradas_vip}
        Restaurante: {total_rest}
        total: {total_vip}

        Promedio: {total_vip/cant_tickets_vip}
    
        ''')

    def orden_asistencia(self):

        '''
        Ordena la lista de self.matches segun la cantidad de asistencias confirmadas por partido
        '''

        # Asistencia partidos
        self.matches.sort(key = lambda match: len(match.asistencia), reverse=True)
        for i, match in enumerate(self.matches):
            boletos_vendidos = len(match.seats_vip) + len(match.seats_general)
            asistencias = len(match.asistencia)
            print(f'''{i+1}. {match.show_attr()}
            Boletos vendidos: {boletos_vendidos}
            Asistencias: {asistencias}
            Relacion: {asistencias}//{boletos_vendidos}
            ''')

            print(f"--- Mayor asistencia ---")
            print(self.matches[0].show_attr())

    def ticket_sales(self):

        '''
        Muestra el partido con mayor cantidad de entradas vendidas
        '''

        mayor_cant = 0

        for match in self.matches:
            vip = len(match.seats_vip)
            general = len(match.seats_general)
            total = vip + general
            if total > mayor_cant:
                partido_mayor = match

        print(f"El partido con mas tickets vendidos fue: {partido_mayor.show_attr()}")

    def best_sellers(self):
        pass
        # cant_mayor = 0
        # for stadium in self.stadium:
        #     for restaurant in stadium.restaurants:
        #         for product in restaurant.products:
        #             for client in self.clients:
        #                 for ticket in client.tickets:
        #                     if ticket.isinstance(ticket, Vip):
        #                         for compra in ticket.compras:
        #                             if compra.name == product.name:
        #                                 cant_mayor += 1
                        


    def best_client(self):

        '''
        Ordena la lista de self.clients y muestra los 3 clientes que compraron la mayor cantidad de entradas 
        '''
        
        self.clients.sort(key = lambda client: len(client.tickets), reverse=True)

        for i, client in enumerate(self.clients):
            boletos_comprados = len(client.tickets)
            if i < 3:
                print()
                print(f"{i+1}. {client.show_attr()}")