import numpy as np
from game.demand import congestion_demand
from game.simulation import compute_profit

def best_response(station_index, stations, total_demand):

    price_grid = np.linspace(5, 20, 50)
    best_price = stations[station_index].price
    best_profit = -1e9

    for p in price_grid:

        stations[station_index].price = p

        allocation = congestion_demand(stations, total_demand)

        demand = allocation[stations[station_index].station_id]
        profit = compute_profit(stations[station_index], demand)

        if profit > best_profit:
            best_profit = profit
            best_price = p

    stations[station_index].price = best_price
    return best_price

def find_nash(stations, total_demand, iterations=20):

    history = []

    for _ in range(iterations):

        for i in range(len(stations)):
            best_response(i, stations, total_demand)

        history.append([s.price for s in stations])

    return history

