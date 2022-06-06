from matplotlib import pyplot

# Exercise 1

x = [0,1,2,3,4,5]
y = [12,2,16,6,3,5]

pyplot.scatter(x, y, marker='x')
pyplot.suptitle('Title of plot :)')
pyplot.xlabel('x-axis')
pyplot.ylabel('y-axis')
pyplot.annotate('maximum',xy=(2,16), xytext=(3,12), arrowprops=dict(facecolor='black', shrink=0.05))
pyplot.show()