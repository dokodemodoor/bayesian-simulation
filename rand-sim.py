# sim.py 

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pylab
from agent import Agent

NPLAYERS = 24 
K = 4
NTRIALS = 15
COST = 10 
BENEFIT = 160 
NREP = 100

def main():
    network = make_ring_lattice(NPLAYERS, K) 
    rnge = 2*K * (COST+BENEFIT) 
    overall_strats = [[] for i in range(NTRIALS)] 
    coop_prp = []

    for i in range(NREP): 
          # Initial cooperative strategies at Trial 0, with p(coop) = 0.6
          # 0 = defect, 1 = cooperate 
        cur_strats = np.random.choice(2, NPLAYERS, replace=True, p=[0.4, 0.6]) 
        record(i, 0, overall_strats, coop_prp, list(cur_strats))
        
        for player in network: 
            player.set_strat(cur_strats[player.get_id()])

        for k in range(1, NTRIALS): 
            calc_payoff(network)  
            update(network, rnge)

            for player in network:
                cur_strats[player.get_id()] = player.get_strat() 

            record(i, k, overall_strats, coop_prp, list(cur_strats))

    plot_coop_prp(coop_prp)

def neighbors (nodes, k):
    n = len(nodes)
    for i, player in enumerate(nodes):
        for j in range(i+1, i+k+1):
            neigh = nodes[j % n]
            yield player, neigh 

def make_ring_lattice (n, k):
    G = nx.Graph()
    nodes = [Agent(i) for i in range(n)]
    G.add_nodes_from(nodes)
    G.add_edges_from(neighbors(nodes, k))
    return G

def record (i, n, overall_strats, coop_prp, cur_strats):
    overall_strats[n].append(cur_strats)
    cur_coop = np.sum(cur_strats) / NPLAYERS 
    if i == 0:
        coop_prp.append(cur_coop)
    else:
        coop_prp[n] += cur_coop 

def calc_payoff (network):
    for player in network: 
          # Calculate payoffs
        coop_neigh = sum(1 for neighbor in network[player] 
                if neighbor.get_strat() == 1)
        cost = -COST * player.get_strat() * 2*K 
        benefit = coop_neigh * BENEFIT
        bank = cost + benefit 
        player.set_bank(bank) 

          # Calculate proportion of neighbors who cooperated
        passort = coop_neigh / (2*K) 
        player.set_assort(passort)

def update (network, rnge): 
    for player in network:
        coop = []
        defect = []

        for neighbor in network[player]:
            if neighbor.get_strat() == 1: 
                coop.append(neighbor.get_bank())
            else:
                defect.append(neighbor.get_bank())

        if player.get_strat() == 1:
            same = coop 
            diff = defect
            same.append(player.get_bank()) 
        else:
            same = defect
            diff = coop
            same.append(player.get_bank())
        
        if diff:  
            theta = (np.sum(diff) + COST * 2*K * len(diff)) / (rnge * len(diff)) 
        else: 
            theta = 0.05

        if same: 
            mu = (np.sum(same) + COST * 2*K * len(same)) / (rnge * len(same)) 
        else:
            mu = 0.05
        
        if player.get_strat() == 1 and player.get_assort() > 0.7:
            switchprob = 0.05
        else:
            switchprob = theta / (theta + mu) 

        player.set_sp(switchprob)
       
    for player in network:
        decision = np.random.choice(2, p=[1 - player.get_sp(), player.get_sp()]) 
        if (decision):
            player.set_strat(1 - player.get_strat()) 

def plot_coop_prp(coop_prp):
    plt.figure(facecolor="white")
    plt.scatter(list(range(0, NTRIALS)), 
            [x / NREP for x in coop_prp], color="#703fbf")
    plt.ylim(0,1)
    plt.ylabel("Mean Cooperation Proportion")
    plt.xlabel("Round Number")
    plt.title("Simulated Proportion of Cooperation over Game\n bc = %1.2f,"
        "k = %d, Players = %d, Runs = %d" % (BENEFIT/COST, K, NPLAYERS, NREP))
    plt.grid(True)
    pylab.show()

if __name__ == "__main__":
    main()
