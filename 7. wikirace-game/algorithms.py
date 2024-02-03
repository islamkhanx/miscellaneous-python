from collections import deque, defaultdict
from typing import List, DefaultDict, Tuple, Dict
import csv
import heapq


def grap_transform(
        edges: List[List[int | int]],
        weighted: bool = False
        ) -> DefaultDict[int, List[int | Tuple]]:

    """Transforms edges to graph in adjacency list form

    Args:
        edges (List[List[int | int]]): edges and weigths(optional)
        weighted (bool, optional): Whether edges have weights.
        Defaults to False.

    Returns:
         DefaultDict[int, List[int | Tuple]]
    """
    adjacency_list = defaultdict(list)

    if weighted:
        for edge in edges:
            i, j, weight = edge
            adjacency_list[i].append((j, weight))
    else:
        for edge in edges:
            i, j = edge
            adjacency_list[i].append(j)

    return adjacency_list


def read_graph(
        path: str,
        weithed: bool = False
        ) -> DefaultDict[int, List[int | Tuple[int, int]]]:
    """Creates a graph from file

    Args:
        path (str): path to csv file with
        weithed (bool, optional): Whether edges have weights.
        Defaults to False.

    Returns:
        DefaultDict[int, List[int | Tuple[int, int]]]: graph (adjacency list)
    """
    edges = []
    with open(path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader, None)  # drop header
        if weithed:
            for row in csv_reader:
                edges.append([int(row[0]), int(row[2]), len(row[1])])
        else:
            for row in csv_reader:
                edges.append([int(row[0]), int(row[2])])

    graph = grap_transform(edges, weithed)
    return graph


def dijkstra(graph: DefaultDict[int, List[Tuple[int, int]]],
             start: int, target: int) -> List[int]:
    """Implementation of Dijkstara algorithm
    to find shotest path from Start to target in a weithed graph

    Args:
        graph (DefaultDict[int, List[Tuple[int, int]]]): graph
        start (int): start node
        target (int): target node

    Returns:
        List[int]: shortes path if such is present, else []
    """
    priority_queue = [(0, start)]
    distances = defaultdict(lambda: float('inf'))
    distances[start] = 0
    predecessors = {start: None}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue

        if current_node == target:
            path = []
            while current_node is not None:
                path.insert(0, current_node)
                current_node = predecessors[current_node]
            return path

        for neighbor, edge_weight in graph[current_node]:
            distance = current_distance + edge_weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return []


def shortest_path(graph: DefaultDict[int, List[int]],
                  start: int, end: int) -> List[int]:
    """Algorithm to find shortest bath between two nodes in
    grapth without weights
    Args:
        graph (DefaultDict[int, List[int]]):graph without weights
        start (int): start node
        end (int): target node

    Returns:
        List[int]: shortest path if ,such is present else epmty path
    """

    visited = set()
    queue = deque([(start, [start])])

    while queue:
        current, path = queue.popleft()

        if current == end:
            return path
        if current not in visited:
            visited.add(current)
            neighbors = graph[current]

            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    return []


def read_pid_map(path: str) -> Tuple[Dict]:
    """Reads file with pagelink id to title mapping
    Args:
        path (str): file path

    Returns:
        Tuple[Dict]: endcoder and decoder dictionaries,
        id's are integers!
    """
    pid_from_ptitle = {}
    ptitle_from_id = {}
    with open(path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader, None)  # drop header
        for row in csv_reader:
            ptitle_from_id[int(row[2])] = row[1]
            pid_from_ptitle[row[1]] = int(row[2])

    return pid_from_ptitle, ptitle_from_id


PATH = 'simple_english_wiki_pagelinks.csv'
PID_FROM_PTITLE, PTITLE_FROM_PID = read_pid_map(PATH)
