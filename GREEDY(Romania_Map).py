graph = {
    "Arad": ["Zerind", "Sibiu", "Timisoara"],
    "Zerind": ["Arad", "Oradea"],
    "Oradea": ["Zerind", "Sibiu"],
    "Sibiu": ["Fagaras", "Rimnicu", "Arad", "Oradea"],
    "Timisoara": ["Arad", "Lugoj"],
    "Lugoj": ["Timisoara", "Mehadia"],
    "Mehadia": ["Lugoj", "Dobreta"],
    "Dobreta": ["Mehadia", "Craiova"],
    "Craiova": ["Dobreta", "Rimnicu", "Pitesti"],
    "Rimnicu": ["Craiova", "Sibiu", "Pitesti"],
    "Fagaras": ["Sibiu", "Bucharest"],
    "Pitesti": ["Rimnicu", "Craiova", "Bucharest"],
    "Bucharest": ["Fagaras", "Pitesti", "Giurgiu"],
    "Giurgiu": ["Bucharest"]
}
straight_line_distance = {
    "Arad" : 366,
    "Bucharest" : 0,
    "Craiova" : 160,
    "Dobreta": 242,
    "Fagaras": 178,
    "Giurgiu":77,
    "Hirsova": 151,
    "lasi" : 226,
    "Lugoj" : 244,
    "Mehedia": 241,
    "Neamt": 234,
    "Oradea":380,
    "Pitesti" : 98,
    "Rimnicu" : 193,
    "Sibiu" : 253,
    "Timisoara": 329,
    "Urziceni": 80,
    "Vasiui":191 , 
    "Zerind" : 373
}
open = []
close = []
open.append(('/' , 'Arad' , 366))
while open:
    minWeightCity = open[0]
    for current_node in open:
        if current_node[2] < minWeightCity[2] :
            minWeightCity = current_node
    currNode = minWeightCity
    open.remove(minWeightCity)
    close.append(currNode)
    if currNode[1] == 'Bucharest':
        print(f'Goal is Found {currNode}')
        break
    else:
        print(currNode[2])
        childNodes = graph[currNode[1]]
        print(childNodes)
        for child in childNodes:
            cond = True
            for tuple in close:
                if child ==  tuple[1]:
                    cond = False
                    break
            if cond:
                weight = 0
                for key,value in straight_line_distance.items():
                    if(key == child):
                        weight = value
                open.append((currNode[1] , child ,weight))
print("Nodes in closed list are : " , close)


print(close)
path = []
selected_node = None
for node in close:
    path.append(node)
path.reverse()
for node in path:
    if node[1] == 'Bucharest':
        selected_node = node
        break

shortest_path = []
shortest_path.append(selected_node)
for node in path:
    if selected_node[0] == node[1]:
        shortest_path.insert(0, node)
        selected_node = node
print("shortest")
print(shortest_path)