r"""Graph theory functions using networkx."""

import networkx as nx
import numpy as np


def create_graph(edges: list, directed: bool = False) -> nx.Graph:
    r"""Create a graph from edge list.
    
    Args:
        edges: List of tuples (u, v) representing edges
        directed: If True, create directed graph
    
    Returns:
        NetworkX graph
    """
    if directed:
        G = nx.DiGraph()
    else:
        G = nx.Graph()
    G.add_edges_from(edges)
    return G


def create_weighted_graph(edges: list, directed: bool = False) -> nx.Graph:
    r"""Create a weighted graph from edge list.
    
    Args:
        edges: List of tuples (u, v, weight)
        directed: If True, create directed graph
    
    Returns:
        NetworkX weighted graph
    """
    if directed:
        G = nx.DiGraph()
    else:
        G = nx.Graph()
    for edge in edges:
        if len(edge) == 3:
            G.add_edge(edge[0], edge[1], weight=edge[2])
        else:
            G.add_edge(edge[0], edge[1])
    return G


def adjacency_matrix(G: nx.Graph) -> np.ndarray:
    r"""Compute adjacency matrix.
    
    A_{ij} = 1 if edge exists between i and j
    
    Args:
        G: NetworkX graph
    
    Returns:
        Adjacency matrix as numpy array
    """
    return nx.to_numpy_array(G)


def laplacian_matrix(G: nx.Graph) -> np.ndarray:
    r"""Compute graph Laplacian matrix.
    
    L = D - A where D is degree matrix, A is adjacency
    
    Args:
        G: NetworkX graph
    
    Returns:
        Laplacian matrix
    """
    return nx.laplacian_matrix(G).toarray()


def degree_sequence(G: nx.Graph) -> list:
    r"""Return degree sequence of graph.
    
    Args:
        G: NetworkX graph
    
    Returns:
        List of degrees for each node
    """
    return [d for n, d in G.degree()]


def degree_distribution(G: nx.Graph) -> dict:
    r"""Compute degree distribution.
    
    Returns:
        Dictionary mapping degree to count
    """
    degrees = degree_sequence(G)
    dist = {}
    for d in degrees:
        dist[d] = dist.get(d, 0) + 1
    return dist


def average_degree(G: nx.Graph) -> float:
    r"""Compute average degree.
    
    Args:
        G: NetworkX graph
    
    Returns:
        Average degree
    """
    return np.mean(degree_sequence(G))


def clustering_coefficient(G: nx.Graph) -> float:
    r"""Compute average clustering coefficient.
    
    Args:
        G: NetworkX graph
    
    Returns:
        Average clustering coefficient
    """
    return nx.average_clustering(G)


def clustering_coefficients(G: nx.Graph) -> dict:
    r"""Compute clustering coefficient for each node.
    
    Args:
        G: NetworkX graph
    
    Returns:
        Dictionary mapping node to clustering coefficient
    """
    return nx.clustering(G)


def shortest_path(G: nx.Graph, source, target) -> list:
    r"""Find shortest path between two nodes.
    
    Args:
        G: NetworkX graph
        source: Source node
        target: Target node
    
    Returns:
        List of nodes in shortest path
    """
    try:
        return nx.shortest_path(G, source, target)
    except nx.NetworkXNoPath:
        return []


def shortest_path_length(G: nx.Graph, source, target) -> float:
    r"""Find shortest path length.
    
    Args:
        G: NetworkX graph
        source: Source node
        target: Target node
    
    Returns:
        Shortest path length
    """
    try:
        return nx.shortest_path_length(G, source, target)
    except nx.NetworkXNoPath:
        return float("inf")


def dijkstra_shortest_path(G: nx.Graph, source, target) -> list:
    r"""Find shortest path using Dijkstra's algorithm.
    
    Args:
        G: Weighted NetworkX graph
        source: Source node
        target: Target node
    
    Returns:
        List of nodes in shortest path
    """
    try:
        return nx.dijkstra_path(G, source, target)
    except (nx.NetworkXNoPath, nx.NodeNotFound):
        return []


def dijkstra_path_length(G: nx.Graph, source, target) -> float:
    r"""Find shortest path length using Dijkstra.
    
    Args:
        G: Weighted NetworkX graph
        source: Source node
        target: Target node
    
    Returns:
        Shortest path length
    """
    try:
        return nx.dijkstra_path_length(G, source, target)
    except (nx.NetworkXNoPath, nx.NodeNotFound):
        return float("inf")


