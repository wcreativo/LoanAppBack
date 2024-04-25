from flask import Flask

from api.route.loan import loan_api

app = Flask(__name__)

app.register_blueprint(loan_api, url_prefix="/loan")
