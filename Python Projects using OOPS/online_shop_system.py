class User:
    def __init__(self,username,email):
        self.username = username
        self.email = email

class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
        
    def basic_info(self):
        print(f"product: {self.name}")
        print(f"Price: {self.price}")


class Customer(User):
    def __init__(self, username, email):
        super().__init__(username, email)
        self.cart = []

    def add_to_cart(self,product):
        self.cart.append(product)

    def rmv_from_cart(self,product):
        if product in self.cart:
            self.cart.remove(product)
        else:
            print("Item not in your cart")

    def view_cart(self):
        print("Items in cart: ")
        for product in self.cart:
            print(product.name)

    def save_cart(self, filename):
        with open(filename, "w") as file:
            for product in self.cart:
                file.write(f"{product.name}, {product.price}")

        print(f"cart saved to {filename}")


class Seller(User):
    def __init__(self, username, email):
        super().__init__(username, email)
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def rmv_from_cart(self,product):
        if product in self.products:
            self.products.remove(product)
        else:
            print("Item not in your cart")

    def view_cart(self):
        print("Items in cart: ")
        for product in self.products:
            print(product.name)

    def save_cart(self, filename):
        with open(filename, "w") as file:
            for product in self.products:
                file.write(f"{product.name}, {product.price}")
        print(f"products saved to {filename}")




customer = Customer("Billy", "billy@hoo.com")
seller = Seller("Serar", "jane@yah.com")

# Create products
product1 = Product("Shoes", 65)
product2 = Product("Ring", 125.60)
product3 = Product("T-Shirt", 28.00)

# Add products to customer's cart
customer.add_to_cart(product1)
customer.add_to_cart(product2)
customer.add_to_cart(product3)

# View customer's cart
customer.view_cart()

customer.save_cart("customer_cart.txt")

customer.rmv_from_cart(product2)
customer.view_cart()
# # Correct instantiation and adding to cart
# new_customer = Customer("Ajaskh", "ajaskh@gmail.com")

# # Add products to the new customer's cart
# new_customer.add_to_cart(product1)
# new_customer.add_to_cart(product2)

# # View new customer's cart
# new_customer.view_cart()
