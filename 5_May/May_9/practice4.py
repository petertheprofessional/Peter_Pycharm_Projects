products = [
    {
        "name": "apple",
        "category": "fruit",
        "price": 4.3,
    },
    {
        "name": "Croissant",
        "category": "bakery",
        "price": 1.3,
    },
    {
        "name": "Salmon",
        "category": "fish",
        "price": 15.00
    },
    {
        "name": "Soda Max",
        "category": "beverages",
        "price": 0.8
    },
    {
        "name": "Beer",
        "category": "beverages",
        "price": 1
    }
]

print("What is the product category >>> ", end='')
enter_category = input()
print("What is the quantity? >>> ", end='')
enter_amount = int(input())

def show_discount(discount):
    for product in products:
        if product["category"] == enter_category:
            value = (enter_amount * product['price']) * 0.9
            print(f"{product['name']}: {value}")

show_discount(enter_amount)