def bellman_ford_shortest_path(G: nx.Graph, source, target) -> list:
    r"""Find shortest path using Bellman-Ford algorithm.
    
    Handles negative edge weights.
    
    Args:
        G: Weighted NetworkX graph
        source: Source node
        target: Target node
    
    Returns:
        List of nodes in shortest path
    """
    try:
        return nx.bellman_ford_path(G, source, target)
    except (nx.NetworkXNoPath, nx.NodeNotFound):
        return []


def connected_components(G: nx.Graph) -> list:
    r"""Find connected components.
    
    Args:
        G: NetworkX graph
    
    Returns:
        List of sets, each set is a connected component
    """
    return list(nx.connected_components(G))


def number_of_connected_components(G: nx.Graph) -> int:
    r"""Count connected components.
    
    Args:
        G: NetworkX graph
    
    Returns:
        Number of connected components
    """
    return nx.number_connected_components(G)


def is_connected(G: nx.Graph) -> bool:
    r"""Check if graph is connected.
    
    Args:
        G: NetworkX graph
    
    Returns:
        True if connected
    """
    return nx.is_connected(G)


def is_biconnected(G: nx.Graph) -> bool:
    r"""Check if graph is biconnected (articulation points).
    
    Args:
        G: NetworkX graph
    
    Returns:
        True if biconnected
    """
    return nx.is_biconnected(G)


def articulation_points(G: nx.Graph) -> list:
    r"""Find articulation points (cut vertices).
    
    Args:
        G: NetworkX graph
    
    Returns:
        List of articulation points
    """
    return list(nx.articulation_points(G))


def is_bipartite(G: nx.Graph) -> bool:
    r"""Check if graph is bipartite.
    
    Args:
        G: NetworkX graph
    
    Returns:
        True if bipartite
    """
    return nx.is_bipartite(G)


def color_bipartite(G: nx.Graph) -> dict:
    r"""Color bipartite graph.
    
    Args:
        G: NetworkX graph
    
    Returns:
        Dictionary mapping nodes to color (0 or 1)
    """
    try:
        return nx.bipartite_color(G)
    except nx.NetworkXError:
        return {}


def graph_center(G: nx.Graph) -> list:
    r"""Find center of graph (nodes with minimum eccentricity).
    
    Args:
        G: NetworkX graph
    
    Returns:
        List of center nodes
    """
    return list(nx.center(G))


def eccentricity(G: nx.Graph, node) -> int:
    r"""Compute eccentricity of a node.
    
    Args:
        G: NetworkX graph
        node: Node to compute eccentricity for
    
    Returns:
        Eccentricity (max shortest path distance to any other node)
    """
    try:
        return nx.eccentricity(G, node)
    except nx.NetworkXError:
        return float("inf")


def radius(G: nx.Graph) -> int:
    r"""Compute graph radius.
    
    Minimum eccentricity over all nodes.
    
    Args:
        G: NetworkX graph
    
    Returns:
        Graph radius
    """
    return nx.radius(G)


def diameter(G: nx.Graph) -> int:
    r"""Compute graph diameter.
    
    Maximum eccentricity over all nodes.
    
    Args:
        G: NetworkX graph
    
    Returns:
        Graph diameter
    """
    return nx.diameter(G)


def pagerank(G: nx.Graph, alpha: float = 0.85) -> dict:
    r"""Compute PageRank scores.
    
    Args:
        G: NetworkX graph
        alpha: Damping parameter
    
    Returns:
        Dictionary mapping nodes to PageRank score
    """
    return nx.pagerank(G, alpha=alpha)


def hits_scores(G: nx.Graph, normalized: bool = True) -> tuple:
    r"""Compute HITS (Hubs and Authorities) scores.
    
    Args:
        G: NetworkX graph
        normalized: If True, normalize scores
    
    Returns:
        Tuple of (hubs, authorities) dictionaries
    """
    return nx.hits(G, normalized=normalized)


def betweenness_centrality(G: nx.Graph) -> dict:
    r"""Compute betweenness centrality.
    
    Args:
        G: NetworkX graph
    
    Returns:
        Dictionary mapping nodes to betweenness centrality
    """
    return nx.betweenness_centrality(G)


def degree_centrality(G: nx.Graph) -> dict:
    r"""Compute degree centrality.
    
    Args:
        G: NetworkX graph
    
    Returns:
        Dictionary mapping nodes to degree centrality
    """
    return nx.degree_centrality(G)


