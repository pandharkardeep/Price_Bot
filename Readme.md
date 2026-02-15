# ⚡ Multi-Agent EV Charging Pricing Game

### Spatial Bertrand Competition with Congestion Effects

## 📌 Overview

This project simulates a **multi-agent pricing game** among EV charging stations operating in a spatial market with congestion effects.

Each charging station:

* Sets its price strategically
* Competes with nearby stations
* Faces demand influenced by price, distance, and waiting time
* Maximizes profit under capacity constraints

The system models:

* **Bertrand price competition**
* **Hotelling spatial differentiation**
* **Congestion externalities**
* **Iterative best-response Nash equilibrium**

---

# 🧠 Economic Model

---

## 🎯 Players

Let:

```markdown
**S = {1, 2, ..., N}**
```

be the set of charging stations.

Each station ( i ) chooses:

```markdown
p_i \in [p_{min}, p_{max}]
```

Each station has:

* Marginal cost: ( c_i )
* Capacity: ( C_i )
* Location: ( s_i \in \mathbb{R}^2 )

---

## 🚗 Users

Users are distributed spatially:

```markdown
u \in \mathbb{R}^2
```

Each user chooses a station probabilistically based on utility.

---

## 📊 Utility Function

User ( u )'s utility for station ( i ):

```markdown
U_{u,i} = -\alpha p_i - \beta d(u, s_i) - \gamma w_i
```

Where:

* ( p_i ) = station price
* ( d(u, s_i) ) = Euclidean distance
* ( w_i ) = waiting time
* ( \alpha ) = price sensitivity
* ( \beta ) = distance sensitivity
* ( \gamma ) = congestion sensitivity

---

## ⏳ Waiting Time

Waiting is modeled as:

```markdown
w_i = \frac{D_i}{C_i}
```

Where:

* ( D_i ) = total demand at station ( i )
* ( C_i ) = capacity

This introduces **congestion externality**.

---

## 📈 Demand Allocation (Softmax Choice Model)

Users choose probabilistically:

```markdown
P_{u,i} =
\frac{e^{U_{u,i}}}
{\sum_{j=1}^{N} e^{U_{u,j}}}
```

Total demand:

```markdown
D_i = \sum_{u} P_{u,i}
```

This ensures smooth, differentiable demand.

---

## 💰 Profit Function

Station profit:

```markdown
\Pi_i = (p_i - c_i) D_i
```

Optional overload penalty:

```markdown
\Pi_i = (p_i - c_i) D_i - \lambda \max(0, D_i - C_i)
```

---

# 🎮 Game Type

This is a:

* Non-cooperative game
* Repeated best-response dynamic
* Spatial congestion oligopoly

We compute **Nash equilibrium numerically** via iterative best-response.

---

# 🔁 Nash Equilibrium Computation

For each station:

```markdown
p_i^* = \arg\max_{p_i} \Pi_i(p_i, p_{-i})
```

Algorithm:

1. Initialize prices
2. For each station:

   * Fix competitors' prices
   * Search over price grid
   * Select profit-maximizing price
3. Repeat until convergence

Convergence implies:

```markdown
\forall i, \quad p_i^* = BR_i(p_{-i}^*)
```

---

# 🏙️ Spatial Market Structure

This model combines:

| Component                | Economic Theory  |
| ------------------------ | ---------------- |
| Price competition        | Bertrand         |
| Location differentiation | Hotelling        |
| Waiting time             | Congestion game  |
| Capacity constraint      | Scarcity pricing |

---

# 📊 Expected Behavior

Depending on parameters:

### 🔹 Low demand

```markdown
D \le \sum C_i
```
→ Prices collapse toward marginal cost.

### 🔹 High demand

```markdown
D > \sum C_i
```
→ Congestion creates scarcity rents
→ Prices rise above marginal cost.

### 🔹 High β (distance sensitivity)

→ Strong local pricing power.

### 🔹 High γ (waiting sensitivity)

→ Higher equilibrium prices.

---

# 🧪 Key Parameters

| Parameter | Effect                  |
| --------- | ----------------------- |
| α         | Price sensitivity       |
| β         | Spatial differentiation |
| γ         | Congestion strength     |
| C_i       | Station capacity        |
| D         | Total demand            |

---

# 📂 Project Structure

```
ev_pricing_game/
│
├── station.py
├── demand.py
├── nash_solver.py
├── simulation.py
├── main.py
└── README.md
```

---

# 📈 Example Output

The model produces:

* Price convergence plots
* Demand allocation per station
* Profit evolution
* Spatial distribution of stations

Typical results:

* No collapse to marginal cost under congestion
* Price differentiation by geography
* Stable Nash equilibrium after iterations

---


# 📚 Research Context

This model relates to:

* Bertrand Oligopoly
* Hotelling Spatial Competition
* Congestion Games
* Electricity Market Design
* Smart Grid Pricing

---

# 🧩 Why This Matters

EV charging markets are:

* Spatially constrained
* Capacity limited
* Price competitive
* Congestion sensitive

This simulation provides a computational framework for:

* Studying pricing power
* Evaluating market efficiency
* Testing regulatory scenarios
* Designing optimal infrastructure

---

# ⚡ Future Upgrade: Multi-Agent RL

Replace best-response with:

[
\pi_i : \text{State} \rightarrow p_i
]

Where state includes:

* Competitor prices
* Local demand
* Congestion
* Grid load

Then solve using:

* Q-learning
* DQN
* PPO


