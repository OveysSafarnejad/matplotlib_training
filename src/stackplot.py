from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

game_progress = list(range(0, 11))

dev1_score = [8, 7, 4, 5, 1, 4, 3, 0, 1, 4, 3]
dev2_score = [1, 1, 2, 4, 6, 4, 7, 0, 0, 0, 0]
dev3_score = [1, 2, 4, 1, 3, 2, 0, 10, 9, 6, 7]

labels = ['D1', 'D2', 'D3']
colors = ['#6d904f', '#fc4f30', '#008fd5']

plt.stackplot(
    game_progress, dev1_score, dev2_score, dev3_score,
    labels=labels,
    colors=colors
)

plt.legend(loc=(0.07, 0.05))  # percentages from the left and the bottom
plt.ylabel('Stack plot')
plt.tight_layout()
plt.show()
