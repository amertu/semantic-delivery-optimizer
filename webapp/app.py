from flask import Flask
from endpoints.ui.index_page import index_page
from endpoints.api.search_api import search_api
import requests

repos = """
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
@prefix rep: <http://www.openrdf.org/config/repository#>.
@prefix sr: <http://www.openrdf.org/config/repository/sail#>.
@prefix sail: <http://www.openrdf.org/config/sail#>.
@prefix ms: <http://www.openrdf.org/config/sail/memory#>.

[] a rep:Repository ;
   rep:repositoryID "semsys" ;
   rdfs:label "test memory store" ;
   rep:repositoryImpl [
      rep:repositoryType "openrdf:SailRepository" ;
      sr:sailImpl [
         sail:sailType "openrdf:MemoryStore" ;
         ms:persist true ;
         ms:syncDelay 120
      ]
   ].
"""

app = Flask(__name__)

@app.before_first_request
def activate_job():
    r = requests.get(url="http://database:8080/rdf4j-server/repositories", headers={'Accept':'application/json'})
    app.logger.info(r)
    r = requests.put('http://database:8080/rdf4j-server/repositories/semsys', data=repos,  headers={'Accept':'application/json', 'Content-Type':'text/rdf+n3'})
    headers = headers = {'Content-Type': 'text/turtle'}
    app.logger.info(r)
    r = requests.post('http://database:8080/rdf4j-server/repositories/semsys/statements', data=open('./foodHub_KG.ttl', 'rb'), headers=headers)
    app.logger.info(r) 


app.register_blueprint(index_page, url_prefix='/')
app.register_blueprint(search_api, url_prefix='/api')




if __name__ == '__main__':
    app.run()

