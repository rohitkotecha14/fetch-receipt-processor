import math
from typing import List, Dict, Any


def retailer_name_points(retailer: str) -> int:
    #Checking if the retailer name contains only alphanumeric characters and returning the number of characters
    retailer_points = sum(1 for c in retailer if c.isalnum())

    print(f"Points based on retailer name: {retailer_points}")
    return retailer_points

def value_points(total: str) -> int:
    points = 0
    # Extracting last two digits from the total and if we have '00' cents
    cents = total[-2:]
    if cents == '00':
        points += 50
        print(f"Points for round dollar amount: {points}")
    # Checking if the total is a multiple of 0.25
    if int(cents) % 25 == 0:
        points += 25
        print(f"Points for total multiple of 0.25: 25")

    return points

def item_points(items: List[Dict[str, Any]]) -> int:
    points = 0
    number_of_items = len(items)
    # Checking the number of pairs
    points += (number_of_items // 2) * 5
    print(f"Points for item pairs: {points} ({number_of_items // 2} * 5)")

    for item in items:
        description, price = item["shortDescription"], float(item["price"])
        # Checking if description is a multiple of 3
        if len(description.strip()) % 3 == 0:
            points += math.ceil(price * 0.2)
            print(f"Points for {description} as multiple of 3: {math.ceil(price * 0.2)}")

    return points

def purchase_date_points(purchase_date: str) -> int:
    # Checking if the date is an odd or even number
    purchase_points = 6 if int(purchase_date[-1]) % 2 == 1 else 0
    print(f"Points for purchase date: {purchase_points}")

    return purchase_points

def purchase_time_points(purchase_time: str) -> int:
    hour, minute = int(purchase_time[:2]), int(purchase_time[3:])

    # Checking if purchase time is between 14:01 and 15:59
    purchase_time_pts = 10 if (hour == 14 and minute > 0) or (hour == 15) else 0
    print(f"Points for purchase time: {purchase_time_pts}")

    return purchase_time_pts

# Function aggregating the points collected using all the rules, based on the receipt data provided
def calculate_points(data: Dict[str, Any]) -> int:
    points = 0

    points += retailer_name_points(data["retailer"])
    points += value_points(data["total"])
    points += purchase_date_points(data["purchaseDate"])
    points += purchase_time_points(data["purchaseTime"])
    points += item_points(data["items"])

    print(f"Points: {points}")

    return points