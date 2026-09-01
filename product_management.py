products = []


def add_product():
    print("\n--- ADD PRODUCT ---")

    product_id = int(input("Enter Product ID: "))
    name = input("Enter Product Name: ")
    category = input("Enter Category: ")
    quantity = int(input("Enter Quantity: "))
    price = float(input("Enter Price: "))

    product = {
        "id": product_id,
        "name": name,
        "category": category,
        "quantity": quantity,
        "price": price
    }

    products.append(product)

    print("Product added successfully!")


def view_products():
    print("\n--- VIEW PRODUCTS ---")

    if len(products) == 0:
        print("No products available.")

    else:
        for product in products:
            print("-------------------------")
            print("Product ID :", product["id"])
            print("Name       :", product["name"])
            print("Category   :", product["category"])
            print("Quantity   :", product["quantity"])
            print("Price      :", product["price"])


def search_product():
    print("\n--- SEARCH PRODUCT ---")

    name = input("Enter Product Name: ")

    for product in products:

        if product["name"].lower() == name.lower():
            print("Product Found!")
            print("Product ID :", product["id"])
            print("Name       :", product["name"])
            print("Category   :", product["category"])
            print("Quantity   :", product["quantity"])
            print("Price      :", product["price"])
            return

    print("Product not found.")


def update_product():
    print("\n--- UPDATE PRODUCT ---")

    product_id = int(input("Enter Product ID: "))

    for product in products:

        if product["id"] == product_id:

            product["name"] = input("Enter New Name: ")
            product["category"] = input("Enter New Category: ")
            product["quantity"] = int(input("Enter New Quantity: "))
            product["price"] = float(input("Enter New Price: "))

            print("Product updated successfully!")
            return

    print("Product not found.")


def delete_product():
    print("\n--- DELETE PRODUCT ---")

    product_id = int(input("Enter Product ID: "))

    for product in products:

        if product["id"] == product_id:
            products.remove(product)
            print("Product deleted successfully!")
            return

    print("Product not found.")

while True:

    print("\n===== PRODUCT MANAGEMENT =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_product()

    elif choice == 2:
        view_products()

    elif choice == 3:
        search_product()

    elif choice == 4:
        update_product()

    elif choice == 5:
        delete_product()

    elif choice == 6:
        break

    else:
        print("Invalid choice.")
