from matplotlib import pyplot as plt


x_axis = list(range(25,35))
y_axis = list((33_900., 35_000, 39_000, 42_000, 50_000, 54_300, 57_000, 65_000, 67_000, 70_000))
plt.plot(x_axis, y_axis)
plt.xlabel('Ages')
plt.ylabel('Median salary (Euro)')
plt.title('Median salary based on age')

plt.show()
