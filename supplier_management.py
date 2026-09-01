suppliers = []
def add_supplier():
    print("\n--- ADD SUPPLIER ---")
    supplier_id = int(input("Enter Supplier ID: "))
    name = input("Enter Supplier Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    supplier = {
        "id": supplier_id,
        "name": name,
        "phone": phone,
        "email": email
    }
    suppliers.append(supplier)
    print("Supplier added successfully!")
def view_suppliers():
    print("\n--- SUPPLIER LIST ---")
    if len(suppliers) == 0:
        print("No suppliers available.")
    else:
        for supplier in suppliers:
            print("-------------------------")
            print("Supplier ID :", supplier["id"])
            print("Name        :", supplier["name"])
            print("Phone       :", supplier["phone"])
            print("Email       :", supplier["email"])
def search_supplier():
    print("\n--- SEARCH SUPPLIER ---")
    name = input("Enter Supplier Name: ")
    for supplier in suppliers:
        if supplier["name"].lower() == name.lower():
            print("Supplier Found!")
            print("ID    :", supplier["id"])
            print("Name  :", supplier["name"])
            print("Phone :", supplier["phone"])
            print("Email :", supplier["email"])
            return
    print("Supplier not found.")
while True:
    print("\n===== SUPPLIER MANAGEMENT =====")
    print("1. Add Supplier")
    print("2. View Suppliers")
    print("3. Search Supplier")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_supplier()
    elif choice == 2:
        view_suppliers()
    elif choice == 3:
        search_supplier()
    elif choice == 4:
        break
    else:
        print("Invalid choice.")
