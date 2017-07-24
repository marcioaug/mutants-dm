from matplotlib import pyplot


friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

pyplot.scatter(friends, minutes)

for label, friend_count, minute_count in zip(labels, friends, minutes):
    pyplot.annotate(
        label,
        xy=(friend_count, minute_count),
        xytext=(5, -5),
        textcoords='offset points'
    )

pyplot.title("Minutos Diários vs. Número de Amigos")
pyplot.xlabel("# de amigos")
pyplot.ylabel("munutos diários passados no site")

pyplot.show()