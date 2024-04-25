from pydantic import BaseModel


class LoanBody(BaseModel):
    tax_id: str
    amount: int
    business_name: str
