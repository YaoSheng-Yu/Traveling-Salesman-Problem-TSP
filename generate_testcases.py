import random
import argparse

def generate_graph(n):
    weights = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            weights[i][j] = weights[j][i] = random.randint(1, n*10)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if weights[i][j] > weights[i][k] + weights[k][j]:
                    weights[i][j] = weights[j][i] = weights[i][k] + weights[k][j]
    return weights


def main(filename, num_nodes):
    weights = generate_graph(num_nodes)
    edges = [(i, j, weights[i][j]) for i in range(num_nodes) for j in range(i+1, num_nodes)]
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"{num_nodes}\n")
        f.write(f"{len(edges)}\n")
        for u, v, w in edges:
            f.write(f"{u} {v} {w}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate a graph.')
    parser.add_argument('filename', type=str, help='The name of the file to write the graph to')
    parser.add_argument('num_nodes', type=int, help='The number of nodes in the graph')
    args = parser.parse_args()

    main(args.filename, args.num_nodes)
