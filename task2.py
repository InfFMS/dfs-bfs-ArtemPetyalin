# Даны N городов и M дорог между ними. Дороги двусторонние (граф неориентированный). 
# Известно, что города разделены на группы (острова), 
# между которыми дорог нет. То есть граф состоит из нескольких компонент связности (островов). 
# Необходимо ответить на следующие вопросы:
# 
# 1. Есть ли путь между двумя заданными городами (вершинами)?
# 2. Сколько всего островов (компонент связности) в графе?
# 3.Перечислить, какие города принадлежат каждому острову.
# 
# Входные данные:
# Первая строка: N (количество городов) и M (количество дорог).
# Следующие M строк: пары чисел u и v, обозначающие дорогу между городами u и v.
# Затем вводится два числа: start и end — номера городов, между которыми нужно проверить наличие пути.
# 
# Выходные данные:
# Ответ на вопрос, есть ли путь между start и end ("YES" или "NO").
# Количество островов (компонент связности) в графе.
# Список городов для каждого острова (в порядке возрастания номеров островов).

# Пример 1:
# 5 3
# 1 2
# 2 3
# 4 5
# 1 4
# 
# Ожидаемый вывод:
# 
# NO
# 2
# 1: [1, 2, 3]
# 2: [4, 5]

# Пример 2:
# 6 4
# 1 2
# 3 4
# 5 6
# 2 3
# 3 5
# 
# Ожидаемый вывод:
# 
# YES
# 1
# 1: [1, 2, 3, 4, 5, 6]

# Пример 3:
# 7 0
# 1 2
# 
# Ожидаемый вывод:
# 
# NO
# 7
# 1: [1]
# 2: [2]
# 3: [3]
# 4: [4]
# 5: [5]
# 6: [6]
# 7: [7]

A = input().split()
N = A[0]
M = A[1]
graph = {i:[] for i in range(1, int(N) + 1)}
list_u = []
list_v = []

for i in range(int(M)):
    a = input().split()
    graph[int(a[0])].append(int(a[1]))
    graph[int(a[1])].append(int(a[0]))
print(graph)

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

path = input().split()
breadth_search(graph, int(path[0]))

for elem in vis:

    if elem == int(path[1]):
        print('YES')
        break

    if elem == int(vis[-1]):
        print('NO')

order = []
def depth_serach(graph, loc):

    if loc not in order:
        order.append(loc)

        for branch in graph[loc]:
            depth_serach(graph, branch)

depth_serach(graph, 1)

#for i in range(int(M)):


