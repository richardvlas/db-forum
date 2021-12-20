# Flask & PostgreSQL database forum
## Overview
A simple webapp to demonstrate how to connect PostgreSQL database with Flask webapp. The webapp allows to write a post and save it in a database in order to fetch and display all posts on a front-end page.

## Create a new database
Forum posts and other related data are stored in a PostgreSQL database named `forum`. PostgreSQL installation comes with a number of useful command line tools that we can use when building web apps with Postgres.

**Log in as a particular user**

First we log as the default installed user called `postgres`

```sql
sudo -u postgres -i
```

We will make a use of a command-line tool called `psql` to create the database. `psql` is an interactive terminal application for connecting and interacting with your local postgres server on your machine. With `psql` you can 
- Connect to your database using `$ psql <dbname>` 
- Directly type and execute SQL commands to your database
- Inspect and preview your database and database tables using psql meta-commands

**TODO:** The steps to initialize the database are shown below:



The database contains one table called `posts` with 3 columns 
- `content` represents the text of the post, 
- `time` is the time stamp when the post was created and 
- `id` is a unique identifier of a post. To create this new table type the following query:

```sql
CREATE TABLE posts ( content TEXT,
                     time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                     id SERIAL );
```                  
                     
