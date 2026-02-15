import numpy as np

class Station:
    def __init__(self, station_id, marginal_cost=5, capacity=50):
        self.station_id = station_id
        self.marginal_cost = marginal_cost
        self.capacity = capacity
        self.price = 10
        self.location = np.random.rand(2) * 10  # 2D city

def generate_users(n_users=200):
    return np.random.rand(n_users, 2) * 10
