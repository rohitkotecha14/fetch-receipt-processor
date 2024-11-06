import re
from datetime import datetime
from typing import List
from pydantic import BaseModel, Field, field_validator


class Item(BaseModel):
    shortDescription: str = Field(..., description='The Short Product Description for the item')
    price: str = Field(..., description='The total price paid for this item')

    @field_validator('shortDescription')
    def validate_shortDescription(cls, value):
        if not re.match(r"^[\w\s\-]+$", value):
            raise ValueError('shortDescription must contain only letters and numbers, spaces or hyphens')

        return value

    @field_validator('price')
    def validate_price(cls, value):
        if not re.match(r"^\d+\.\d{2}$", value):
            raise ValueError('price must be a numeric string with 2 decimal places')

        return value



class ReceiptSchema(BaseModel):
    retailer: str = Field(..., description='The name of the retailer or store the receipt is from')
    purchaseDate: str = Field(..., description='The date of purchase printed on the receipt')
    purchaseTime: str = Field(..., description='The time of purchase printed on the receipt. 24-hour time expected')
    total: str = Field(..., description='The total amount paid on the receipt')
    items: List[Item] = Field(..., min_length=1,description='The list of items paid on the receipt')

    @field_validator("purchaseDate")
    def validate_purchase_date(cls, value):
        try:
            datetime.strptime(value, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Purchase Date must be in the format of YYYY-MM-DD")

        return value

    @field_validator("purchaseTime")
    def validate_purchase_time(cls, value):
        try:
            time_obj = datetime.strptime(value, "%H:%M")
            if time_obj.strftime("%H:%M") != value:
                raise ValueError
        except ValueError:
            raise ValueError("purchaseTime must be in the format of HH:MM (24-hour time expected)")

        return value

    @field_validator("total")
    def validate_total_format(cls, value):
        if not isinstance(value, str) or not value.replace('.', '', 1).isdigit() or '.' not in value:
            raise ValueError("Total must be a numeric string with two decimal places")
        if len(value.split('.')[-1]) != 2:
            raise ValueError("Total must be a numeric string with two decimal places")

        return value
