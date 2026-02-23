inventory = [
    {"item_id": 1, "name": "Espresso", "unit_price": 2.50, "stock": 40},
    {"item_id": 2, "name": "Latte", "unit_price": 4.25, "stock": 25},
    {"item_id": 3, "name": "Cold Brew", "unit_price": 3.75, "stock": 30},
    {"item_id": 4, "name": "Mocha", "unit_price": 4.50, "stock": 20},
    {"item_id": 5, "name": "Blueberry Muffin", "unit_price": 2.95, "stock": 18},
]

status = ["Cancelled", "Placed", "Finished"]

orders = [
    {
        "Order ID": "Order_101",
        "Item ID": 2,
        "Quantity": 2,
        "Status": "Placed",
        "Total": 8.50
    },
    {
        "Order ID": "Order_102",
        "Item ID": 3,
        "Quantity": 1,
        "Status": "Placed",
        "Total": 3.75
    }
]


#CREATE
#Query 1
#### Create
#**Query 1:** Place a new order for an item and quantity.
#- Validate the item exists and enough stock is available.
#- Reduce stock.
#- Calculate and store total price: `quantity * unit_price`.
#- create a new key for this order
#- Record the order (add it to the orders list).
#- Set the order `status` to `Placed`.


#1 Input: user inputs item id and quantity
item_id_input = int(input("Enter the Item ID to order: "))
quantity = int(input("Enter the quantity: "))

#2 Process the order: Validate and create order
for item_id in inventory:
    if item_id["item_id"] == item_id_input:
        if item_id["stock"] >= quantity:
            total_price = quantity * item_id["unit_price"]
            item_id["stock"] -= quantity
            order_id = f"Order_{len(orders) + 101}"
            new_order = { #recording order
                "Order ID": order_id,
                "Item ID": item_id["item_id"],
                "Quantity": quantity,
                "Status": "Placed",
                "Total": total_price
            }
            orders.append(new_order) #adding it to list
#3 Output: display confirmation message with order ID and total price/ or error message if stock is insufficient
            print(f"Order placed successfully! Order ID: {order_id}, Total Price: ${total_price:.2f}")
        else:
            print("Insufficient stock for the requested quantity.")
        break
else:
    print("Item ID not found in inventory.")

print(f"Current stock for {item_id['name']} is {item_id['stock']}") #displaying current stock after order is placed

#READ
#Query 2: View all orders placed for a particular item.
#Prompt the user for the item name.
#Input:
search_item = input("Enter the item name to search (e.g. 'Latte'): ")

#Process: Find orders for item
#Step 1: Find matching item_id from inventory
matched_item_id = None

for inventory_item in inventory:
    if inventory_item["name"] == search_item:
        matched_item_id = inventory_item["item_id"]
        break

#Step 2: Find all orders with that item_id
matching_orders = []

if matched_item_id is not None:
    for order in orders:
        if order["Item ID"] == matched_item_id:
            matching_orders.append(order)


#Output:
if matched_item_id is None:
    print("Item not found in inventory.")
elif len(matching_orders) == 0:
    print("No orders found for this item.")
else:
    print(f"Orders for {search_item}:")
    for order in matching_orders:
        print(f"- Order ID: {order['Order ID']}, Quantity: {order['Quantity']}, Status: {order['Status']}, Total: ${order['Total']}")

# Query 3: Total number of orders placed for "Cold Brew".

# 1. Input:
target_item_name = "Cold Brew"


# 2. Process: Count orders for Cold Brew

# Step 1: Find the item_id for Cold Brew
cold_brew_id = None

for inventory_item in inventory:
    if inventory_item["name"] == target_item_name:
        cold_brew_id = inventory_item["item_id"]
        break

# Step 2: Count matching orders
order_count = 0

if cold_brew_id is not None:
    for order in orders:
        if order["Item ID"] == cold_brew_id and order["Status"] == "Placed":
            order_count += 1


# 3. Output:
if cold_brew_id is None:
    print("Cold Brew not found in inventory.")
else:
    print(f"Total orders placed for Cold Brew: {order_count}")

######
# Query 4: Update item stock quantity by item id and new stock quantity, then display updated stock.

# 1. Input:
item_id = int(input("Enter ID of item to update: "))
new_stock = int(input("Enter new stock quantity: "))


# 2. Process: Validate and update stock

updated_item = None

for inventory_item in inventory:
    if inventory_item["item_id"] == item_id:
        inventory_item["stock"] = new_stock
        updated_item = inventory_item
        break


# 3. Output:
if updated_item is not None:
    print(f"Stock updated successfully!")
    print(f"{updated_item['name']} now has {updated_item['stock']} in stock.")
else:
    print("Item ID not found in inventory.")

# Query 5: Cancel an order and restore stock.
#1. Prompt the user to enter an order ID.
#2. Find that order in the orders list.
#3. Change the order status to Cancelled.
#4. Read the item_id and quantity from the order.
#5. Locate the matching item in inventory and add the quantity back to its stock.


# 1. Input:
cancel_order_id = input("Enter Order ID to cancel: ")


# 2. Process: Cancel order and restore stock

found_order = None

# Step 1: Find the order
for order in orders:
    if order["Order ID"] == cancel_order_id:
        found_order = order
        break

# Step 2: If found, check status and restore stock
if found_order is not None:
    if found_order["Status"] == "Placed":
        
        # Change status
        found_order["Status"] = "Cancelled"
        
        # Get item_id and quantity from order
        ordered_item_id = found_order["Item ID"]
        ordered_quantity = found_order["Quantity"]
        
        # Restore stock in inventory
        for inventory_item in inventory:
            if inventory_item["item_id"] == ordered_item_id:
                inventory_item["stock"] += ordered_quantity
                break

        cancellation_success = True
    else:
        cancellation_success = False
else:
    cancellation_success = False


# 3. Output:
if found_order is None:
    print("Order ID not found.")
elif found_order["Status"] != "Cancelled":
    print("Order cannot be cancelled (already processed).")
else:
    print(f"Order {cancel_order_id} has been cancelled.")
    print(f"Stock restored successfully.")
