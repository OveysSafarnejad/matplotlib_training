import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import dates


prices = pd.read_csv('../resources/bitcoin_prices.csv')

prices['Date'] = pd.to_datetime(prices['Date'])
report_dates = prices['Date'].sort_values()
price_list = prices['Close']

plt.plot_date(report_dates, price_list, linestyle='solid')
plt.gcf().autofmt_xdate()  # get current figures

date_format = dates.DateFormatter('%d.%m.%Y')
plt.gca().xaxis.set_major_formatter(date_format)

plt.tight_layout()
plt.show()

