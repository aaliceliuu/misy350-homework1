# Homework Assignment Draft: Coffee Shop Kiosk Inventory & Orders (CRUD)
**Scenario:** You are building the backend logic for a new **"Smart Coffee Kiosk"**. This automated kiosk has a limited stock of ingredients for each drink (stored inside the machine). The owner needs a system to track this inventory in real-time, place orders, and release stock back if an order is cancelled.

**Goal:** Build a Python program that performs CRUD operations on inventory items and orders using lists and dictionaries.

## Learning Goals
- Practice Python fundamentals (variables, lists/dicts, loops, conditionals, functions)
- Implement CRUD operations cleanly
- Simulate a database using in-memory data structures
- Write readable, organized code

## Project Setup
1. **GitHub:** Create a new repository on GitHub named `misy350-homework1`.
2. **Local Folder:** Create a folder on your computer with the same name.
3. **VS Code:** Open this new folder in VS Code.
4. **Git Init:** Initialize the repository and connect it to your GitHub repo (or clone it).
5. **Files:** Create the following files:
   - `main.py` (Your code goes here)
   - `.gitignore` (Add `.env` to this file)
   - `.env` (For environment variables, if any)

## Requirements

## Design Requirements

### 1. IPO Pattern
- **Use the IPO Pattern:** Structure each function using the **Input-Process-Output** workflow discussed in class:
  1. **Input:** Get the data you need (arguments or user input).
  2. **Process:** Perform the logic (calculations, updating lists).
     > **Requirement:** Define the process name clearly starting with an action verb (e.g., "Find Low Inventory Stocks").
  3. **Output:** Return a value or print a success/failure message.

### 2. Naming Conventions
- **Meaningful Names:** All variables, lists, dictionaries, and functions must have meaningful, relevant names.
  - **Do not** use generic names like `x`, `y`, `list`, `data`, or `dict`.
  - **Do** use descriptive names like `customer_orders`, `inventory_item`, `total_price`, or `updated_stock`.



## Program Requirements


### 1) Data Model (In Memory)
- Inventory items stored in a list of dictionaries.
- Each item must include: `id`, `name`, `price`, `stock`.
- Orders stored in a list of dictionaries.
- Each order must include: `order_id`, `item_id`, `quantity`,`status`, `total`.

(status = `Cancelled`,`Placed`,`Finished`)

**Starter Inventory Data (5 items):**
```python
inventory = [
    {"item_id": 1, "name": "Espresso", "unit_price": 2.50, "stock": 40},
    {"item_id": 2, "name": "Latte", "unit_price": 4.25, "stock": 25},
    {"item_id": 3, "name": "Cold Brew", "unit_price": 3.75, "stock": 30},
    {"item_id": 4, "name": "Mocha", "unit_price": 4.50, "stock": 20},
    {"item_id": 5, "name": "Blueberry Muffin", "unit_price": 2.95, "stock": 18},
]
```

**Orders (create this list with two sample orders):**
Create an `orders` list with **two** entries using the following data.
Ensure you use a unique string for the `order_id` (e.g., `"Order_101"`). 

- **Order 1:** Order iD: `"Order_101"`, Item ID: `2`, Quantity: `2`, Status: `"Placed"`, Total: `8.50`
- **Order 2:** Order iD: `"Order_102"`, Item ID: `3`, Quantity: `1`, Status: `"Placed"`, Total: `3.75`

### 2) Main File Structure (Required)
- Organize `main.py` into four labeled sections: **Create**, **Read**, **Update**, **Remove/Delete**.
- Within each section, label queries exactly as `Query 1`, `Query 2`, etc.


## CRUD Sections (Place Code Below)
### Example: Read
**Query 0:** View all items in the inventory with stock less than 20.
```python
# Query 0: View all items in the inventory with stock less than 20.

# 1. Input:
# Define the threshold for low stock (20) and access the inventory list.
threshold = 5

# 2. Process: Find items with stock below threshold
# Loop through the inventory to find matches
low_stock_items = []
for item in inventory:
    if item["stock"] < threshold:
        # Found one! Add it to our result list
        low_stock_items.append(item)

# 3. Output:
# Print the results
if len(low_stock_items) > 0:
    print("Low stock items found:")
    for item in low_stock_items:
        print(f"- {item['name']}: {item['stock']}")
else:
    print("No low stock items.")
```

