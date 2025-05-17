# Напишите алгоритм поиска в ширину (BFS)
#
# Формат входных данных:
# Граф задаётся в виде словаря, где ключи — вершины, а значения — списки смежных вершин.
#
# Обход начинается с заданной стартовой вершины.
# Требуется:
# 1.Реализовать BFS — обход графа в ширину.
# 2.Вернуть самый коротки маршрут от точки старта до точки назначения.

# Пример входных данных
# city_map = {  
#     'Home': ['Park', 'School', 'Mail'],  
#     'Park': ['Home', 'Museum', 'Cafe'],  
#     'School': ['Home', 'Library', 'Mail'],  
#     'Mail': ['Home', 'School', 'Hospital'],  
#     'Library': ['School', 'Hospital'],  
#     'Hospital': ['Library', 'Mail', 'Office'],  
#     'Cafe': ['Park', 'Theater', 'Office'],  
#     'Museum': ['Park', 'Shop'],  
#     'Shop': ['Museum', 'Theater'],  
#     'Theater': ['Shop', 'Cafe'],  
#     'Office': ['Cafe', 'Hospital']  
# }
# start = "Home"
# finish = "Theater"
#
# Пример выходных данных
# ['Home', 'Park', 'Cafe', 'Theater']
vis = []
def breadth_search(graph, loc):
    unvs = []
    unvs.append(loc)

    while unvs:
        next = unvs[0]
        unvs.pop(0)

        if next not in vis:
            vis.append(next)

            for i in graph[next]:

                if i not in vis:
                    unvs.append(i)

city_map = {
     'Home': ['Park', 'School', 'Mail'],
     'Park': ['Home', 'Museum', 'Cafe'],
     'School': ['Home', 'Library', 'Mail'],
     'Mail': ['Home', 'School', 'Hospital'],
     'Library': ['School', 'Hospital'],
     'Hospital': ['Library', 'Mail', 'Office'],
     'Cafe': ['Park', 'Theater', 'Office'],
     'Museum': ['Park', 'Shop'],
     'Shop': ['Museum', 'Theater'],
     'Theater': ['Shop', 'Cafe'],
     'Office': ['Cafe', 'Hospital'] }

breadth_search(city_map, 'Home')
print(vis)