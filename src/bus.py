class Bus:
    def __init__(self, route_number, destination, price, capacity):
        self.route_number = route_number
        self.destination = destination
        self.price = price
        self.capacity = capacity
        self.passengers = []
        self.fare_cash = 0
    
    def drive(self):
        return "Brum brum"
    
    def how_many_passengers(self):
        return len(self.passengers)

    def remaining_capacity(self):
        return self.capacity - self.how_many_passengers()

    def pick_up_passenger(self, passenger):
        self.passengers.append(passenger)

    def drop_passenger(self, passenger):
        self.passengers.remove(passenger)
    
    def empty_bus(self):
        self.capacity += self.how_many_passengers()
        self.passengers = []

    def pay_fare(self, passenger):
        self.fare_cash += self.price
        passenger.pay_cash(self.price)

    def pick_up_from_stop(self, bus_stop):
        to_be_removed_passengers = []
        for passenger in bus_stop.queue:
            if self.remaining_capacity() > 0 and passenger.destination == self.destination and passenger.cash >= self.price:
                self.pick_up_passenger(passenger)
                to_be_removed_passengers.append(passenger)
                self.pay_fare(passenger)
        bus_stop.queue = [p for p in bus_stop.queue if p not in to_be_removed_passengers]

            # self.passengers = [*self.passengers, *bus_stop.queue]
            # bus_stop.queue = 0
        