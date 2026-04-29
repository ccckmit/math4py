r"""Graph theory tests using networkx."""

import numpy as np
import pytest
import networkx as nx
from math4py.graph.function import (
    create_graph,
    create_weighted_graph,
    adjacency_matrix,
    laplacian_matrix,
    degree_sequence,
    degree_distribution,
    average_degree,
    clustering_coefficient,
    connected_components,
    number_of_connected_components,
    is_connected,
    is_bipartite,
    shortest_path,
    shortest_path_length,
    dijkstra_shortest_path,
    dijkstra_path_length,
    pagerank,
    betweenness_centrality,
    degree_centrality,
    closeness_centrality,
    minimum_spanning_tree,
    number_of_edges,
    number_of_nodes,
    density,
    radius,
    diameter,
    articulation_points,
    is_biconnected,
)


class TestGraphCreation:
    """Graph creation tests."""

    def test_create_simple_graph(self):
        """Create simple undirected graph."""
        edges = [(0, 1), (1, 2), (2, 3)]
        G = create_graph(edges)
        assert G.number_of_nodes() == 4
        assert G.number_of_edges() == 3

    def test_create_directed_graph(self):
        """Create directed graph."""
        edges = [(0, 1), (1, 2), (2, 0)]
        G = create_graph(edges, directed=True)
        assert G.number_of_nodes() == 3
        assert G.number_of_edges() == 3

    def test_create_weighted_graph(self):
        """Create weighted graph."""
        edges = [(0, 1, 2.0), (1, 2, 3.0)]
        G = create_weighted_graph(edges)
        assert G[0][1]["weight"] == 2.0
        assert G[1][2]["weight"] == 3.0


class TestGraphMatrices:
    """Matrix operation tests."""

    def test_adjacency_matrix(self):
        """Adjacency matrix for simple graph."""
        edges = [(0, 1), (1, 2)]
        G = create_graph(edges)
        A = adjacency_matrix(G)
        assert A.shape == (3, 3)
        assert A[0, 1] == 1
        assert A[1, 2] == 1

    def test_laplacian_matrix(self):
        """Laplacian matrix: L = D - A."""
        edges = [(0, 1), (1, 2)]
        G = create_graph(edges)
        L = laplacian_matrix(G)
        assert L.shape == (3, 3)


class TestDegreeProperties:
    """Degree-related tests."""

    def test_degree_sequence(self):
        """Degree sequence."""
        edges = [(0, 1), (1, 2), (2, 3)]
        G = create_graph(edges)
        degs = degree_sequence(G)
        assert degs == [1, 2, 2, 1]

    def test_degree_distribution(self):
        """Degree distribution."""
        edges = [(0, 1), (1, 2), (2, 0)]
        G = create_graph(edges)
        dist = degree_distribution(G)
        assert dist[2] == 3

    def test_average_degree(self):
        """Average degree = 2E/V."""
        edges = [(0, 1), (1, 2), (2, 3)]
        G = create_graph(edges)
        avg = average_degree(G)
        assert abs(avg - 1.5) < 1e-10


class TestConnectivity:
    """Connectivity tests."""

    def test_connected_components(self):
        """Find connected components."""
        edges = [(0, 1), (2, 3)]
        G = create_graph(edges)
        comps = connected_components(G)
        assert len(comps) == 2

    def test_is_connected(self):
        """Check if connected."""
        edges = [(0, 1), (1, 2)]
        G = create_graph(edges)
        assert is_connected(G)

    def test_is_not_connected(self):
        """Check if not connected."""
        edges = [(0, 1), (2, 3)]
        G = create_graph(edges)
        assert not is_connected(G)

    def test_articulation_points(self):
        """Find cut vertices."""
        edges = [(0, 1), (1, 2), (1, 3)]
        G = create_graph(edges)
        aps = articulation_points(G)
        assert 1 in aps

    def test_is_biconnected(self):
        """Biconnected check."""
        triangle = [(0, 1), (1, 2), (2, 0)]
        G = create_graph(triangle)
        assert is_biconnected(G)


