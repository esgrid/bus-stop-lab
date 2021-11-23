class Bus:
    def __init__(self, route_number, destination, price, capacity):
        self.route_number = route_number
        self.destination = destination
        self.price = price
        self.capacity = capacity
        self.passengers = []
    
    def drive(self):
        return "Brum brum"
    
    def how_many_passengers(self):
        return len(self.passengers)

    def pick_up_passenger(self, passenger):
        self.passengers.append(passenger)

    def drop_passenger(self, passenger):
        self.passengers.remove(passenger)
    
    def empty_bus(self):
        self.passengers = []

    def pick_up_from_stop(self, bus_stop):
        self.passengers = [*self.passengers, *bus_stop.queue]
        bus_stop.queue = 0