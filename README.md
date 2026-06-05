# 📊 WhatsApp Chat Analyzer

A powerful WhatsApp Chat Analysis Web App built using **Python**, **Streamlit**, **Pandas**, **Matplotlib**, **Seaborn**, and **Natural Language Processing (NLP)** techniques.

The application allows users to upload exported WhatsApp chat files and generate detailed insights, statistics, visualizations, and user activity reports. Inspired by modern data analytics dashboards and WhatsApp chat mining projects.

## 🚀 Live Demo

**Web App:** https://whatsapp-chat-analyzer-3dfe3yus9voe4cbc82qvrg.streamlit.app/

---

## ✨ Features

### 📈 Chat Statistics

* Total Messages
* Total Words
* Media Shared
* Links Shared

### 👥 User Analysis

* Most Active Users
* User-wise Statistics
* User Contribution Percentage

### ☁️ Text Analysis

* Word Cloud Generation
* Most Common Words
* Hinglish Stop Words Filtering

### 😂 Emoji Analysis

* Most Used Emojis
* Emoji Frequency Distribution
* Emoji Pie Chart Visualization

### 📅 Timeline Analysis

* Monthly Timeline
* Daily Timeline
* Most Active Day
* Most Active Month

### 🔥 Activity Analysis

* Weekly Activity Heatmap
* Hourly Activity Analysis
* Peak Chatting Hours

### 📸 Media & Links Analysis

* Media King Detection
* Link Spammer Detection
* URL Extraction

### 🤖 Sentiment Analysis

* Positive Messages
* Negative Messages
* Neutral Messages
* Sentiment Distribution Visualization

### 📝 Additional Insights

* Longest Message Detection
* Average Chat Activity
* User Behavior Analysis

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### Data Processing

* Pandas
* Regular Expressions (Regex)

### Data Visualization

* Matplotlib
* Seaborn

### NLP & Text Analysis

* WordCloud
* URLExtract
* TextBlob

---

## 📂 Project Structure

```bash
whatsapp-chat-analyzer/
│
├── app.py
├── helper.py
├── preprocessor.py
├── stop_hinglish.txt
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/SujalRamnani/whatsapp-chat-analyzer.git

cd whatsapp-chat-analyzer
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 📤 How To Use

### Step 1

Open WhatsApp.

### Step 2

Export a chat without media.

```text
Chat → More → Export Chat → Without Media
```

### Step 3

Upload the exported `.txt` file into the application.

### Step 4

Select:

* Overall Analysis
* Individual User Analysis

### Step 5

Explore insights and visualizations.

---

## 📊 Sample Insights

* Most Active User
* Peak Chatting Time
* Most Common Words
* Emoji Usage Patterns
* Monthly Activity Trends
* Sentiment Distribution
* Media Sharing Statistics

---

## 🎯 Future Improvements

* AI-Powered Chat Summarization
* Topic Modeling
* Relationship Network Graphs
---

## 👨‍💻 Author

**Sujal Ramnani**


GitHub: https://github.com/SujalRamnani

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
