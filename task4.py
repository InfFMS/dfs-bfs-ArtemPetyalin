# Дан список курсов университета и их пререквизитов. Нужно определить,
# можно ли окончить все курсы, и если да, то вывести один из возможных порядков их изучения.
#
# Формат ввода:
# Первая строка: n (число курсов), m (число зависимостей).
# Следующие m строк: a b (курс b требует прохождения курса a).
#
# Формат вывода:
# Если циклов нет, вывести любой допустимый порядок курсов.
# Если есть цикл, вывести -1.

# Пример 1 (нет циклов)
# Ввод:
# 4 3
# 1 2
# 2 3
# 1 4
# Граф:
# 1 → 2 → 3
# 1 → 4
# Вывод:
# 1 2 4 3  # Или 1 4 2 3

# Пример 2 (есть цикл)
# Ввод:
# 3 3
# 1 2
# 2 3
# 3 1
# Граф:
# 1 → 2 → 3 → 1 (цикл!)
# Вывод:
# -1

A = input().split()
N = int(A[0])
M = int(A[1])
graf = {}
keys = []

for i in range(1, N + 1):
    graf[i] = []

for i in range(M):
    B = input().split()
    graf[int(B[0])].append(int(B[1]))

cycle = 0
for i in range(1 , 1 + M):
    counter = 0

    if len(graf[i]) == 0:
        counter += 1

    for j in list(graf.keys()):
        if i in graf[j]:
            counter += 1

    if counter >= 2:
        break

    if i == M:
        print(-1)
        cycle = 1
        break

if cycle == 0:

    container = []

    for i in list(graf.keys()):

        if len(graf[i]) == 0:
            container.append(i)

    answer = ''
    i = 0

    while i < len(container):
        answer = answer + ' ' + str(container[i])

        for j in list(graf.keys()):

            if container[i] in graf[j]:
                graf[j].remove(container[i])

            if len(graf[j]) == 0 and j not in container:
                container.append(j)

        i += 1

    print(answer[::-1])