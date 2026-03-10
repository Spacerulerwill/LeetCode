from typing import List
from collections import defaultdict


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        connections = defaultdict(set)
        for u, v in edges:
            connections[u].add(v)
            connections[v].add(u)

        def path_exists(current: int, visited: set[int]) -> bool:
            if current == destination:
                return True
            visited.add(current)
            for neighbour in connections[current]:
                if neighbour in visited:
                    continue
                if path_exists(neighbour, visited):
                    return True
            return False

        return path_exists(source, set())
