from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv("iris.csv")

df["petal.length"].plot(kind="hist", edgecolor="black", bins=49)

plt.title("Histogram")
plt.xlabel("Petal length")
plt.show()
