import numpy as np
from game.demand import spatial_congestion_demand
from game.simulation import compute_profit

def best_response(i, stations, users):

    price_grid = np.linspace(5, 25, 40)
    best_price = stations[i].price
    best_profit = -1e9

    for p in price_grid:
        stations[i].price = p

        allocation = spatial_congestion_demand(stations, users)

        demand = allocation[stations[i].station_id]
        profit = (p - stations[i].marginal_cost) * demand

        if profit > best_profit:
            best_profit = profit
            best_price = p

    stations[i].price = best_price
    return best_price


def find_nash(stations, users, iterations=20):

    history = []

    for _ in range(iterations):
        for i in range(len(stations)):
            best_response(i, stations, users)

        history.append([s.price for s in stations])

    return history


