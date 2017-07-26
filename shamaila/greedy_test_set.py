from linear_algebra import vector_sum


def greedy_test_set(cluster):

    test_set = []
    survivors = [c for c in cluster]

    while len(survivors) > 0:
        sum_killed_mutants = vector_sum(survivors)

        if len(sum_killed_mutants) > 0:
            i, t = max(enumerate(sum_killed_mutants), key=lambda e: e[1])
            test_set.append(i)
            survivors = [c for c in survivors if c[i] == 0]

    # test_test_set(cluster, test_set)
    return test_set


def test_test_set(cluster, test_set):
    survivors = [c for c in cluster]

    print("------------------------")
    print("Test set: %s" % str(test_set))

    for i, test in enumerate(test_set):
        print("Using test #%i" % test)
        survivors = [c for c in survivors if c[test] == 0]
        if len(survivors) > 0:
            for i, survivor in enumerate(survivors):
                print("Mutant #%i survived the test #%i. %i of %i survived." % (i, test, len(survivors), len(cluster)))
        else:
            print("All %i mutants were killed. %i test(s) of %i used." % (len(cluster), i + 1 , len(test_set)))
            break


def kill_mutants(mutants, test_set):

    survivors = mutants.copy()

    for test in test_set:
        survivors = [s for s in survivors if s[test] == 0]

    return (len(mutants) - len(survivors)) / len(mutants)
