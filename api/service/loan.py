def validate_requested_amount(requested_amount: int):

    if int(requested_amount) > 50000:
        return "Declined"
    if int(requested_amount) == 50000:
        return "Undecided"
    if int(requested_amount) < 50000:
        return "Approved"
