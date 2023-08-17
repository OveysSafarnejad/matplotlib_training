import pandas as pd
from matplotlib import pyplot as plt

"""
    What is figure?
    It's a container for the plot. We can think of a whole window that comes up
    when we starting a plot.
    
    What is Axis?
    The axis is the actual plot.
    
    So, a figure can have multiple plots.
    Here we are going to modify the following code.
"""

plt.style.use('seaborn-v0_8')

data = pd.read_csv('../resources/developers.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

# plt.plot(ages, py_salaries, label='Python')
# plt.plot(ages, js_salaries, label='JavaScript')
#
# plt.plot(ages, dev_salaries, color='#444444',
#          linestyle='--', label='All Devs')
#
# plt.legend()
#
# plt.title('Median Salary (USD) by Age')
# plt.xlabel('Ages')
# plt.ylabel('Median Salary (USD)')
#
# plt.tight_layout()
#
# plt.show()

# This will create a plot with two Axes
figure, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)

ax1.plot(ages, dev_salaries, color='#444', linestyle='--', label='Mix')
ax1.legend()
ax1.set_title('Median Salary for All Developers')
ax1.set_ylabel('Median Salary (USD)')

ax2.plot(ages, py_salaries, label='Python')
ax2.plot(ages, js_salaries, label='JavaScripts')
ax2.legend()
ax2.set_xlabel('Ages')
ax2.set_ylabel('Median Salary (USD)')

plt.tight_layout()
plt.show()
