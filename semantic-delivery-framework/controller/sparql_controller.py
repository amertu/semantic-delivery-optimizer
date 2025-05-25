import requests
import urllib.parse

BASIC_URL = "http://database:8080/rdf4j-server/repositories/semsys?name=&infer=true&sameAs=true&query="

PREFIX = urllib.parse.quote_plus("PREFIX food: <http://metafood.org#>" + "PREFIX ic: <http://ontology.eil.utoronto.ca/icontact.owl#>" + "PREFIX gr: <http://purl.org/goodrelations/v1#>" + "PREFIX fo: <http://purl.org/ontology/fo/>" + "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>")

SELECT_BASIC = "select ?menuName ?restaurantName ?menuPrice ?isCashEnabled ?isCreditEnabled ?ratingValue where {";


def get_all_products():
    query = "select ?product ?description where { ?r rdf:type fo:Menu .?r gr:legalName ?product .?r gr:description ?description .}"
    url = BASIC_URL + PREFIX + urllib.parse.quote_plus(query)
    try:
        r = requests.get(url=url, headers={'Accept': 'application/json'})
        return r.json()
    except Exception:
        return "{}"


def _construct_filter(state: dict):
    query_filter = ""
    if not state["allProducts"]:
        menu_filter = []
        for product in state["products"]:
            for p in product.split():
                menu_filter.append(p)

        query_filter = "FILTER("
        i = 0
        for product in menu_filter:
            query_filter += ("REGEX(?menuName,\"" + product + "\")")
            if i < (len(menu_filter) - 1):
                query_filter += "||"
            i = i + 1
        query_filter += ")"

    if not state["cashEnabled"]:
        query_filter += "FILTER(REGEX(?isCreditEnabled, \"YES\"))"
    if not state["cardEnabled"]:
        query_filter += "FILTER(REGEX(?isCashEnabled, \"ENABLED\"))"
    return query_filter


def _construct_ordering(state: dict) -> str:
    if state["ordering"] == "price":
        return "} ORDER BY ASC (?menuPrice)"
    else:
        return "} ORDER BY DESC (?ratingValue)"


def _construct_query(state: dict):
    BODY = SELECT_BASIC + \
        "?r gr:legalName ?restaurantName." + \
        "?r food:hasRating ?rating." + \
        "?rating a food:Rating ;" + \
        "food:hasRatingValue ?ratingValue ." + \
        "?r food:acceptedPaymentCashMethod ?cashMethod." + \
        "?cashMethod a food:PaymentMethodCash ;" + \
        "food:cashIsEnabled ?isCashEnabled ." + \
        "?r food:acceptedPaymentCreditMethod ?creditMethod." + \
        "?creditMethod a gr:PaymentMethodCreditCard ;" + \
        "food:creditIsEnabled ?isCreditEnabled ." + \
        "?r gr:offers ?menu." + \
        "?menu a fo:Menu ;" + \
        "gr:legalName ?menuName ;" + \
        "food:hasPrice ?menuPrice ;"

    query_filter = _construct_filter(state)
    query_ordering = _construct_ordering(state)

    return BASIC_URL + PREFIX + urllib.parse.quote_plus(BODY + query_filter + query_ordering)


def get_all_restaurants(filter: dict):
    query = _construct_query(filter)
    r = requests.get(url=query, headers={'Accept': 'application/json'})
    return r.json()
