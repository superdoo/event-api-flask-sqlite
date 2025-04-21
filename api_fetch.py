import requests
import sqlite3

# Replace with your NewsAPI key
API_KEY = "5c2365bdab8e44469fb3838905063123"
URL = "https://newsapi.org/v2/top-headlines"

def fetch_data():
    params = {
        "country": "us",  # You can change this to other countries as well
        "apiKey": API_KEY
    }
    response = requests.get(URL, params=params)
    data = response.json()

    # Store the fetched news articles in SQLite database
    conn = sqlite3.connect('news_data.db')
    c = conn.cursor()
    for article in data["articles"]:
        c.execute('''
            INSERT INTO news_articles (title, description, url) 
            VALUES (?, ?, ?)
        ''', (article['title'], article['description'], article['url']))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    fetch_data()
