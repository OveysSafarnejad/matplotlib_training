import pandas as pd
from matplotlib import pyplot as plt


plt.style.use('fivethirtyeight')
top_200_videos_df = pd.read_csv('../resources/youtube_top_200.csv')

number_of_views = top_200_videos_df['view_count']
likes = top_200_videos_df['likes']
like_to_dislike_ratio = top_200_videos_df['ratio']

plt.scatter(
    number_of_views,
    likes,
    c=like_to_dislike_ratio,
    # https://matplotlib.org/stable/tutorials/colors/colormaps.html
    cmap='OrRd',
    marker='.',
)
plt.xscale('log')
plt.yscale('log')

color_bar = plt.colorbar()
color_bar.set_label('Like/dislike ratio')

plt.tight_layout()
plt.legend()
plt.xlabel('Played')
plt.ylabel('Likes')

plt.title('Youtube scatter diagram')
plt.show()


