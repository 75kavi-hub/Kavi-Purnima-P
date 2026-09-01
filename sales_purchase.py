products = {
    101: {
        "name": "Tea Powder",
        "quantity": 50,
        "price": 250
    },
    102: {
        "name": "Sugar",
        "quantity": 30,
        "price": 45
    }
}
sales = []
purchases = []
def sell_product():
    print("\n--- SELL PRODUCT ---")
    product_id = int(input("Enter Product ID: "))
    quantity = int(input("Enter Quantity Sold: "))
    if product_id in products:
        if quantity <= products[product_id]["quantity"]:
            total = quantity * products[product_id]["price"]
            products[product_id]["quantity"] -= quantity
            sales.append({
                "product_id": product_id,
                "quantity": quantity,
                "total": total
            })
            print("Sale completed successfully!")
            print("Total Amount :", total)
            print("Remaining Stock :",
                  products[product_id]["quantity"])
        else:
            print("Not enough stock.")
    else:
        print("Product not found.")
def purchase_product():
    print("\n--- PURCHASE PRODUCT ---")
    product_id = int(input("Enter Product ID: "))
    quantity = int(input("Enter Quantity Purchased: "))
    if product_id in products:
        products[product_id]["quantity"] += quantity
        purchases.append({
            "product_id": product_id,
            "quantity": quantity
        })
        print("Purchase completed successfully!")
        print("Updated Stock :",
              products[product_id]["quantity"])
    else:
        print("Product not found.")
def view_sales():
    print("\n--- SALES DETAILS ---")
    for sale in sales:
        print("-------------------------")
        print("Product ID :", sale["product_id"])
        print("Quantity   :", sale["quantity"])
        print("Total      :", sale["total"])
def view_purchases():
    print("\n--- PURCHASE DETAILS ---")
    for purchase in purchases:
        print("-------------------------")
        print("Product ID :", purchase["product_id"])
        print("Quantity   :", purchase["quantity"])
while True:
    print("\n===== SALES & PURCHASE =====")
    print("1. Sell Product")
    print("2. Purchase Product")
    print("3. View Sales")
    print("4. View Purchases")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        sell_product()
    elif choice == 2:
        purchase_product()
    elif choice == 3:
        view_sales()
    elif choice == 4:
        view_purchases()
    elif choice == 5:
        break
    else:
        print("Invalid choice.")
