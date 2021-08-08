#!/usr/bin/env python
"""
Define some common stuff that we need to work on together
"""

# IMPORTS GO HERE
# import pandas as pd
from collections import OrderedDict  # dictionary that remembers order of elements, as e.g. in list



# ----------------------------------------------------------------------------


# collect the most important attributes for restaurants
# The idea is to use this list of attribute names to directly use it as
# the `columns` argument when creating a pandas dataframe (see below)
# columns_restaurants = ['name',  # restaurant name
#                        'cuisine',  # such a s 'italian', 'bugers' , NOTE: should this be a list?
#                        'description',
#                        'price_category',  # such as '€', '€€', '€€€', mapped to 1, 2, 3, ...
#                        'breakfast',
#                        'lunch',
#                        'sandwiches',
#                        'city',
#                        'post_code',
#                        'street',
#                        'number',  # house number, like 56
#                        'number_addon',  # add on to house number, like 56/2 or 56-2
#                        'phone',
#                        'url',
#                        'latitude',
#                        'longitude',
#                        'delivery_charge',
#                        'min_order',  # min amount of order, in pounds
#                        'payment_cash',
#                        'payment_card',
#                        'waiting_time',  # how long after order is pickup [do we need this?]
#                        'delivery_time',  # typical delivery time to address
#                        'delivery_postcode',  # where delivery is possible to
#                        'rating_value',
#                        'rating_count',  # how many ratings?
#                        'data_source'  # such as 'uber eats', 'foodhub', etc.
#                        ]


restaurant_columns_types = [('name', 'str'),            # restaurant name
                            ('cuisine', 'str'),         # such a s 'italian', 'bugers' , NOTE: should this be a list?
                            ('description', 'str'),
                            ('price_category', 'str'),  # such as '€', '€€', '€€€', mapped to 1, 2, 3, ...
                            ('breakfast', 'str'),
                            ('lunch', 'str'),
                            ('sandwiches', 'str'),
                            ('city', 'str'),
                            ('post_code', 'str'),     # restaturants post code
                            ('street', 'str'),
                            ('number', 'int'),        # house number, like 56
                            ('number_addon', 'str'),  # add on to house number, like 56/2 or 56-2
                            ('phone', 'int'),
                            ('url', 'str'),
                            ('latitude', 'float'),    # let's assume this is in the "fraction format"
                            ('longitude', 'float'),
                            ('delivery_charge', 'float'),
                            ('min_order', 'float'),   # min amount of order, in pounds
                            ('payment_cash', 'str'),
                            ('payment_card', 'str'),
                            ('waiting_time', 'float'),    # how long after order is pickup [do we need this?]
                            ('delivery_time', 'float'),   # typical delivery time to address
                            ('delivery_postcode', 'str'), # where delivery is possible to
                            ('rating_value', 'float'),
                            ('rating_count', 'int'),      # how many ratings?
                            ('data_source', 'str')        # such as 'uber eats', 'foodhub', etc.
                            ]

restaurant_columns_types = OrderedDict(restaurant_columns_types)

columns_restaurants = list(restaurant_columns_types.keys())
types_restaurants = list(restaurant_columns_types.values())


# Here goes the more detailed explanation of the attribute names:
# * name: the restaurant name
# * cuisine: like 'italian', 'mexican', etc.
# * description: further description of offered food, etc.


# restaurants_df = pd.DataFrame(foo, columns=columns_restaurant)


# ----------------------------------------------------------------------------

columns_menu = ['name',  # name of the food, such as: Bacon-Burger
                'restaurant_name',  # for linking back to restaurant
                'description',  # str for description of food, such as ingredients on pizza, or side dishes, etc.
                'price'
                ]




