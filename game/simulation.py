def compute_profit(station, demand, overload_penalty=2):

    overload = max(0, demand - station.capacity)
    penalty = overload_penalty * overload

    return (station.price - station.marginal_cost) * demand - penalty
