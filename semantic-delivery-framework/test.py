import requests
import urllib

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

r = requests.get(url="http://localhost:8080/rdf4j-server/repositories", headers={'Accept':'application/json'})
print(r.json())

r = requests.put('http://localhost:8080/rdf4j-server/repositories/semsys', data=repos,  headers={'Accept':'application/json', 'Content-Type':'text/rdf+n3'})
print(r)

BASIC_URL = "http://localhost:8080/rdf4j-server/repositories/semsys?name=&infer=true&sameAs=true&query="
PREFIX = urllib.quote_plus("PREFIX food: <http://metafood.org#>" + "PREFIX ic: <http://ontology.eil.utoronto.ca/icontact.owl#>" + "PREFIX gr: <http://purl.org/goodrelations/v1#>" + "PREFIX fo: <http://purl.org/ontology/fo/>" + "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>")
SELECT_BASIC = "select ?menuName ?restaurantName ?menuPrice ?isCashEnabled ?isCreditEnabled ?ratingValue where {";
query = "select ?product ?description where { ?r rdf:type fo:Menu .?r gr:legalName ?product .?r gr:description ?description .}"

url = BASIC_URL + PREFIX + urllib.quote_plus(query)
r = requests.get(url=url, headers={'Accept': 'application/json'})
print(r.json())
    
    
