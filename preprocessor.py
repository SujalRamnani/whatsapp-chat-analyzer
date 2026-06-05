import re
import pandas as pd


def preprocess(data):

    # WhatsApp date pattern
    pattern = r'\d{1,2}/\d{1,2}/\d{2},\s\d{1,2}:\d{2}.*?[ap]m\s-\s'

    # Extract messages and dates
    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)

    # Create DataFrame
    df = pd.DataFrame({
        'user_message': messages,
        'message_date': dates
    })

    # Remove weird WhatsApp unicode space
    df['message_date'] = df['message_date'].str.replace('\u202f', ' ', regex=False)

    # Convert to datetime
    df['message_date'] = pd.to_datetime(
        df['message_date'],
        format='%d/%m/%y, %I:%M %p - '
    )

    # Separate users and messages
    users = []
    messages = []

    for message in df['user_message']:

        entry = re.split(r'([\w\W]+?):\s', message)

        if entry[1:]:
            users.append(entry[1])
            messages.append(entry[2])

        else:
            users.append('group_notification')
            messages.append(entry[0])

    df['user'] = users
    df['message'] = messages

    df.drop(columns=['user_message'], inplace=True)

    # Date Features
    df['year'] = df['message_date'].dt.year
    df['month'] = df['message_date'].dt.month
    df['month_name'] = df['message_date'].dt.month_name()
    df['day'] = df['message_date'].dt.day
    df['day_name'] = df['message_date'].dt.day_name()
    df['hour'] = df['message_date'].dt.hour
    df['minute'] = df['message_date'].dt.minute

    # Date only
    df['date'] = df['message_date'].dt.date

    # Period column for heatmap
    period = []

    for hour in df[['day_name', 'hour']]['hour']:

        if hour == 23:
            period.append(str(hour) + "-" + str('00'))

        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))

        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df['period'] = period

    return df