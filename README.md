# #MetaFood
Semantic web application enabled by a knowledge graph


## Version 1: based data collection



## Version 2: API-based data collection
In general, the idea is to have per data source a list of about 25 restaurants. For each restaurant, maybe get 3-4 meals from the menu? (I guess this should be manageable, depending on how much cleanup all this needs).

Quote from assignment:
"The size of the data is not of major importance, but it should contain around hundred relevant entities (i.e., data instances) for your domain"

So, I guess with 4 sources, each with 25 restaurants, we fulfill that.

I guess that we should try to cover a range of different cuisines, from the idea of our application, i.e. italian, mexican, indian, burger/american, korean, chinese food, something like this?


## Data Cleaning, Pre-processing


## Common Data Structures for Collected Data
There is a file that should hold common definitions to be used for organizing the raw data:
`common_definitions.py`

It holds e.g. a definition of suitable column names for a pandas dataframe; here, the columns define the attributes we think are useful / necessary for our tasks. 

E.g. use like this:
`from common_definitions import columns_restaurants, columns_menu`
and then use these columns for creating our pandas dataframe, like so:
`restaurants_df = pd.DataFrame(columns=columns_restaurants)`.
This creates an empty data frame whose columns can then be filled, e.g. by directly assigning a list of appropriate length, for each resepctive column, etc.




## Existing Ontologies and Vocabularies
The assignment says that we should " [...] make sure to reuse existingvocabularies wherever fitting and possible".
They suggest the following ontologies/vocabularies as starting points (see assignment):
* http://lov.okfn.org/
* http://www.w3.org/wiki/Ontology_repositories

Additional existing vocabularies that seem to make a lot of sense:

### Food
* BBC food ontology [looks promising] https://www.bbc.co.uk/ontologies/fo
* Food ontology catalog: http://lov4iot.appspot.com/?p=lov4iot-food
* [Maybe this one? Not yet checked!]  https://github.com/ailabitmo/food-ontology

### Delivery Services
* [check as starting point]  https://lov.linkeddata.es/dataset/lov/terms?q=+delivery

### Address Ontology
* This ontology has all vocabolaries related to location that we needed in our project. Like (street, city, country, postcode, latitude, longitude, phone).
* Hier is a decription of it: http://ontology.eil.utoronto.ca/icontact.html#d4e383
* Hier is the IRI to import it in protege for example: http://ontology.eil.utoronto.ca/icontact.owl

### Good Relation Ontology
* THis ontology has been created for shop application. We can find different vocabolaries we need like (delivery methodes, delivery charge, payment methods, price, location).
* I used webvowl to get a fast overwie of this ontology.
* Hier you can find more information about it: http://www.heppnetz.de/ontologies/goodrelations/v1.html
* Hier is the ontology IRI: http://purl.org/goodrelations/v1





## Final Report Overleaf:

https://www.overleaf.com/8736587956jvnmqwsjzpqf





