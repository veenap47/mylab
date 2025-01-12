import re
import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS
import emoji
import itertools 
from collections import Counter
import warnings
import regex

#%matplotlib inline
warnings.filterwarnings('ignore')
def date_time(s):
    #pattern = '^\[([0-9]+)(\/)([0-9]+)(\/)([0-9]+), ([0-9]+):([0-9]+)[ ]?(AM|PM|am|pm)\]'
    pattern = r'^\[?(\d{1,2})\/(\d{1,2})\/(\d{2,4}), (\d{1,2}):(\d{2})[ ]?(AM|PM|am|pm)?\]?'
    result = regex.match(pattern, s)
    if result:
        return True
    return False

def find_author(s):
    parts = s.split(":",1) #split with maxsplit = 1, splits only on the first occurrence of ":"
    return len(parts) == 2

def split_data(line):
    # remove [ from the line   
    line = line.strip("[")
    #line = [02/04/23, 9:17:20 PM] John: Hello everyone!
    
    # split based on ]
    splitline = line.split("]")
    # splitline[0] = 02/04/23, 9:17:20 PM
    # splitline[1] = John: Hello everyone!
    
    # Get time and date 
    time_stamp = splitline[0]
    time_stamp = time_stamp.split(",")
    date = time_stamp[0]
    time = time_stamp[1].strip()

    #date, time = time_stamp.split(",")

    # Get author and message
    message = splitline[1].strip()

    if find_author(message):
        split_message = message.split(":",1)
        author = split_message[0]
        message = split_message[1].strip()
    else:
        author = None
        
    return date, time, author, message


data = []
#chat = '/Users/veenap47/Downloads/wayfarer_chat.txt' -- to be removed
chat = 'data/whatsapp_chat.txt'

#Clean unicode characters
def clean_text(text):
    return text.replace('\u202f', ' ')\
               .replace('\u200e', '')\
               .replace('\u200f', '')\
               .replace('\u200b', '')

# Skip system messages
def should_skip_line(line):
    skip_messages = [
        "You created this group",
        "Messages and calls are end-to-end encrypted",
        "You added",
        "You removed",
        "You started a call"
    ]
    return any(msg in line for msg in skip_messages) #

with open(chat, 'r',encoding='utf-8') as file:
    date, time, author, message = None, None, None, None
    while True:
        raw_line = file.readline()
        line = clean_text(raw_line)
        if should_skip_line(line):
            continue
        if not line:
            break
        line = line.strip()
        
        if date_time(line):
            date, time, author,message = split_data(line)
            data.append([date, time, author, message])
            
#print(data)
'''from pprint import pprint
pprint(data)'''

df = pd.DataFrame(data, columns=["Date", 'Time', 'Author', 'Message'])
df['Date'] = pd.to_datetime(df['Date'])
#print(df.tail(20)) 
#print(df.info())
#print(df.Author.unique())

summary = df.groupby('Date').agg({
    'Message': 'count'  # Count messages per date
}).reset_index()

# Rename column
summary.columns = ['Date', 'Message_Count']

# Sort by date
summary = summary.sort_values('Date')

# Numberof messages over time - line plot
# Create the plot
plt.figure(figsize=(12, 6))
plt.plot(summary['Date'], summary['Message_Count'])

# Customize the plot
plt.title('Number of Messages Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Messages')
plt.grid(True)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Adjust layout to prevent label cutoff
plt.tight_layout()

plt.show()

top10days = summary.sort_values('Message_Count', ascending=False).head(10)
print(top10days)

# Most active days
sns.set_style("darkgrid")
plt.figure(figsize=(12, 6))

# A bar plot for top 10 days
sns.barplot(data = top10days, x = top10days.Date, y = top10days.Message_Count, palette="hls");




# Most common words in chat
text = ' '.join(df['Message'].astype(str))

# Create and generate a word cloud image
wordcloud = WordCloud(width=800, height=400,
                     background_color='white').generate(text)

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Most Common Words in Chat')
plt.show()


# Top 5 most active members
# Count messages per author
author_msgs = df['Author'].value_counts()

# Create plot
plt.figure(figsize=(12, 6))
sns.barplot(x=author_msgs.values, y=author_msgs.index)

# Customize
plt.title('Most Active Members in Group')
plt.xlabel('Number of Messages')
plt.ylabel('Author')

plt.tight_layout()
plt.show()

# Print statistics
print("\nTop 5 Most Active Members:")
print(author_msgs.head())