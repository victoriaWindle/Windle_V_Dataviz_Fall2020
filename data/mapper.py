import matplotlib.pyplot as plt

years = [1924, 1936, 1952, 1996, 1994, 2002, 2014]


medals = [9, 13, 17, 20, 40, 75, 90]

plt.plot(years, medals, color=(255/255, 100/255, 100/155), linewidth=3.0)

plt.ylabel("Years of Winter Olympics")

plt.xlabel("# of Medals Won by Canadians")

plt.show()



