import numpy as np
from game.config import alpha, beta, gamma
def spatial_congestion_demand(stations, users, alpha=1, beta=1, gamma=5):

    n_stations = len(stations)
    demands = np.zeros(n_stations)

    # Initial waiting guess
    waiting = np.zeros(n_stations)

    for _ in range(10):  # iterate to stabilize congestion
        demands = np.zeros(n_stations)

        for user in users:
            utilities = []

            for i, s in enumerate(stations):
                distance = np.linalg.norm(user - s.location)
                utility = -alpha * s.price - beta * distance - gamma * waiting[i]
                utilities.append(utility)

            exp_u = np.exp(utilities - np.max(utilities))
            probs = exp_u / np.sum(exp_u)

            demands += probs

        waiting = demands / np.array([s.capacity for s in stations])

    allocation = {}
    for s, d in zip(stations, demands):
        allocation[s.station_id] = d

    return allocation
