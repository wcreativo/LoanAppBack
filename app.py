from flask import Flask
from flask_cors import CORS

from api.route.loan import loan_api

app = Flask(__name__)
CORS(app)

app.register_blueprint(loan_api, url_prefix="/loan")
