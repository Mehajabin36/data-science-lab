from matplotlib import pyplot
from numpy import array

fig, ax = pyplot.subplots()

a = array([22, 87, 5, 43, 56, 73, 55, 5, 4, 11, 20, 51, 5, 79, 31, 271])

ax.hist(a, bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

ax.set_title("Histogram of Result")
ax.set_xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
ax.set_xlabel("Marks")
ax.set_ylabel("No. of Students")

pyplot.show()
