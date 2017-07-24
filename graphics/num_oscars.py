from matplotlib import pyplot

movies = ['Annie Hall', 'Ben-Hur', 'Casablanca', 'Gandhi', 'West Side Story']
num_oscars = [5, 11, 3, 8, 10]

xs = range(len(movies))

pyplot.bar(xs, num_oscars)

pyplot.ylabel("# de Premiações")
pyplot.title("Meu Filmes Favoritos")
pyplot.xticks(xs, movies)

pyplot.show()
