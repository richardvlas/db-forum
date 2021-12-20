# Flask & PostgreSQL database forum
## Overview
A simple webapp to demonstrate how to connect PostgreSQL database with Flask webapp. The webapp allows to write a post and save it in a database in order to fetch and display all posts on a front-end page.

## Create a new database
Forum posts and other related data are stored in a PostgreSQL database named `forum`. The steps to initialize the database are shown below:

TODO: **add steps on how to create the database**

The database contains one table called `posts` with 3 columns 
- `content` represents the text of the post, 
- `time` is the time stamp when the post was created and 
- `id` is a unique identifier of a post. To create this new table type the following query:

```sql
CREATE TABLE posts ( content TEXT,
                     time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                     id SERIAL );
```                  
                     
