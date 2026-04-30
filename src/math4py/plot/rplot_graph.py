r"""Graph plotting functions using matplotlib and networkx."""

import os
from typing import Optional

import matplotlib.pyplot as plt
import networkx as nx

_OUT_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))),
    "out"
)

_PALETTE = ["#2196F3", "#F44336", "#4CAF50", "#FF9800", "#9C27B0",
           "#00BCD4", "#FF5722", "#607D8B"]


def plot_graph(
    G,
    filename: Optional[str] = None,
    pos: Optional[dict] = None,
    node_color: str = "#2196F3",
    edge_color: str = "#424242",
    node_size: int = 300,
    with_labels: bool = True,
    font_size: int = 10,
    width: float = 1.0,
    alpha: float = 0.8,
    title: Optional[str] = None,
):
    r"""Plot a graph.

    Args:
        G: NetworkX graph
        filename: Output file (None for display)
        pos: Node positions (None for spring layout)
        node_color: Node color
        edge_color: Edge color
        node_size: Node size
        with_labels: Show labels
        font_size: Label font size
        width: Edge width
        alpha: Transparency
        title: Plot title

    Examples:
        import networkx as nx
        from math4py.graph import create_graph
        from math4py.plot import plot_graph

        G = create_graph([(0,1), (1,2), (2,0)])
        plot_graph(G, filename="out/graph.pdf")
    """
    fig, ax = plt.subplots(figsize=(6, 6))

    if pos is None:
        pos = nx.spring_layout(G)

    nx.draw(
        G, pos, ax=ax,
        node_color=node_color,
        edge_color=edge_color,
        node_size=node_size,
        with_labels=with_labels,
        font_size=font_size,
        width=width,
        alpha=alpha,
    )

    if title:
        ax.set_title(title, fontsize=14)

    plt.tight_layout()

    if filename:
        os.makedirs(_OUT_DIR, exist_ok=True)
        filepath = os.path.join(_OUT_DIR, filename) if not os.path.isabs(filename) else filename
        plt.savefig(filepath, dpi=150, bbox_inches="tight")
        plt.close()
    else:
        plt.show()


def plot_directed_graph(
    G,
    filename: Optional[str] = None,
    pos: Optional[dict] = None,
    node_color: str = "#2196F3",
    edge_color: str = "#424242",
    node_size: int = 300,
    with_labels: bool = True,
    font_size: int = 10,
    arrow_size: float = 15,
    width: float = 1.0,
    alpha: float = 0.8,
    title: Optional[str] = None,
):
    r"""Plot a directed graph with arrows.

    Args:
        G: NetworkX directed graph
        filename: Output file
        pos: Node positions
        node_color: Node color
        edge_color: Edge color
        node_size: Node size
        with_labels: Show labels
        font_size: Label font size
        arrow_size: Arrow size for edges
        width: Edge width
        alpha: Transparency
        title: Plot title
    """
    fig, ax = plt.subplots(figsize=(6, 6))

    if pos is None:
        pos = nx.spring_layout(G)

    nx.draw(
        G, pos, ax=ax,
        node_color=node_color,
        edge_color=edge_color,
        node_size=node_size,
        with_labels=with_labels,
        font_size=font_size,
        width=width,
        alpha=alpha,
        arrows=True,
        arrowsize=arrow_size,
    )

    if title:
        ax.set_title(title, fontsize=14)

    plt.tight_layout()

    if filename:
        os.makedirs(_OUT_DIR, exist_ok=True)
        filepath = os.path.join(_OUT_DIR, filename) if not os.path.isabs(filename) else filename
        plt.savefig(filepath, dpi=150, bbox_inches="tight")
        plt.close()
    else:
        plt.show()


