from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_news_from_db():
    conn = sqlite3.connect('news_data.db')
    c = conn.cursor()
    c.execute('SELECT * FROM news_articles')
    rows = c.fetchall()
    conn.close()
    return rows

@app.route('/')
def home():
    news = get_news_from_db()
    return render_template('index.html', news=news)

if __name__ == '__main__':
    app.run(debug=True)
