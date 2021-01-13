# Redis_CRUD_app

This application utilizes the Redis database to cache a Goodreads book dataset (available at https://www.kaggle.com/jealousleopard/goodreadsbooks) and performs CRUD (Create, Read, Update, and Delete) operations on the database through a Flask application interface. 

Note: application can only be used in local environment 

Dataset: 

Total 11,127 records of books
Columns include: bookID, title, authors, average_rating, isbn, isbn13, language_code, num_pages, ratings_count, text_reviews_count, publication_date, publisher

Methology: 

1. transform the csv dataset(books.csv) into a JSON format (books2.json) 

2. store the JSON file into Redis database with ReJSON API 

INFO: https://redislabs.com/blog/redis-as-a-json-store/

Module installation: https://github.com/RedisJSON/RedisJSON

3. run 'rejsontest.py' to cache the database in Redis 

in Redis-cli, data can be retrived with bookID as follows:

https://github.com/suzzyzhen/Redis_CRUD_app/issues/1#issue-785421058


4. Launch Flask app with python app.py in terminal 


