import random

from matplotlib import pyplot

from transform import data_set
from shamaila.kmeans import ShamailaKMeans
from shamaila.greedy_test_set import greedy_test_set, kill_mutants


def eliminate_pseudo_equivalent(vectors):
    return [v for v in vectors if sum(v) != 0 and sum(v) != len(v)]

k = 15
mutants = eliminate_pseudo_equivalent(data_set)

clusterer = ShamailaKMeans(k)
assignments = clusterer.train(mutants)

clusters = [[m for m, a in zip(mutants, assignments) if a == k] for k in range(k)]

sc = []

for cluster in clusters:
    if len(cluster) >= 1:
        sc.append(random.sample(cluster, 1)[0])

tc = greedy_test_set(sc)

print(len(tc))
print(kill_mutants(mutants, tc))



# clusters.sort(key=lambda c: len(c), reverse=True)
#
# pyplot.bar(range(len(clusters)), [len(c) for c in clusters], 1)
#
# pyplot.title("Mutants Per Cluster, k=%i" % k)
#
# pyplot.axis([0, k + 1, 0, len(clusters[0]) + 5])
# pyplot.ylabel("Number of mutants")
# pyplot.xlabel("Number of the cluster")
#
#
# pyplot.show()



