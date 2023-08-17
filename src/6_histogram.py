import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('../resources/survey_respondant.csv')
salaries = data['Age']

age_min = data['Age'].min()
age_max = data['Age'].max()
median_age = data['Age'].median()

age_ranges = list(range(age_min, age_max, 5))

plt.hist(salaries, bins=age_ranges, edgecolor='k', log=True)
plt.axvline(median_age, color='r', label='Median Age', linewidth=1)

plt.legend()
plt.tight_layout()
plt.title('Histogram charts when we want to group data')
plt.xlabel('Ages')
plt.ylabel('Number of persons')

plt.show()
