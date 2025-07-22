class Product:
    def __init__(self, product_id, name, price, source):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.source = source

    def __str__(self):
        return f"ID: {self.product_id} | Name: {self.name} | Price: {self.price} | Source: {self.source}"

products = []

def add_product():
    try:
        product_id = input("Enter product ID: ").strip()
        name = input("Enter product name: ").strip()
        price = float(input("Enter product price: "))
        source = input("Enter product source: ").strip()
        products.append(Product(product_id, name, price, source))
        print("Product added successfully.\n")
    except ValueError:
        print("Invalid input. Please enter numeric value for price.\n")

def display_products():
    if not products:
        print("Product list is empty.\n")
    else:
        print("Product List:")
        for product in products:
            print(product)
        print()

def filter_products_by_price():
    try:
        limit = float(input("Enter price limit: "))
        filtered = [p for p in products if p.price < limit]
        if not filtered:
            print("No products found below that price.\n")
        else:
            print("Filtered Products:")
            for p in filtered:
                print(p)
            print()
    except ValueError:
        print("Invalid input. Please enter a numeric value.\n")

def update_product():
    product_id = input("Enter product ID to update: ").strip()
    for p in products:
        if p.product_id == product_id:
            p.name = input("Enter new name: ").strip()
            try:
                p.price = float(input("Enter new price: "))
            except ValueError:
                print("Invalid price. Update canceled.\n")
                return
            p.source = input("Enter new source: ").strip()
            print("Product updated successfully.\n")
            return
    print("Product not found.\n")

def delete_product():
    product_id = input("Enter product ID to delete: ").strip()
    global products
    products = [p for p in products if p.product_id != product_id]
    print("Product deleted if existed.\n")

def menu():
    while True:
        print("------ MENU ------")
        print("1. Add Product")
        print("2. Display Product List")
        print("3. Filter Products by Price")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Exit")
        choice = input("Select an option (1-6): ")

        match choice:
            case "1":
                add_product()
            case "2":
                display_products()
            case "3":
                filter_products_by_price()
            case "4":
                update_product()
            case "5":
                delete_product()
            case "6":
                print("Exiting program.")
                break
            case _:
                print("Invalid option. Please try again.\n")

if __name__ == "__main__":
    menu()
