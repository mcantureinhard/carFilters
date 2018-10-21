from flask import Flask

app = Flask(__name__)

from app import Rest
app.register_blueprint(Rest.rest_api, url_prefix='/rest')

