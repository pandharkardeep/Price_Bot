import matplotlib.pyplot as plt
from game.station import Station
from game.nash_solver import find_nash
from game.station import generate_users

stations = [
    Station(1, marginal_cost=5),
    Station(2, marginal_cost=5),
    Station(3, marginal_cost=4),
    Station(4, marginal_cost=9),
    Station(5, marginal_cost=2),
    Station(6, marginal_cost=3)
]
users = generate_users(92)
stations[0].price = 15
stations[1].price = 18
stations[2].price = 12
stations[3].price = 15
stations[4].price = 18
stations[5].price = 12

total_demand = 100   # > total capacity (60)


price_history = find_nash(stations, users)

for i in range(len(stations)):
    plt.plot([ph[i] for ph in price_history], label=f"Station {i+1}")

plt.title("Price Convergence")
plt.xlabel("Iteration")
plt.ylabel("Price")
plt.legend()
plt.show()
