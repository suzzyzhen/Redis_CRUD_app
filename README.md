# Redis_CRUD_app

This application utilizes the Redis database to cache a Goodreads book dataset (available at https://www.kaggle.com/jealousleopard/goodreadsbooks) and performs CRUD (Create, Read, Update, and Delete) operations on the database through a Flask application interface. 

Note: application can only be used in local environment 

## Dataset: 

Total 11,127 records of books
Columns include: bookID, title, authors, average_rating, isbn, isbn13, language_code, num_pages, ratings_count, text_reviews_count, publication_date, publisher

## Methology: 

1. transform the csv dataset(books.csv) into a JSON format (books2.json) 

2. store the JSON file into Redis database with ReJSON API 

INFO: https://redislabs.com/blog/redis-as-a-json-store/

Module installation: https://github.com/RedisJSON/RedisJSON

3. run 'rejsontest.py' to cache the database in Redis 

in Redis-cli, data can be retrived with bookID as follows:

<img width="876" alt="Screen Shot 2021-01-13 at 3 27 58 PM" src="https://user-images.githubusercontent.com/60942661/104506877-f7cf5880-55b3-11eb-9f8f-54e06163bf4d.png">


4. Launch Flask app with python app.py in terminal 


![Screen Shot 2021-01-13 at 5 39 31 PM](https://user-images.githubusercontent.com/60942661/104518914-88169900-55c6-11eb-9f05-2c27639c6b55.png)


## Operations: 
1. Read books from database: 

![Screen Shot 2021-01-13 at 6 12 06 PM](https://user-images.githubusercontent.com/60942661/104521582-2278db80-55cb-11eb-968a-9353ba46cc99.png)

2. Create books into the database: 
![Screen Shot 2021-01-13 at 6 16 50 PM](https://user-images.githubusercontent.com/60942661/104521884-cbbfd180-55cb-11eb-9c67-78027dfee94b.png)

3. Update
