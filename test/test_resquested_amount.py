from api.service.loan import validate_requested_amount


class TestRequestAmount:

    def test_approved_loan(self):
        result = validate_requested_amount(5000)
        assert result == "Approved"

    def test_declined_loan(self):
        result = validate_requested_amount(500000)
        assert result == "Declined"

    def test_undecided_loan(self):
        result = validate_requested_amount(50000)
        assert result == "Undecided"