def plot_weighted_graph(
    G,
    filename: Optional[str] = None,
    pos: Optional[dict] = None,
    node_color: str = "#2196F3",
    edge_color: str = "#424242",
    node_size: int = 300,
    with_labels: bool = True,
    font_size: int = 10,
    width: float = 1.0,
    alpha: float = 0.8,
    show_weights: bool = True,
    title: Optional[str] = None,
):
    r"""Plot a weighted graph with edge labels.

    Args:
        G: NetworkX weighted graph
        filename: Output file
        pos: Node positions
        node_color: Node color
        edge_color: Edge color
        node_size: Node size
        with_labels: Show labels
        font_size: Label font size
        width: Edge width
        alpha: Transparency
        show_weights: Show edge weights
        title: Plot title
    """
    fig, ax = plt.subplots(figsize=(6, 6))

    if pos is None:
        pos = nx.spring_layout(G)

    edge_labels = {}
    if show_weights:
        for u, v, d in G.edges(data=True):
            edge_labels[(u, v)] = d.get("weight", "")

    nx.draw(
        G, pos, ax=ax,
        node_color=node_color,
        edge_color=edge_color,
        node_size=node_size,
        with_labels=with_labels,
        font_size=font_size,
        width=width,
        alpha=alpha,
    )

    if show_weights and edge_labels:
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)

    if title:
        ax.set_title(title, fontsize=14)

    plt.tight_layout()

    if filename:
        os.makedirs(_OUT_DIR, exist_ok=True)
        filepath = os.path.join(_OUT_DIR, filename) if not os.path.isabs(filename) else filename
        plt.savefig(filepath, dpi=150, bbox_inches="tight")
        plt.close()
    else:
        plt.show()


def plot_graph_properties(
    G,
    filename: Optional[str] = None,
    centrality: Optional[str] = "degree",
    node_color_map: Optional[dict] = None,
    node_size_scale: float = 500,
    title: Optional[str] = None,
):
    r"""Plot graph with node properties (centrality, clustering, etc.).

    Args:
        G: NetworkX graph
        filename: Output file
        centrality: Type ("degree", "betweenness", "closeness", "eigenvector")
        node_color_map: Custom node colors
        node_size_scale: Scale factor for node sizes
        title: Plot title
    """
    fig, ax = plt.subplots(figsize=(6, 6))

    if centrality == "degree":
        values = dict(G.degree())
    elif centrality == "betweenness":
        values = nx.betweenness_centrality(G)
    elif centrality == "closeness":
        values = nx.closeness_centrality(G)
    elif centrality == "eigenvector":
        values = nx.eigenvector_centrality(G)
    else:
        values = {n: 1 for n in G.nodes()}

    if node_color_map:
        colors = [node_color_map.get(n, "#2196F3") for n in G.nodes()]
    else:
        max_val = max(values.values()) if values else 1
        colors = [plt.cm.Blues(values[n] / max_val + 0.2) for n in G.nodes()]

    sizes = [node_size_scale * (values.get(n, 1) / max(values.values()) + 0.3) for n in G.nodes()]

    pos = nx.spring_layout(G)
    nx.draw(
        G, pos, ax=ax,
        node_color=colors,
        node_size=sizes,
        with_labels=True,
        font_size=10,
        width=1.0,
        alpha=0.8,
    )

    title_str = title or f"Graph - {centrality.title()} Centrality"
    ax.set_title(title_str, fontsize=14)

    plt.tight_layout()

    if filename:
        os.makedirs(_OUT_DIR, exist_ok=True)
        filepath = os.path.join(_OUT_DIR, filename) if not os.path.isabs(filename) else filename
        plt.savefig(filepath, dpi=150, bbox_inches="tight")
        plt.close()
    else:
        plt.show()


def plot_degree_distribution(
    G,
    filename: Optional[str] = None,
    title: Optional[str] = None,
):
    r"""Plot degree distribution histogram.

    Args:
        G: NetworkX graph
        filename: Output file
        title: Plot title
    """
    degrees = [d for n, d in G.degree()]

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.hist(degrees, bins=range(max(degrees) + 2), edgecolor="black", alpha=0.7)
    ax.set_xlabel("Degree", fontsize=12)
    ax.set_ylabel("Frequency", fontsize=12)
    ax.set_title(title or "Degree Distribution", fontsize=14)

    plt.tight_layout()

    if filename:
        os.makedirs(_OUT_DIR, exist_ok=True)
        filepath = os.path.join(_OUT_DIR, filename) if not os.path.isabs(filename) else filename
        plt.savefig(filepath, dpi=150, bbox_inches="tight")
        plt.close()
    else:
        plt.show()


