def all_ways(graph, start, end, way =[]):
    way = way + [start]
    if start == end:
        return [way]
    if start not in graph or end not in graph:
        return "Какой-то из этих точек не существует"
    ways = []
    for el in graph[start]:
        if el not in way:
            new_ways = all_ways(graph, el, end, way)
            ways.extend(new_ways)
    return ways

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
start = 'A'
end = 'F'
print("Все пути из точки", start, "в точку ", end, ":", all_ways(graph, start, end))