### Create
**Query 1:** Place a new order for an item and quantity.
- Validate the item exists and enough stock is available.
- Reduce stock.
- Calculate and store total price: `quantity * unit_price`.
- create a new key for this order
- Record the order (add it to the orders list).
- Set the order `status` to `Placed`.

```python
# Query 1: Place a new order for an item and quantity.


# 1. Input:
# ...
item_id = int(input("Enter the Item ID to order: "))
quantity = int(input("Enter the quantity: "))


# 2. Process: [Name process here, e.g. "Validate and create order"]
# ...





# 3. Output:
# ...






```

### Read
**Query 2:** View all orders placed for a particular item — prompt the user to enter the item name.

```python
# Query 2: View all orders placed for a particular item.
# Prompt the user for the item name.

# 1. Input:
# ...
search_item = input("Enter the item name to search (e.g. 'Latte'): ")



# 2. Process: [Name process here, e.g. "Find orders for item"]
# ...




# 3. Output:
# ...





```

**Query 3:** Calculate and print the total number of orders placed for "Cold Brew".

```python
# Query 3: Total number of orders placed for "Cold Brew".

# 1. Input:
# ...




# 2. Process: [Name process here, e.g. "Count orders"]
# ...




# 3. Output:
# ...





```

### Update
**Query 4:** Prompt the user to enter an item id and new quantity. Update the item stock quantity.

```python
# Query 4: Update item stock quantity by item id.

# 1. Input:
# ...
item_id = int(input("Enter ID of item to update: "))
new_stock = int(input("Enter new stock quantity: "))



# 2. Process: [Name process here, e.g. "Validate and update stock"]
# ...




# 3. Output:
# ...



```

### Remove/Delete
**Query 5:** Cancel an order (and restore stock) using the steps below:
1. Prompt the user to enter an order ID.
2. Find that order in the `orders` list.
3. Change the order `status` to `Cancelled`.
4. Read the `item_id` and `quantity` from the order.
5. Locate the matching item in `inventory` and add the quantity back to its `stock`.

```python
# Query 5: Cancel an order and restore stock.

# 1. Input:
# ...
cancel_order_id = input("Enter Order ID to cancel: ")


# 2. Process: [Name process here, e.g. "Cancel order"]
# ...




# 3. Output:
# ...





```




## Testing Plan
Run the application and test each query using the following inputs. Your screenshots should show these exact steps:

1.  **Create (Query 1):**
    *   **Action:** Place a new order.
    *   **Input:** Item ID: `2` (Latte), Quantity: `2`.
    *   **Expected Result:** Stock for Latte reduces from 25 to 23.

2.  **Read (Query 2):**
    *   **Action:** Search for orders by item name.
    *   **Input:** `Latte`
    *   **Expected Result:** Should show the new order you just placed (and any previous ones).

3.  **Analysis (Query 3):**
    *   **Action:** Run the analysis.
    *   **Input:** *None*
    *   **Expected Result:** Should correctly count orders for "Cold Brew".

4.  **Update (Query 4):**
    *   **Action:** Update stock manually.
    *   **Input:** Item ID: `3` (Cold Brew), New Stock: `28`.
    *   **Expected Result:** Cold Brew stock updates to 28.

5.  **Delete (Query 5):**
    *   **Action:** Cancel an order.
    *   **Input:** Order ID: `Order_101`.
    *   **Expected Result:** Order status changes to "Cancelled", and Stock for Item 2 (Latte) increases back by 2.

## Deliverables
1. **Source Code:** Submit one of the following:
   - This markdown file (`homework1_python_refresher.md`) with your code pasted into the blocks above.
   - OR your `main.py` file (must include the exact IPO comment headers for each query).
2. **Repository Screenshot:** A full-screen screenshot of your GitHub repository page showing your files.
3. **Test Run Screenshot:** Start with a clean/cleared terminal. Run your program and perform the actions listed in the **Testing Plan** section above *exactly* in the order listed. Take a full-screen screenshot showing your inputs and the program's output.