retailer_inventory = [
    {'store': 'a', 
     'book': {'price': 2, 'quantity': 20}, 
     'pen': {'price': 1, 'quantity': 100}, 
     'eraser': {'price': 3, 'quantity': 30}}, 
    
    {'store': 'b', 
     'book': {'price': 3, 'quantity': 30}, 
     'pen': {'price': 2, 'quantity': 20}, 
     'eraser': {'price': 1, 'quantity': 100}}, 
    
    {'store': 'c', 
     'book': {'price': 1, 'quantity': 100}, 
     'pen': {'price': 3, 'quantity': 30}, 
     'eraser': {'price': 2, 'quantity': 20}}
]

products_types = ["book", "pen", "eraser"]

# Function to display current inventory
def display_inventory():
    print("\nCurrent Inventory:")
    for store in retailer_inventory:
        print(f"\nStore: {store['store']}")
        for item in products_types:
            print(f"  {item.title()}: Price=${store[item]['price']}, Quantity={store[item]['quantity']}")

# Initial display
display_inventory()

# Main loop
while True:
    product = input("\nEnter product to buy (book/eraser/pen or 'exit' to quit): ").lower()
    if product == 'exit':
        break
    if product in products_types:
        try:
            quantity = int(input("Enter quantity: "))
        except:
            print("Has to be a number.")
            continue
        
        if quantity < 0:
            print("Setting quantity to 0.")
            quantity = 0

        price_list = []

        # Collect stores with available quantity
        for i in retailer_inventory:
            if i[product]["quantity"] > 0:
                data = dict(i[product])  # make a copy
                data["store"] = i["store"]
                price_list.append(data)

        if not price_list:
            print(f"No available stock for {product}.")
            continue

        # Sort by price (cheapest first)
        price_list.sort(key=lambda x: x["price"])

        # Purchase from cheapest available stores
        for x in price_list:
            if quantity == 0:
                break
            for y in retailer_inventory:
                if x["store"] == y["store"]:
                    available = y[product]["quantity"]
                    if available >= quantity:
                        y[product]["quantity"] -= quantity
                        quantity = 0
                    else:
                        y[product]["quantity"] = 0
                        quantity -= available

        print(f"{product.title()} purchased successfully.")

        # Show updated inventory
        display_inventory()
    else:
        print("Invalid product. Please choose from book, pen, or eraser.")
