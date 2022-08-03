import queue
from re import A
import sys
from sqlalchemy import null


graph = {'A': ['B','C'],
        'B': ['A','D','C'],
        'C': ['A','B','D','E'], 
        'D': ['B','C','E','F'],
        'E': ['C','D','F'],
        'F': ['D','E']
        }


def bfs(graph, src):
    discovered = set()
    queue = []
    queue.append(src)
    discovered.add(src)


    while len(queue) != 0:
        v = queue.pop(0)
        print(v)
        for i in graph[v]:
            if i not in discovered:
                queue.append(i)
                discovered.add(i)

def unweighted_shortest(graph, src):
    discovered = set()
    queue = []
    queue.append(src)
    discovered.add(src)
    cost = {}
    cost[src] = 0

    while len(queue) != 0: 
        v = queue.pop(0)
        print(v)
        for i in graph[v]:
            if i not in discovered:
                queue.append(i)
                discovered.add(i)
                cost[i] = cost[v] + 1
    return(cost)

def unweighted_shortest_recover(graph, src, target):
    discovered = set()
    queue = []
    queue.append(src)
    discovered.add(src)
    previous = {}
    spath = []

    while len(queue) != 0:
        v = queue.pop(0)
        print(v)
        for i in graph[v]:
            if i not in discovered:
                queue.append(i)
                discovered.add(i)
                previous[i] = v
    return(previous)


print(unweighted_shortest_recover(graph, 'A', 'B'))