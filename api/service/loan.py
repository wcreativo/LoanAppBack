def validate_requested_amount(requested_amount: int):

    if requested_amount > 50000:
        return "Declined"
    if requested_amount == 50000:
        return "Undecided"
    if requested_amount < 50000:
        return "Approved"
