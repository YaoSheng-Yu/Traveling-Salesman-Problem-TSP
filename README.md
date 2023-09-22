# Traveling Salesman Problem (TSP) & Kruskal's Algorithm

## Introduction:

The Traveling Salesman Problem (TSP) is a classic optimization challenge in which a salesman strives to visit each city once and return to the starting city, all while minimizing the total distance traveled. This repository introduces a heuristic approach to the TSP, utilizing Kruskal's algorithm to generate a Minimum Spanning Tree (MST) and subsequently conducting a Depth-First Search (DFS) traversal to construct a tour.

## Features:

- **Kruskal's Algorithm Implementation:** An adept rendition of Kruskal's algorithm to determine the MST of a specified weighted graph.
- **TSP via DFS:** By leveraging the MST derived from Kruskal's algorithm, a DFS traversal provides a tour approximating the solution to the TSP.
- **Graph Test Cases:** A utility script that crafts graphs tailored for both best-case and worst-case scenario evaluations.

## How It Works:

1. **Minimum Spanning Tree:** Employing Kruskal's algorithm, the MST of the input graph is obtained. This MST ensures every node is interconnected with the least possible cumulative weight.
2. **DFS Traversal:** Harnessing the MST, a DFS traversal delineates a tour encompassing all cities once, eventually circling back to the commencement city.

## Interpretation of Results:

The output manifests:

- **MST Cost:** The aggregate weight of the MST extrapolated from the input graph.
- **TSP Tour Cost:** The cumulative travel distance of the tour generated from the MST.
- **Ratio:** A comparison of the TSP tour cost to the MST cost, shedding light on the efficacy of the deduced tour.

## Usage:

> **Note:** All input data and subsequent results are consigned to the `data` directory.

1. **Special Scenario Graphs: `generate_worst_best.py`**
   - Craft graphs that depict the most optimal or least favorable ratio scenarios for the TSP.
   - **Example Use:** To generate a worst-case scenario graph encompassing 500 vertices: `python3 generate_worst_best.py 2 500 -o ./data/graph_worst.txt`

2. **Random Graph Generation: `generate_testcases.py`**
   - Generate a standard graph with stochastic weight edges, ensuring it is undirected, interconnected, and respects the triangle inequality.
   - **Example Use:** To create a graph containing 100 nodes: `python3 generate_testcases.py ./data/graph.txt 100`
   - 
3. **Minimum Spanning Tree: `mst.py`**
   - Compute the MST of a given graph and ascertain the corresponding TSP tour cost.
   - **Output:** Two lines - the first conveys the MST cost, while the second denotes the TSP tour cost.
   - **Example Use:** To process a graph and retrieve the MST and TSP costs: `python3 mst.py -i ./data/graph.txt -o ./data/output.txt`
