products = {
    101: {
        "name": "Tea Powder",
        "quantity": 3
    },
    102: {
        "name": "Sugar",
        "quantity": 25
    },
    103: {
        "name": "Milk",
        "quantity": 2
    }
}
sales = [
    {
        "product_id": 101,
        "quantity": 5,
        "amount": 1250
    },
    {
        "product_id": 102,
        "quantity": 10,
        "amount": 450
    }
]
purchases = [
    {
        "product_id": 101,
        "quantity": 20
    },
    {
        "product_id": 103,
        "quantity": 15
    }
]
def low_stock_report():
    print("\n--- LOW STOCK REPORT ---")
    found = False
    for product_id, product in products.items():
        if product["quantity"] <= 5:
            print("-------------------------")
            print("Product ID :", product_id)
            print("Product    :", product["name"])
            print("Quantity   :", product["quantity"])
            found = True
    if found == False:
        print("No low-stock products.")
def sales_report():
    print("\n--- SALES REPORT ---")
    total_sales = 0
    for sale in sales:
        print("------------------------")
        print("Product ID :", sale["product_id"])
        print("Quantity   :", sale["quantity"])
        print("Amount     :", sale["amount"])
        total_sales += sale["amount"]
    print("-------------------------")
    print("Total Sales :", total_sales)
def purchase_report():
    print("\n--- PURCHASE REPORT ---")
    total_quantity = 0
    for purchase in purchases:
        print("-------------------------")
        print("Product ID :", purchase["product_id"])
        print("Quantity   :", purchase["quantity"])
        total_quantity += purchase["quantity"]
    print("-------------------------")
    print("Total Purchased Quantity :", total_quantity)
while True:
    print("\n===== REPORT MANAGEMENT =====")
    print("1. Low Stock Report")
    print("2. Sales Report")
    print("3. Purchase Report")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        low_stock_report()
    elif choice == 2:
        sales_report()
    elif choice == 3:
        purchase_report()
    elif choice == 4:
        break
    else:
        print("Invalid choice.")
