#import the class that describes each vectorized post
from PostVectorized import *

#connection to the database to retrieve the posts
import matplotlib.pyplot as plt
import json
import psycopg2
import pandas as pd

con = psycopg2.connect(
database="FB",
user="user",
password="password",
host="localhost",
port= '5432'
)

cursor_obj = con.cursor()

cursor_obj.execute('''SELECT * FROM post''')
posts = cursor_obj.fetchall()

#connection to the new database
connection = psycopg2.connect(
database="FB_vectors",
user="user",
password="password",
host="localhost",
port= '5432'
)

connection.autocommit = True

cursor_obj = connection.cursor()

#creating the new table where the posts will be saved as groups of vectors
query = '''CREATE TABLE post_vector (
post_id CHAR(20) PRIMARY KEY, 
reaction_vector INTEGER ARRAY[6], 
vaderSentimentVector FLOAT ARRAY[4], 
basicInfoVector INTEGER ARRAY[5],
posVector INTEGER ARRAY[7],
nerVector INTEGER ARRAY[7],
textLengthsVector INTEGER ARRAY[7],
label BOOL
)
'''

cursor_obj.execute(query)
connection.commit()

#insert in the database the "new" posts, now as a group of vectors (feature sets)
print('start')
for post in posts:
    try:
        post_vector = postVectorized(post[0], vectorizingReactions(post), vectorizingVaderSentiment(post), vectorizingBasicInfo(post), vectorizingPOS(post), vectorizingNER(post), vectorizingTextLengths(post), post[2])
        print(post[0])
        cursor_obj.execute('INSERT INTO post_vector VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', (post_vector.id, post_vector.reactions, post_vector.vaderSentiment, post_vector.basicInfo, post_vector.POS, post_vector.NER, post_vector.textLengths, post_vector.label))
    except Exception:
        continue
connection.commit()
print('done')
