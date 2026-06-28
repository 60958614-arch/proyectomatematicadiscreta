import sys, matplotlib.pyplot as plt, networkx as nx
from matplotlib.patches import FancyArrowPatch

# === Definición del DFA ===
states = {"q0","q1","q2","q3","q4"}
alphabet = {"a","b"}
delta = {("q0","a"):"q1", 
        ("q1","a"):"q4", 
        ("q1","b"):"q4", 
        ("q2","a"):"q0", 
        ("q2","b"):"q1", 
        ("q3","b"):"q2", 
        ("q4","a"):"q4", 
        ("q4","b"):"q4"}

q0, F = "q0", {"q4"}

# === Simulación ===
def run(s):
    q, steps = q0, [q0]
    for i,ch in enumerate(s):
        if (q,ch) not in delta: raise ValueError(f"Sin transición desde {q} con '{ch}' en pos {i}")
        q = delta[(q,ch)]; steps.append(q)
    return steps, steps[-1] in F

# === Grafo y layout ===
G = nx.MultiDiGraph(); G.add_nodes_from(states)
for (q,a),p in delta.items(): G.add_edge(q,p,key=a,label=a)
pos = nx.spring_layout(G, seed=7)