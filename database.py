import sqlite3

conn = sqlite3.connect('news_data.db')
c = conn.cursor()

# Recreate table
c.execute('''DROP TABLE IF EXISTS news_articles''')
c.execute('''
    CREATE TABLE news_articles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        description TEXT,
        author TEXT,
        source_name TEXT,
        published_at TEXT,
        url TEXT,
        image_url TEXT
    )
''')

conn.commit()
conn.close()

print("Database schema reset. Now run: python api_fetch.py")