def plot_adjacency_heatmap(
    G,
    filename: Optional[str] = None,
    title: Optional[str] = None,
):
    r"""Plot adjacency matrix as heatmap.

    Args:
        G: NetworkX graph
        filename: Output file
        title: Plot title
    """
    A = nx.to_numpy_array(G)

    fig, ax = plt.subplots(figsize=(6, 5))
    im = ax.imshow(A, cmap="Blues", edgecolor="white", linewidth=0.5)
    ax.set_title(title or "Adjacency Matrix", fontsize=14)
    plt.colorbar(im, ax=ax)

    plt.tight_layout()

    if filename:
        os.makedirs(_OUT_DIR, exist_ok=True)
        filepath = os.path.join(_OUT_DIR, filename) if not os.path.isabs(filename) else filename
        plt.savefig(filepath, dpi=150, bbox_inches="tight")
        plt.close()
    else:
        plt.show()


def plot_laplacian_heatmap(
    G,
    filename: Optional[str] = None,
    title: Optional[str] = None,
):
    r"""Plot Laplacian matrix as heatmap.

    Args:
        G: NetworkX graph
        filename: Output file
        title: Plot title
    """
    L = nx.laplacian_matrix(G).toarray()

    fig, ax = plt.subplots(figsize=(6, 5))
    im = ax.imshow(L, cmap="RdBu_r", edgecolor="white", linewidth=0.5)
    ax.set_title(title or "Laplacian Matrix", fontsize=14)
    plt.colorbar(im, ax=ax)

    plt.tight_layout()

    if filename:
        os.makedirs(_OUT_DIR, exist_ok=True)
        filepath = os.path.join(_OUT_DIR, filename) if not os.path.isabs(filename) else filename
        plt.savefig(filepath, dpi=150, bbox_inches="tight")
        plt.close()
    else:
        plt.show()


def plot_spectral_embedding(
    G,
    filename: Optional[str] = None,
    title: Optional[str] = None,
):
    r"""Plot graph using spectral layout.

    Args:
        G: NetworkX graph
        filename: Output file
        title: Plot title
    """
    fig, ax = plt.subplots(figsize=(6, 6))

    pos = nx.spectral_layout(G)

    nx.draw(
        G, pos, ax=ax,
        node_color="#2196F3",
        edge_color="#424242",
        node_size=300,
        with_labels=True,
        font_size=10,
        width=1.0,
        alpha=0.8,
    )

    if title:
        ax.set_title(title, fontsize=14)
    else:
        ax.set_title("Spectral Layout", fontsize=14)

    plt.tight_layout()

    if filename:
        os.makedirs(_OUT_DIR, exist_ok=True)
        filepath = os.path.join(_OUT_DIR, filename) if not os.path.isabs(filename) else filename
        plt.savefig(filepath, dpi=150, bbox_inches="tight")
        plt.close()
    else:
        plt.show()


def plot_shell(
    G,
    filename: Optional[str] = None,
    title: Optional[str] = None,
):
    r"""Plot graph using shell layout.

    Args:
        G: NetworkX graph
        filename: Output file
        title: Plot title
    """
    fig, ax = plt.subplots(figsize=(6, 6))

    n = G.number_of_nodes()
    shells = [list(range(i, min(i + 3, n + 1))) for i in range(0, n, 3)]
    pos = nx.shell_layout(G, nlist=shells)

    nx.draw(
        G, pos, ax=ax,
        node_color="#2196F3",
        edge_color="#424242",
        node_size=300,
        with_labels=True,
        font_size=10,
        width=1.0,
        alpha=0.8,
    )

    if title:
        ax.set_title(title, fontsize=14)
    else:
        ax.set_title("Shell Layout", fontsize=14)

    plt.tight_layout()

    if filename:
        os.makedirs(_OUT_DIR, exist_ok=True)
        filepath = os.path.join(_OUT_DIR, filename) if not os.path.isabs(filename) else filename
        plt.savefig(filepath, dpi=150, bbox_inches="tight")
        plt.close()
    else:
        plt.show()
