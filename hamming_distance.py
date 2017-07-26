
def hamming_distance_float(v, w):
    distance = 0

    for i, _ in enumerate(v):
        if v[i] > w[i]:
            distance = distance + (v[i] - w[i])
        else:
            distance = distance + (w[i] - v[i])

    return distance


def hamming_distance(v, w):
    distance = 0

    for i, _ in enumerate(v):
        if v[i] != w[i]:
            distance = distance + 1

    return distance


def hamming_distance_matrix(vector):
    return [[hamming_distance(v, w) for w in vector] for v in vector]
