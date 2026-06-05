from urlextract import URLExtract
from wordcloud import WordCloud
from collections import Counter
import pandas as pd
import re
import emoji
from textblob import TextBlob


extract = URLExtract()



# Top Statistics


def fetch_stats(selected_user, df):

    if selected_user != "Overall":
        df = df[df['user'] == selected_user]

    # Total Messages
    num_messages = df.shape[0]

    # Total Words
    words = []

    for message in df['message']:
        words.extend(message.split())

    # Media Messages
    media_messages = df[
        df['message'] == '<Media omitted>\n'
    ].shape[0]

    # Links
    links = []

    for message in df['message']:
        links.extend(extract.find_urls(message))

    return num_messages, len(words), media_messages, len(links)



# Most Busy Users


def most_busy_users(df):

    x = df['user'].value_counts().head()

    new_df = round(
        (df['user'].value_counts() / df.shape[0]) * 100,
        2
    ).reset_index()

    new_df.columns = ['name', 'percent']

    return x, new_df



# WordCloud

def create_wordcloud(selected_user, df):

    f = open('stop_hinglish.txt', 'r', encoding='utf-8')
    stop_words = set(f.read().split())

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'group_notification']

    # Remove media messages
    temp = temp[temp['message'] != '<Media omitted>\n']

    # Remove deleted messages
    temp = temp[temp['message'] != 'This message was deleted\n']

    temp = temp.copy()

    def remove_stop_words(message):

        y = []

        for word in message.lower().split():

            if (
                word not in stop_words
                and 'http' not in word
                and 'www.' not in word
            ):
                y.append(word)

        return " ".join(y)

    temp['message'] = temp['message'].apply(remove_stop_words)

    wc = WordCloud(
        width=500,
        height=500,
        min_font_size=10,
        background_color='white'
    )

    df_wc = wc.generate(
        temp['message'].str.cat(sep=" ")
    )

    return df_wc



# Most Common Words


def most_common_words(selected_user, df):

    f = open('stop_hinglish.txt', 'r', encoding='utf-8')
    stop_words = set(f.read().split())

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'group_notification']

    # Remove media messages
    temp = temp[temp['message'] != '<Media omitted>\n']

    # Remove deleted messages
    temp = temp[temp['message'] != 'This message was deleted\n']

    words = []

    for message in temp['message']:

        for word in message.lower().split():

            # Remove punctuation
            word = re.sub(r'[^\w]', '', word)

            if (
                word
                and word not in stop_words
                and 'http' not in word
                and 'www' not in word
            ):
                words.append(word)

    most_common_df = pd.DataFrame(
        Counter(words).most_common(25)
    )

    return most_common_df


def emoji_helper(selected_user, df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    emojis = []

    for message in df['message']:
        for c in message:
            if c in emoji.EMOJI_DATA:
                emojis.append(c)

    emoji_df = pd.DataFrame(
        Counter(emojis).most_common(len(Counter(emojis)))
    )

    return emoji_df
def monthly_timeline(selected_user, df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    timeline = df.groupby(['year', 'month', 'month_name']).count()['message'].reset_index()

    time = []

    for i in range(timeline.shape[0]):
        time.append(
            timeline['month_name'][i] + "-" + str(timeline['year'][i])
        )

    timeline['time'] = time

    return timeline
def daily_timeline(selected_user, df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    daily_timeline = df.groupby('date').count()['message'].reset_index()

    return daily_timeline

def week_activity_map(selected_user, df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['day_name'].value_counts()
def month_activity_map(selected_user, df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['month_name'].value_counts()
def activity_heatmap(selected_user, df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    user_heatmap = df.pivot_table(
        index='day_name',
        columns='period',
        values='message',
        aggfunc='count'
    ).fillna(0)

    return user_heatmap
def busiest_hour(selected_user, df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['hour'].value_counts().sort_index()
def longest_message(selected_user, df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df.copy()

    temp['length'] = temp['message'].str.len()

    return temp.loc[temp['length'].idxmax()]
def media_king(df):

    media_df = df[
        df['message'] == '<Media omitted>\n'
    ]

    return media_df['user'].value_counts().head()
def link_spammer(df):

    users = {}

    for _, row in df.iterrows():

        links = extract.find_urls(row['message'])

        if len(links) > 0:

            users[row['user']] = users.get(
                row['user'],
                0
            ) + len(links)

    return pd.Series(users).sort_values(
        ascending=False
    ).head()
def sentiment_analysis(selected_user, df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    positive = 0
    negative = 0
    neutral = 0

    for msg in df['message']:

        score = TextBlob(msg).sentiment.polarity

        if score > 0:
            positive += 1

        elif score < 0:
            negative += 1

        else:
            neutral += 1

    return positive, negative, neutral

