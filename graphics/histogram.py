from matplotlib import pyplot
from collections import Counter


grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
decile = lambda grade: grade // 10 * 10
histogram = Counter(decile(grade) for grade in grades)

pyplot.bar([x for x in histogram.keys()], histogram.values(), 8)

pyplot.axis([-5, 105, 0, 5])
pyplot.xticks([10 * i for i in range(11)])
pyplot.xlabel("Decil")
pyplot.ylabel("# de Alunos")
pyplot.title("Distribuição das Notas do Teste 1")

pyplot.show()