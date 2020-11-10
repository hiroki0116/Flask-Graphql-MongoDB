# Frask-Graphql-MongoDB/app.py
from database import init_db
from flask import Flask
from flask_graphql import GraphQLView
from schema import schema
from models import Ranking
from scraping import scraping



app = Flask(__name__)
app.debug = True

# You can copy following quary and paste it in GraphiQL(5000/graphql)
'''
{ 
   allRankings{
    edges{
      node {
        no
        title
        artist
        img
      }
    }
  }
}
'''

#Redirect to Graphql IDE (ex. http://127.0.0.1:5000/graphql)
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)

if __name__ == '__main__':
    scraping()
    init_db()
    app.run()
