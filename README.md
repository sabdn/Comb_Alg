Центры сети - Задача 1056
Суть задачи заключается в нахождении компьютеров в компьютерной сети, 
которые имеют минимальное расстояние до самого удаленного от них компьютера.

Ссылка на задачу: 1056 - Центры сети (https://acm.timus.ru/problem.aspx?space=1&num=1056)

Как работает код:
1) Код начинается определения класса Node. Каждый экземпляр Node имеет свойство p (для хранения родительского узла), 
v (для хранения соседних узлов), d (для хранения расстояния до узла) и visited (для отметки посещенных узлов).
2) Затем создается список nodes из Node объектов, равное количеству компьютеров в сети 
плюс один (для удобства индексации, начинающейся с 1).
3) Код считывает количество компьютеров n и затем считывает протокол сети, соединяя каждый компьютер с его родительским
компьютером.
4) Далее, выполняется поиск в глубину для определения максимального расстояния от первого компьютера (max_distance) и узла
с этим максимальным расстоянием (maxnode).
5) Затем проводится второй поиск в глубину, начиная с maxnode для определения нового max_distance и соответствующего
maxnode.
6) После этого, код перебирает все узлы от maxnode к началу, выбирая те, которые находятся в середине максимальной
дистанции. Это и будут центры сети.
7) В конце, порядковые номера всех центров сети выводятся в порядке возрастания.
Этот алгоритм работает, потому что он ищет самую длинную цепь в сети, затем определяет узлы в середине этой цепи, что
соответствует определению центра сети.
