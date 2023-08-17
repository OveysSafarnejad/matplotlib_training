import pandas as pd
from matplotlib import pyplot as plt

developers = pd.read_csv('../resources/developers.csv')

ages = developers.Age
py_salaries = developers.Python
all_devs = developers.All_Devs

plt.plot(ages, all_devs, color='#444444', linestyle='--',
         label='All Developers')
plt.plot(ages, py_salaries, color='b', label='Python Developers')

medium_salary = 57890
# plt.fill_between(ages, py_salaries, alpha=0.25)
plt.fill_between(
    ages, py_salaries,
    where=(py_salaries > medium_salary),
    interpolate=True,
    y2=medium_salary,
    alpha=0.25,
    label='Above average'
)

plt.fill_between(
    ages, py_salaries,
    where=(py_salaries <= medium_salary),
    interpolate=True,
    y2=medium_salary,
    color='red',
    alpha=0.25,
    label='Below average'
)

plt.tight_layout()
plt.legend()
plt.xlabel('Ages')
plt.ylabel('Median Salaries')

plt.title('Average salaries for developers')

plt.show()
