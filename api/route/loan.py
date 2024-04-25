from flask import Blueprint, jsonify, request
from flask_pydantic import validate

from api.schema.loan import LoanBody
from api.service.loan import validate_requested_amount

loan_api = Blueprint("api", __name__)


@loan_api.route("/", methods=["POST"])
@validate(body=LoanBody)
def validate_loan():
    data = request.get_json()
    response = validate_requested_amount(data["amount"])
    return jsonify({"message": response})
