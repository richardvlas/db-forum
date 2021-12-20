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

**Create a new database**

Now we can create a new database called `forum`. There are two ways to accomplish this either by using 

```sql
createdb forum
```

or alternativaly we can make a use of a command-line tool called `psql` to create the database, that also comes as part of the PostreSQL installation. `psql` is an interactive terminal application for connecting and interacting with your local postgres server on your machine. With `psql` you can 
- Connect to your database using `$ psql <dbname>` 
- Directly type and execute SQL commands to your database
- Inspect and preview your database and database tables using psql meta-commands

The following snippet shows how a database can be created. First we launch `psql` by simply typing:

```
psql
```

once logged in write a SQL query to create the database

```sql
CREATE DATABASE forum;
```

Now list the databases with the command `\l` to verify that the new `forum` database was created

```
                              List of databases
   Name    |  Owner   | Encoding | Collate |  Ctype  |   Access privileges
-----------+----------+----------+---------+---------+-----------------------
 forum     | postgres | UTF8     | C.UTF-8 | C.UTF-8 |
(1 rows)
```

Connect to the database by typing

```
\c forum
```

The database should contain one table called `posts` with 3 columns 
- `content` represents the text of the post, 
- `time` is the time stamp when the post was created and 
- `id` is a unique identifier of a post. To create this new table type the following query:

The following SQL query acomplish this

```sql
CREATE TABLE posts ( content TEXT,
                     time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                     id SERIAL );
```                  

To verify that the table `posts` was created type `\dt` that shows all database tables

```
         List of relations
 Schema | Name  | Type  |  Owner
--------+-------+-------+----------
 public | posts | table | postgres
(1 row)
```

And finaly to show the table schema type

```
\d posts
```

that returns

```
 content | text                        |           |          |
 time    | timestamp without time zone |           |          | CURRENT_TIMESTAMP
 id      | integer                     |           | not null | nextval('posts_id_seq'::regclass)
```
