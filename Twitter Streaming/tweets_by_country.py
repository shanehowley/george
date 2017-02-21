
tweets_by_lang = statuses['lang'].value_counts()

tweets_by_country = statuses['country'].value_counts()


fig = plt.figure()

ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

ax1.tick_params(axis='x', labelsize=15)
ax1.tick_params(axis='y', labelsize=10)
ax1.set_xlabel('Tweet Languages', fontsize=15)
ax1.set_ylabel('Number of tweets', fontsize=15)
ax1.xaxis.label.set_color('#666666')
ax1.yaxis.label.set_color('#666666')
ax1.tick_params(axis='x', colors='#666666')
ax1.tick_params(axis='y', colors='#666666')

ax1.set_title('Top 10 languages', fontsize=15, color='#666666')

tweets_by_lang[:10].plot(ax=ax1, kind='bar', color='#FF7A00')

for spine in ax1.spines.values():
    spine.set_edgecolor('#666666')

ax2.tick_params(axis='x', labelsize=15)
ax2.tick_params(axis='y', labelsize=10)
ax2.set_xlabel('Countries', fontsize=15)
ax2.set_ylabel('Number of tweets', fontsize=15)
ax2.xaxis.label.set_color('#666666')
ax2.yaxis.label.set_color('#666666')
ax2.tick_params(axis='x', colors='#666666')
ax2.tick_params(axis='y', colors='#666666')

ax2.set_title('Top 10 Countries', fontsize=15, color='#666666')

tweets_by_country[:10].plot(ax=ax2, kind='bar', color='#FF7A00')

for spine in ax2.spines.values():
    spine.set_edgecolor('#666666')


plt.show()
tweets_by_lang = statuses['lang'].value_counts()

tweets_by_country = statuses['country'].value_counts()

fig = plt.figure()

ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

ax1.tick_params(axis='x', labelsize=15)
ax1.tick_params(axis='y', labelsize=10)
ax1.set_xlabel('Tweet Languages', fontsize=15)
ax1.set_ylabel('Number of tweets' , fontsize=15)
ax1.xaxis.label.set_color('#666666')
ax1.yaxis.label.set_color('#666666')
ax1.tick_params(axis='x', colors='#666666')
ax1.tick_params(axis='y', colors='#666666')

ax1.set_title('Top 10 languages', fontsize=15, color='#666666')

tweets_by_lang[:10].plot(ax=ax1, kind='bar', color='#FF7A00')


for spine in ax1.spines.values():
        spine.set_edgecolor('#666666')


ax2.tick_params(axis='x', labelsize=15)
ax2.tick_params(axis='y', labelsize=10)
ax2.set_xlabel('Countries', fontsize=15)
ax2.set_ylabel('Number of tweets' , fontsize=15)
ax2.xaxis.label.set_color('#666666')
ax2.yaxis.label.set_color('#666666')
ax2.tick_params(axis='x', colors='#666666')
ax2.tick_params(axis='y', colors='#666666')

ax2.set_title('Top 10 Countries', fontsize=15, color='#666666')


tweets_by_country[:10].plot(ax=ax2, kind='bar', color='#FF7A00')

for spine in ax2.spines.values():
        spine.set_edgecolor('#666666')

plt.show()