from task1 import *

def dfs(g, fr, to, path=[], visited=set()):
    path = path + [fr]
    visited.add(fr)
    if fr == to:
        return path
    for neighbor in g.neighbors(fr):
        if neighbor not in visited:
            new_path = dfs(g, neighbor, to, path, visited)
            if new_path:
                return new_path
    return None


def bfs(g, fr, to):
    visited = set()
    queue = [(fr, [fr])]
    while queue:
        current, path = queue.pop(0)
        visited.add(current)
        if current == to:
            return path
        for neighbor in g.neighbors(current):
            if neighbor not in visited and (neighbor, path + [neighbor]) not in queue:
                queue.append((neighbor, path + [neighbor]))
    return None


if __name__ == "__main__":
    print(f'{"dfs":5}:', dfs(G, 'A', 'H'))
    print(f'{"bfs":5}:', bfs(G, 'A', 'H'))
