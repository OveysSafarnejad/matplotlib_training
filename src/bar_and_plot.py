import matplotlib.pyplot as plt

ages = list(range(25, 35))

python_devs = list((33_900., 35_000, 39_000, 49_000, 50_000, 54_300, 57_000,
                    65_000, 67_000, 70_000))
js_devs = list((
               25_900., 27_000, 29_000, 32_000, 40_000, 44_300, 53_000, 59_000,
               66_000, 69_000))

plt.plot(ages, python_devs, label='Py')
plt.plot(ages, js_devs, label='JS')

all_developers = list((30_900., 31_000, 35_000, 40_000, 45_000, 49_300, 55_000,
                       60_000, 66_000, 69_000))

plt.bar(ages, all_developers, label='all')

plt.xlabel('Ages')
plt.ylabel('Median salary (Euro)')
plt.title('Median salary based on age')

plt.show()
