from matplotlib import pyplot as plt
import pandas as pd
df=pd.read_csv("iris.csv")
df=["petal.length"].plot(kind="List",edgecolor="black",bins=49)
plt.title("Histogram")
plt.xlabel("petal length")
plt.show()
