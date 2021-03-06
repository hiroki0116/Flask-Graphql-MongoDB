# Frask-Graphql-MongoDB/database.py
import json
from mongoengine import connect
import os
from models import Ranking


#Using free cluster of Mongodb Atlas
DB_URI = "mongodb+srv://db_hseino:Everythingis6@cluster0.upiob.mongodb.net/db_hseino?retryWrites=true&w=majority"
connection = connect(host=DB_URI)
db = connection.list_database_names()
connection.drop_database("db_hseino") #Drop database first everytime run this program

def init_db():

    #loading json data that fetched the song data[title,artist,cover image] by scraping
    with open("ranking.json", "r") as file:
        data = json.loads(file.read())

    rankings = []
    for row in data:
        ranking = Ranking(no = row["no"],title = row["title"], artist = row["artist"], img = row["img"])
        ranking.save()
        rankings.append(ranking)
        
        
