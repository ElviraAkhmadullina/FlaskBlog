"""Script to seed database"""

import os #module from Python's library, code related to working with your computer's operating system
import json
from random import choice, randint
from datetime import datetime


import models
import server

os.system('dropdb rooms')
os.system('createdb rooms')

models.connect_to_db(server.app)
models.db.create_all()

#Create 10 users
for n in range(10):
    username = f'user{n}'
    email = f'user{n}@test.com'  #unique email
    password = f'test{n}'

    user = models.User(username=username, email=email, password=password)
    models.db.session.add(user)
    models.db.session.commit()

# Create rooms, store them in list so we can use them
# to create fake posts, likes and comments later
posts_in_db = []
posts = ["living room", "bedroom", "kitchen", "patio", "home office"]

db_room = models.Post(title='test', date_posted=datetime.now(), content='test test test',
                        user_id=1)
models.db.session.add(db_room)
models.db.session.commit()     
posts_in_db.append(db_room)

