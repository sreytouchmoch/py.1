
input = [
    {"name": "banana", "price": 50},
    {"name": "apple", "price": 10},
    {"name": "coconut", "price": 75},
]

result = []
for fruit in input:
    fruitName = fruit["name"]
    fruitPrice = fruit["price"]

    if fruitPrice < 20:
        result.append(fruitName)

print(result)