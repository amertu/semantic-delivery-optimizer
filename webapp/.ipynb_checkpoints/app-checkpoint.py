from flask import Flask
from endpoints.ui.index_page import index_page
from endpoints.api.search_api import search_api

app = Flask(__name__)


app.register_blueprint(index_page, url_prefix='/')
app.register_blueprint(search_api, url_prefix='/api')

if __name__ == '__main__':
    app.run()
