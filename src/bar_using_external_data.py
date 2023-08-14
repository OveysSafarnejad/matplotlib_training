import csv
from collections import Counter

import matplotlib.pyplot as plt

with open('../resources/data.csv') as csv_data:
    csv_reader = csv.DictReader(csv_data)
    counter = Counter()
    for record in csv_reader:
        counter.update(record.get('LanguagesWorkedWith').split(';'))

top_10 = counter.most_common(20)
languages = [item[0] for item in top_10]
popularity = [item[1] for item in top_10]
languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)
plt.xlabel('popularity')
plt.title('Most 10 popular programming languages')
plt.show()