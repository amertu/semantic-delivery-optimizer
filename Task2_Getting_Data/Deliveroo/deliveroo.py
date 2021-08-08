import json
import re

import requests
from parsel import Selector
from collections import namedtuple


HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
}

Restaurant = namedtuple(
    "Restaurant",
    [
        "name",
        "cuisine",
        "description",
        "price_category",
        "breakfast",
        "lunch",
        "sandwiches",
        "city",
        "post_code",
        "street",
        "number",
        "number_addon",
        "phone",
        "url",
        "latitude",
        "longitude",
        "delivery_charge",
        "min_order",
        "payment_cash",
        "payment_card",
        "waiting_time",
        "delivery_time",
        "delivery_postcode",
        "rating_value",
        "rating_count",
        "data_source",
    ],
)
Restaurant.__new__.__defaults__ = (None,) * len(Restaurant._fields)
Menu = namedtuple("Menu", ["name", "restaurant_name", "description", "price"])


def get_restaurants():
    params = (("postcode", "SW9 9TN"),)
    response = requests.get(
        "https://deliveroo.co.uk/restaurants/london/stockwell",
        headers=HEADERS,
        params=params,
    )
    sel = Selector(text=response.text)
    links = sel.css("ul[class^='HomeFeedGrid'] a::attr('href')").extract()

    restaurant_links = set()
    for link in links:
        link = "https://deliveroo.co.uk" + link
        restaurant_links.add(link)
        # restaurants.add("https://deliveroo.co.uk" + re.sub(r"\?.*", "", link))

    restaurants = []
    for i, link in enumerate(list(restaurant_links)):
        print("Parsing {}: {}".format(i, link))
        restaurants.append(get_restaurant(link))

    return restaurants


def get_restaurant(restaurant_link):
    response = requests.get(restaurant_link, headers=HEADERS)
    sel = Selector(text=response.text)

    #address, city, post_code = sel.css(".address ::text").extract_first().split(", ")
    #number, street = address.split(address, 1)

    res_data = json.loads(
        sel.css('script[type="application/json"] ::text').extract()[1]
    )

    restaurant_data = res_data["restaurant"]
    number, street = restaurant_data["street_address"].split(" ", 1)
    restaurant = Restaurant(
        name=restaurant_data["name"],
        cuisine=[t["name"] for t in restaurant_data["menu"]["menu_tags"]],
        description=restaurant_data["description"],
        price_category=None,
        breakfast=None,
        lunch=None,
        sandwiches=None,
        city=restaurant_data["city"],
        post_code=restaurant_data["post_code"],
        street=street,
        number=number,
        number_addon=None,
        phone=restaurant_data["phone_numbers"]["primary"],
        url=restaurant_link,
        latitude=None,
        longitude=None,
        delivery_charge=None,
        min_order=None,
        payment_cash=None,
        payment_card=None,
        waiting_time=None,
        delivery_time=None,
        delivery_postcode=None,
        rating_value=None,
        rating_count=None,
        data_source=None,
    )

    menu = []
    menu_data = res_data["menu"]
    for item in menu_data["items"]:
        menu.append(
            Menu(
                name=item["name"],
                restaurant_name=restaurant.name,
                description=item["description"],
                price=item["raw_price"],
            )._asdict()
        )

    return (restaurant._asdict(), menu)


restaurants = get_restaurants()

with open("deliveroo.json", "w") as f:
    json.dump(restaurants, f)
