# Database code for the DB Forum.

import psycopg2

DATABASE_NAME = "forum"

def get_posts():
    """Return all posts from the 'database', most recent first."""
    db = psycopg2.connect(database=DATABASE_NAME, user="postgres", 
                          password="postgres")
    c = db.cursor()
    c.execute("SELECT content, time, id FROM posts ORDER BY time DESC")
    posts = c.fetchall()
    db.close()
    
    return posts


def add_post(content):
    """Add a post to the 'database' with the current timestamp."""
    db = psycopg2.connect(database=DATABASE_NAME, user="postgres", 
                          password="postgres")
    c = db.cursor()
    c.execute("INSERT INTO posts VALUES (%s)", (content,))
    db.commit()
    db.close()