def closeness_centrality(G: nx.Graph) -> dict:
    r"""Compute closeness centrality.
    
    Args:
        G: NetworkX graph
    
    Returns:
        Dictionary mapping nodes to closeness centrality
    """
    return nx.closeness_centrality(G)


def eigenvector_centrality(G: nx.Graph, max_iter: int = 100) -> dict:
    r"""Compute eigenvector centrality.
    
    Args:
        G: NetworkX graph
        max_iter: Maximum iterations
    
    Returns:
        Dictionary mapping nodes to eigenvector centrality
    """
    try:
        return nx.eigenvector_centrality(G, max_iter=max_iter)
    except nx.PowerIterationFailedConvergence:
        return {}


def minimum_spanning_tree(G: nx.Graph) -> nx.Graph:
    r"""Compute minimum spanning tree.
    
    Args:
        G: Weighted NetworkX graph
    
    Returns:
        MST as NetworkX graph
    """
    return nx.minimum_spanning_tree(G)


def minimum_spanning_tree_edges(G: nx.Graph) -> list:
    r"""Get edges of minimum spanning tree.
    
    Args:
        G: Weighted NetworkX graph
    
    Returns:
        List of edges in MST
    """
    return list(nx.minimum_spanning_tree_edges(G))


def number_of_edges(G: nx.Graph) -> int:
    r"""Count number of edges.
    
    Args:
        G: NetworkX graph
    
    Returns:
        Number of edges
    """
    return G.number_of_edges()


def number_of_nodes(G: nx.Graph) -> int:
    r"""Count number of nodes.
    
    Args:
        G: NetworkX graph
    
    Returns:
        Number of nodes
    """
    return G.number_of_nodes()


def density(G: nx.Graph) -> float:
    r"""Compute graph density.
    
    Args:
        G: NetworkX graph
    
    Returns:
        Density (actual edges / possible edges)
    """
    return nx.density(G)


def is_eulerian(G: nx.Graph) -> bool:
    r"""Check if graph has Eulerian circuit/path.
    
    Args:
        G: NetworkX graph
    
    Returns:
        True if Eulerian
    """
    return nx.is_eulerian(G)


def eulerian_path(G: nx.Graph) -> list:
    r"""Find Eulerian path/circuit.
    
    Args:
        G: NetworkX graph
    
    Returns:
        List of nodes in Eulerian path
    """
    try:
        return list(nx.eulerian_path(G))
    except nx.NetworkXError:
        return []


def is_hamiltonian(G: nx.Graph) -> bool:
    r"""Check if graph has Hamiltonian cycle.
    
    Args:
        G: NetworkX graph
    
    Returns:
        True if Hamiltonian cycle exists (not guaranteed)
    """
    return nx.is_hamiltonian(G)


def traveling_salesman(G: nx.Graph) -> list:
    r"""Approximate traveling salesman problem.
    
    Args:
        G: Weighted NetworkX graph
    
    Returns:
        Approximate TSP tour as list of nodes
    """
    try:
        return list(nx.approximation.traveling_salesman_problem(G))
    except nx.NetworkXError:
        return []


def max_clique(G: nx.Graph) -> list:
    r"""Find maximum clique.
    
    Args:
        G: NetworkX graph
    
    Returns:
        List of nodes in maximum clique
    """
    try:
        return list(nx.approximation.max_clique(G))
    except nx.NetworkXError:
        return []


def graph_clique_number(G: nx.Graph) -> int:
    r"""Compute clique number (size of largest clique).
    
    Args:
        G: NetworkX graph
    
    Returns:
        Clique number
    """
    try:
        return nx.graph_clique_number(G)
    except nx.NetworkXError:
        return 0


def independent_set(G: nx.Graph) -> list:
    r"""Find maximum independent set.
    
    Args:
        G: NetworkX graph
    
    Returns:
        List of nodes in maximum independent set
    """
    try:
        return list(nx.maximum_independent_set(G))
    except nx.NetworkXError:
        return []


def vertex_cover(G: nx.Graph) -> list:
    r"""Find minimum vertex cover.
    
    Args:
        G: NetworkX graph
    
    Returns:
        List of nodes in minimum vertex cover
    """
    try:
        return list(nx.minimum_vertex_cover(G))
    except nx.NetworkXError:
        return []