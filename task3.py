# Реализовать алгоритм Кана для топологической сортировки
# Пример с пошаговой работой алгоритма
# Граф: A → B → C
#       A → D

graf = {"A" : ["B", "C"],
        "B" : ["C"],
        "C" : [],
        "D" : []}

# Шаги:
# 1. Начальные вершины без входящих рёбер: [A]
# 2. Обрабатываем A → результат [A], обновляем степени B(1→0), D(1→0)
# 3. Вершины для обработки: [B, D]
# 4. Обрабатываем B → результат [A,B], обновляем степень C(1→0)
# 5. Обрабатываем D → результат [A,B,D]
# 6. Обрабатываем C → результат [A,B,D,C]
# 7. Все вершины обработаны → сортировка завершена

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

print(answer[1:])