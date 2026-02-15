import numpy as np
from game.config import alpha, gamma
# class demand:
def congestion_demand(stations, total_demand, alpha=alpha, gamma=gamma, iterations=20):

    n = len(stations)
    demand = np.ones(n) * (total_demand / n)

    for _ in range(iterations):

        utilities = []

        for i, s in enumerate(stations):
            waiting = demand[i] / s.capacity
            utility = -alpha * s.price - gamma * waiting
            utilities.append(utility)

        exp_u = np.exp(utilities - np.max(utilities))
        shares = exp_u / np.sum(exp_u)

        demand = total_demand * shares

    allocation = {}
    for s, d in zip(stations, demand):
        allocation[s.station_id] = d

    return allocation
