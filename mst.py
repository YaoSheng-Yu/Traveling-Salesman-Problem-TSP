# -*- coding: utf-8 -*-

import sys, getopt
from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        # Initialize parents to be themselves and rank to 0
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        # Find the representative (root) of the set
        # Uses path compression for efficiency
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Merge two sets using rank to ensure small depth tree
        xr = self.find(x)
        yr = self.find(y)
        if xr != yr:
            if self.rank[xr] < self.rank[yr]:
                self.parent[xr] = yr
            elif self.rank[xr] > self.rank[yr]:
                self.parent[yr] = xr
            else:
                self.parent[yr] = xr
                self.rank[xr] += 1

def kruskal(edges, n):
    """Implementing Kruskal's algorithm to find Minimum Spanning Tree (MST)"""
    uf = UnionFind(n)
    mst = []
    # Sort edges by weight
    for w, u, v in sorted(edges):
        # If nodes u and v are not in the same set, merge them and add edge to MST
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, w))
    return mst

def dfs(graph, start):
    """Depth First Search to traverse the MST"""
    visited = [False for _ in range(len(graph))]
    tour = []
    stack = [start]
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            tour.append(node)
            for neighbor in reversed(graph[node]):  # reversed to make the smallest node appear at the top of the stack
                if not visited[neighbor]:
                    stack.append(neighbor)
    return tour

def main(argv):
    # Argument parsing
    inputfile = ''
    outputfile = ''
    opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    for opt, arg in opts:
        if opt == '-h':
            print ('mst.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    # Reading input file
    with open(inputfile, 'r', encoding="utf-8") as f:
        n = int(f.readline().strip())  # number of nodes
        m = int(f.readline().strip())  # number of edges
        edges = []
        for _ in range(m):
            u, v, w = map(int, f.readline().split())
            edges.append((w, u, v))  # store as (weight, node1, node2)

    # Compute MST
    mst_edges = kruskal(edges, n)
    mst_cost = sum(w for _, _, w in mst_edges)

    # Convert MST edges to adjacency list representation
    mst_graph = defaultdict(list)
    for u, v, _ in mst_edges:
        mst_graph[u].append(v)
        mst_graph[v].append(u)

    # Compute DFS tour over MST
    tour = dfs(mst_graph, 0)  # starting node is 0
    tour.append(tour[0])  # return to start

    # Compute cost of the DFS tour
    tour_edges = [(tour[i-1], tour[i]) for i in range(1, len(tour))]
    edge_dict = {(min(u, v), max(u, v)): w for w, u, v in edges}
    tour_cost = sum(edge_dict[(min(u, v), max(u, v))] for u, v in tour_edges)

    # Write results to output file
    with open(outputfile, "w") as f:
        f.write(f"MST cost: {mst_cost}\n")
        f.write(f"TSP tour cost: {tour_cost}\n")
    
    # Display results to the console
    print(f"MST cost: {mst_cost}")
    print(f"TSP tour cost: {tour_cost}")
    print(f"ratio: {tour_cost/mst_cost}")

if __name__ == "__main__":
    main(sys.argv[1:])
