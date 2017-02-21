import json
import pandas
import matplotlib.pyplot as plt

tweets_data_path = 'tweet_mining.json'

results = []
tweets_file = open(tweets_data_path, "r")
for tweet_line in tweets_file:
    try:
        status = json.loads(tweet_line)
        results.append(status)
    except:
        continue

print len(results)

statuses = pandas.DataFrame()

statuses['text'] = map(lambda status: status['text'], results)

statuses['lang'] = map(lambda status: status['lang'], results)

statuses['country'] = map(lambda status: status['place']['country'] if status['place'] != None else None, results)

tweets_by_lang = statuses['lang'].value_counts()

fig = plt.figure()

ax = fig.add_subplot(1,1,1)

ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Tweet Languages', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.xaxis.label.set_color('#666666')
ax.yaxis.label.set_color('#666666')
ax.tick_params(axis='x', colors='#666666')
ax.tick_params(axis='y', colors='#666666')

ax.set_title('Top 10 languages', fontsize=15, color='#666666')

tweets_by_lang[:10].plot(ax=ax, kind='bar', color='#FF7A00')

for spine in ax.spines.values():
        spine.set_edgecolor('#666666')


plt.show()