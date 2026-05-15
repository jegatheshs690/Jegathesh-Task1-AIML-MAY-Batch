# -----------------------------
# Part A — Spot the Bug
# -----------------------------

def add_item_bug(item, cart=[]):
    cart.append(item)
    return cart


print("Part A Output:")
print(add_item_bug("apple"))
print(add_item_bug("banana"))
print(add_item_bug("milk", cart=["bread"]))
print(add_item_bug("eggs"))

# Explanation:
# The default list cart=[] is created only ONCE when the function is defined.
# So the same list is reused in future function calls.
# That is why "apple", "banana", and "eggs" stay in the same list.


# -----------------------------
# Part B — Fix It
# -----------------------------

def add_item(item, cart=None):
    if cart is None:
        cart = []

    cart.append(item)
    return cart


print("\nPart B Output:")
print(add_item("apple"))
print(add_item("banana"))
print(add_item("eggs"))

# Now each function call gets a fresh new list.


# -----------------------------
# Part C — Shopping Cart System
# -----------------------------

# Function to create a cart
def create_cart(owner, discount=0):
    return {
        "owner": owner,
        "items": [],
        "discount": discount
    }


# Function to add items into cart
def add_to_cart(cart, name, price, qty=1):
    item = {
        "name": name,
        "price": price,
        "qty": qty
    }

    cart["items"].append(item)


# Function to demonstrate tuple immutability
def update_price(price_tuple, new_price):
    try:
        price_tuple[1] = new_price
    except TypeError as e:
        print("\nTuple Error:")
        print(e)

    # Tuples are immutable.
    # Their values cannot be changed after creation.


# Function to calculate total
def calculate_total(cart):
    total = 0

    for item in cart["items"]:
        total += item["price"] * item["qty"]

    # Apply discount
    discount_amount = total * (cart["discount"] / 100)
    final_total = total - discount_amount

    return final_total


# -----------------------------
# Creating carts for customers
# -----------------------------

cart1 = create_cart("Aarav", 10)
cart2 = create_cart("Meera", 5)

# Adding items to cart1
add_to_cart(cart1, "Laptop", 50000, 1)
add_to_cart(cart1, "Mouse", 1000, 2)

# Adding items to cart2
add_to_cart(cart2, "Book", 500, 3)

# Display carts
print("\nCustomer 1 Cart:")
print(cart1)

print("\nCustomer 2 Cart:")
print(cart2)

# Calculating totals
print("\nCustomer 1 Total:", calculate_total(cart1))
print("Customer 2 Total:", calculate_total(cart2))

# Demonstrating tuple immutability
price_data = ("Laptop", 50000)
update_price(price_data, 60000)


# -----------------------------
# Discussion Points
# -----------------------------

# 1. Why is discount=0 safe but cart=[] dangerous?
#
# discount=0 is safe because integers are immutable.
# cart=[] is dangerous because lists are mutable.
# The same list object gets reused across function calls.


# 2. What is the difference between rebinding and mutating?
#
# Rebinding means assigning a variable to a new object.
# Example:
# x = [1, 2]
# x = [3, 4]
#
# Mutating means changing the existing object itself.
# Example:
# x.append(5)


# 3. Which of these are mutable?
#
# Mutable:
# list, dict, set
#
# Immutable:
# tuple, str, int


# 4. When you pass a list into a function and modify it,
#    do changes reflect outside? Why?
#
# Yes.
# Because lists are mutable and functions receive a reference
# to the same list object.
# So modifications affect the original list outside the function.
