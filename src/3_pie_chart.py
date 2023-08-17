from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')
"""
    their sum doesn't need to be 100, Its going to be 
    calculated by Pie automatically
"""

slices = [30, 23, 27, 20]
labels = ['A_cat', 'B_cat', 'C_cat', 'D_cat']
colors = ['#008fd5', '#fc4f30', '#e5ae37', '#6d904f']
"""
    This option is for detaching some element
"""
explodes = [0.1, 0.1, 0.3, 0.1]
plt.pie(
        slices,
        labels=labels,
        colors=colors,
        explode=explodes,
        # shadow=True,
        # startangle=90,
        autopct='%1.1f%%',
        wedgeprops={'edgecolor': 'gray'}
)

plt.ylabel('Pie chart')
plt.tight_layout()
plt.show()
