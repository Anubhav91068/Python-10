n = int(input())

stock = {}

for i in range(n):
    item, qty = input().split()
    stock[item] = int(qty)

q = int(input())

for i in range(q):
    action, item, qty = input().split()
    qty = int(qty)

    if action == "ADD":
        stock[item] = stock.get(item, 0) + qty

    elif action == "SELL":
        if stock[item] >= qty:
            stock[item] -= qty
        else:
            print("Insufficient stock:", item)

for item in stock:
    print(item, stock[item])