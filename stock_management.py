stock = {
    "Tea Powder": 50,
    "Sugar": 30,
    "Milk": 40
}
def view_stock():

    print("\n--- CURRENT STOCK ---")

    for product, quantity in stock.items():
        print(product, ":", quantity)
def add_stock():

    print("\n--- ADD STOCK ---")

    product = input("Enter Product Name: ")
    quantity = int(input("Enter Quantity: "))

    if product in stock:
        stock[product] += quantity
    else:
        stock[product] = quantity

    print("Stock added successfully!")
def reduce_stock():

    print("\n--- REDUCE STOCK ---")

    product = input("Enter Product Name: ")
    quantity = int(input("Enter Quantity: "))

    if product in stock:

        if quantity <= stock[product]:
            stock[product] -= quantity
            print("Stock reduced successfully!")

        else:
            print("Not enough stock.")
    else:
        print("Product not found.")
def low_stock():

    print("\n--- LOW STOCK PRODUCTS ---")

    found = False

    for product, quantity in stock.items():

        if quantity <= 5:
            print(product, ":", quantity)
            found = True

    if found == False:
        print("No low-stock products.")
while True:

    print("\n===== STOCK MANAGEMENT =====")
    print("1. View Stock")
    print("2. Add Stock")
    print("3. Reduce Stock")
    print("4. Low Stock")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        view_stock()

    elif choice == 2:
        add_stock()

    elif choice == 3:
        reduce_stock()

    elif choice == 4:
        low_stock()

    elif choice == 5:
        break

    else:
        print("Invalid choice.")
