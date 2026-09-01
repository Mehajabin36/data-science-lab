from matplotlib import pyplot
rollno=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
marks=[22,87,5,43,56,73,55,54,11,20,51,5,79,31,77]
fig,ax=pyplot.subplots(1,1)
ax.scatter(rollno,marks)
ax.set_title("scatter plot")
ax.set_xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
ax.set_yticks([25,50,75,100])
ax.set_xlabel("rollno")
ax.set_ylabel("marks")
pyplot.show()

