# WhatsApp Chat Analysis with Python

This repository contains a Python script for analyzing and visualizing WhatsApp chat data. By parsing raw chat exports, the script provides insights into message trends, most active members, and frequently discussed topics.

---

## Features

- Parse and structure WhatsApp chat data into a DataFrame
- Analyze message trends over time
- Identify the most active members in the chat
- Generate word clouds to visualize commonly used words
- Visualize top activity days using bar charts
- Perform exploratory data analysis (EDA) on group chats

---

## Prerequisites

To run this project, ensure you have the following installed:

- Python 3.x
- Libraries: 
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `seaborn`
  - `wordcloud`
  - `regex`

Install the dependencies using pip:

```bash
pip install pandas numpy matplotlib seaborn wordcloud regex
```

---

## How to Use

1. **Export WhatsApp Chat**: Export the chat from WhatsApp (text format).
2. **Place Chat File**: Save the chat file (e.g., `whatsapp_chat.txt`) in the `data/` folder.
3. **Run the Script**:

   ```bash
   python chat_analysis.py
   ```

4. **View Outputs**:
   - Line plot showing the number of messages over time
   - Bar chart for the most active days
   - Word cloud for the most common words
   - Bar chart of the most active members

---

## Code Overview

### 1. **Preprocessing the Chat Data**

- **Date and Time Parsing**: Identify lines with timestamps to mark the start of a new message.
- **Message Segmentation**: Extract the date, time, author, and message content.
- **Text Cleaning**: Remove unwanted Unicode characters and filter out system messages.

### 2. **Data Transformation**

- Convert parsed data into a Pandas DataFrame with columns: `Date`, `Time`, `Author`, `Message`.
- Group data by date for trend analysis.

### 3. **Visualizations**

- **Messages Over Time**: Line plot showing daily message counts.
- **Most Active Days**: Bar chart highlighting top 10 activity days.
- **Word Cloud**: Visualize common words in the chat.
- **Top Contributors**: Bar chart of message counts per user.

---

## Example Visualizations

### Number of Messages Over Time

```python
plt.plot(summary['Date'], summary['Message_Count'])
plt.title('Number of Messages Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Messages')
plt.grid(True)
plt.show()
```

### Word Cloud of Common Words

```python
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Most Common Words in Chat')
plt.show()
```

### Most Active Members

```python
author_msgs = df['Author'].value_counts()
sns.barplot(x=author_msgs.values, y=author_msgs.index)
plt.title('Most Active Members in Group')
plt.xlabel('Number of Messages')
plt.ylabel('Author')
plt.show()
```

---

## Key Insights

- **Message Trends**: Identify the most and least active days.
- **Content Analysis**: Highlight frequently used words and topics.
- **User Contribution**: Determine the most active participants in the group.

---

## Contributing

Feel free to fork this repository and contribute by submitting pull requests. Suggestions for improvements or new features are always welcome!


---


Happy Analyzing! 🚀
