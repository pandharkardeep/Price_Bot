class Station:
    def __init__(self, station_id, marginal_cost=5, capacity=50):
        self.station_id = station_id
        self.marginal_cost = marginal_cost
        self.capacity = capacity
        self.price = 10