class TestShortestPath:
    """Shortest path tests."""

    def test_shortest_path(self):
        """Basic shortest path."""
        edges = [(0, 1), (1, 2), (0, 2)]
        G = create_graph(edges)
        path = shortest_path(G, 0, 2)
        assert path == [0, 2] or path == [0, 1, 2]

    def test_shortest_path_length(self):
        """Path length."""
        edges = [(0, 1), (1, 2)]
        G = create_graph(edges)
        length = shortest_path_length(G, 0, 2)
        assert length == 2

    def test_no_path_same_node(self):
        """Same node path."""
        edges = [(0, 1)]
        G = create_graph(edges)
        length = shortest_path_length(G, 0, 0)
        assert length == 0

    def test_dijkstra_weighted(self):
        """Dijkstra on weighted graph."""
        edges = [(0, 1, 1), (1, 2, 2), (0, 2, 10)]
        G = create_weighted_graph(edges)
        path = dijkstra_shortest_path(G, 0, 2)
        assert path == [0, 1, 2]

    def test_dijkstra_path_length(self):
        """Dijkstra path length."""
        edges = [(0, 1, 1), (1, 2, 2)]
        G = create_weighted_graph(edges)
        length = dijkstra_path_length(G, 0, 2)
        assert length == 3


class TestCentralityMeasures:
    """Centrality tests."""

    def test_degree_centrality(self):
        """Degree centrality."""
        edges = [(0, 1), (1, 2), (2, 3)]
        G = create_graph(edges)
        cent = degree_centrality(G)
        assert cent[1] > cent[0]

    def test_closeness_centrality(self):
        """Closeness centrality."""
        star = [(0, 1), (0, 2), (0, 3)]
        G = create_graph(star)
        cent = closeness_centrality(G)
        assert cent[0] > cent[1]

    def test_betweenness_centrality(self):
        """Betweenness centrality."""
        path = [(0, 1), (1, 2)]
        G = create_graph(path)
        cent = betweenness_centrality(G)
        assert cent[1] > 0


class TestEigenvectorProperties:
    """Graph eigenprojector properties."""

    def test_clustering_coefficient(self):
        """Clustering coefficient."""
        triangle = [(0, 1), (1, 2), (2, 0)]
        G = create_graph(triangle)
        cc = clustering_coefficient(G)
        assert cc == 1.0

    def test_pagerank(self):
        """PageRank scores."""
        edges = [(0, 1), (1, 2), (2, 0), (2, 3)]
        G = create_graph(edges)
        pr = pagerank(G)
        assert abs(sum(pr.values()) - 1.0) < 1e-10
        assert pr[0] > 0


class TestSpanningTree:
    """Spanning tree tests."""

    def test_minimum_spanning_tree(self):
        """MST."""
        edges = [(0, 1, 1), (1, 2, 2), (0, 2, 3)]
        G = create_weighted_graph(edges)
        mst = minimum_spanning_tree(G)
        assert mst.number_of_edges() == 2


class TestBipartite:
    """Bipartite graph tests."""

    def test_is_bipartite(self):
        """Check bipartite."""
        bipartite = [(0, 2), (0, 3), (1, 2), (1, 3)]
        G = create_graph(bipartite)
        assert is_bipartite(G)

    def test_not_bipartite(self):
        """Triangle is not bipartite."""
        triangle = [(0, 1), (1, 2), (2, 0)]
        G = create_graph(triangle)
        assert not is_bipartite(G)


class TestSpecialGraphs:
    """Special graph properties."""

    def test_radius(self):
        """Graph radius."""
        star = [(0, 1), (0, 2), (0, 3)]
        G = create_graph(star)
        r = radius(G)
        assert r == 1

    def test_diameter(self):
        """Graph diameter."""
        path = [(0, 1), (1, 2), (2, 3)]
        G = create_graph(path)
        d = diameter(G)
        assert d == 3

    def test_density(self):
        """Graph density."""
        complete = [(0, 1), (0, 2), (1, 2)]
        G = create_graph(complete)
        d = density(G)
        assert d == 1.0

    def test_number_of_nodes_edges(self):
        """Node and edge counts."""
        edges = [(0, 1), (1, 2)]
        G = create_graph(edges)
        assert number_of_nodes(G) == 3
        assert number_of_edges(G) == 2


class TestCompleteGraphProperties:
    """Complete graph properties."""

    def test_complete_graph(self):
        """K4 properties."""
        G = nx.complete_graph(4)
        G = create_graph(list(G.edges()))
        assert number_of_nodes(G) == 4
        assert number_of_edges(G) == 6
        assert density(G) == 1.0

    def test_cycle_graph(self):
        """C5 properties."""
        G = nx.cycle_graph(5)
        G = create_graph(list(G.edges()))
        assert number_of_nodes(G) == 5
        assert number_of_edges(G) == 5
        assert is_connected(G)

    def test_path_graph(self):
        """P4 properties."""
        G = nx.path_graph(4)
        G = create_graph(list(G.edges()))
        assert number_of_connected_components(G) == 1
        assert not is_biconnected(G)