import customtkinter as ctk
import tkinter as tk

app = ctk.CTk()
app.geometry("800x600") #Creates ui size
app.title("Joshi's Football Store")

PRODUCTS = []
TEAMS = ["Manchester United", "Chelsea", "Real Madrid", "Nottingham Forest"]
BRANDS = ["Nike", "Adidas", "Puma", "Asics"]

class Products: # Parent class for the child classes of the different categories
    def __init__(self, name, price, quality): # Initialises the attributes of the class
        self.name = name
        self.price = price
        self.quality = quality

class football_kits(Products): #Child class for the football kits
    pass

class football_boots(Products): #Child class for the football boots
    pass

class football_balls(Products):#Child class for the football balls
    pass

class Cart: #Class for the cart
    def __init__(self):
        self.items = [] 

    def add_to_cart(self, product): #Function to add products to the cart
        self.items.append(product)
        update_cart_label()

    def get_total(self): #Function to find the total price in the cart
        return sum(item.price for item in self.items)

    def clear_cart(self): #Function to clear the cart
        self.items.clear()
        update_cart_label()

cart = Cart() #Creates an instance of the cart class

def update_cart_label(): #Function to update the cart label in the top right corner
    cart_label.configure(text=f"Cart: {len(cart.items)} items, Total: ${cart.get_total()}")

#Provides values for the different products and stores into a class
man_united = football_kits("Manchester United", 100, "New") 
real_madrid = football_kits("Real Madrid", 110, "Used")
nottingham_forest = football_kits("Nottingham Forest", 120, "Perfect")

Nike = football_boots("Nike", 100, "Good")
Adidas = football_boots("Adidas", 90, "Good")
Puma = football_boots("Puma", 80, "Good")

Nike_ball = football_balls("Nike", 100, "Top quality")
Adidas_ball = football_balls("Adidas", 90, "Mid range")
Puma_ball = football_balls("Puma", 80, "Low end")

def store_start(): #Function to start the store screen
    first_label.configure(text="Welcome to Joshi's Football Store") #configures text in the postion of label 1
    second_label.configure(text="Please pick which category you would like to shop in")
    third_label.grid_remove()
    button1.configure(text="Football Kits", command=football_kits) #configures text in the postion of button 1
    button1.grid() #places button 1 in the grid
    button2.configure(text="Football Boots", command=football_boots)
    button2.grid()
    button3.configure(text="Football Balls", command=football_balls)
    button3.grid()
    button4.configure(text="View Cart", command=view_cart)
    button4.grid()

def football_kits(): #Function to show the football kits screen
    first_label.configure(text="Football Kits") #configures text in the postion of label 1
    second_label.configure(text="Please pick which football kit you would like to buy")
    button1.configure(text="Manchester United", command=lambda: show_product(man_united)) #configures text in the postion of button 1
    button2.configure(text="Real Madrid", command=lambda: show_product(real_madrid))
    button3.configure(text="Nottingham Forest", command=lambda: show_product(nottingham_forest)) #Uses lambda to pass the product to the show_product function
    button4.configure(text='Back', command=store_start)
    button4.grid()  #places button 4 in the grid

def football_boots(): #Function to show the football boots screen
    first_label.configure(text="Football Boots") #configures text in the postion of label 1
    second_label.configure(text="Please pick which football boots you would like to buy")
    button1.configure(text="Nike", command=lambda: show_product(Nike)) #configures text in the postion of button 1
    button2.configure(text="Adidas", command=lambda: show_product(Adidas))
    button3.configure(text="Puma", command=lambda: show_product(Puma))
    button4.configure(text="Back", command=store_start)
    button4.grid() #places button 4 in the grid

def football_balls(): #Function to show the football balls screen
    first_label.configure(text="Football Balls") #configures text in the postion of label 1
    second_label.configure(text="Please pick which football ball you would like to buy")
    button1.configure(text="Nike", command=lambda: show_product(Nike_ball))
    button2.configure(text="Adidas", command=lambda: show_product(Adidas_ball))
    button3.configure(text="Puma", command=lambda: show_product(Puma_ball))
    button4.configure(text="Back", command=store_start)
    button4.grid() #places button 4 in the grid

def show_product(product): #Function to show the product screen
    first_label.configure(text=product.name)
    second_label.configure(text=f"Price: ${product.price}") #calls the attributes of the product class
    third_label.configure(text=f"Quality: {product.quality}")
    third_label.grid() #places the third label in the grid
    button1.configure(text="Add to Cart", command=lambda: add_to_cart(product))
    button2.configure(text="Back", command=store_start)
    button3.configure(text="Exit", command=app.destroy) #closes the app
    button4.configure(text="", command=None)
    button4.grid_remove() #removes button 4 from the screen

def add_to_cart(product): #Function to add the product to the cart
    cart.add_to_cart(product)
    store_start()

def view_cart(): #Function to view the cart
    first_label.configure(text="Cart")
    second_label.configure(text="Your Cart Items:")
    cart_items_text = "\n".join([f"{item.name} - ${item.price}" for item in cart.items]) #joins the items in the cart
    third_label.configure(text=cart_items_text if cart_items_text else "Cart is empty") #displays the items in the cart and if empty displays 'Cart is empty'
    third_label.grid() #places the third label in the grid
    button1.configure(text="Buy", command=buy_items) 
    button2.configure(text="Clear Cart", command=clear_cart)
    button3.configure(text="Back", command=store_start)
    button4.configure(text="Exit", command=app.destroy)
    button4.grid()

def buy_items(): #Function to buy the items in the cart
    if cart.items: #if the cart is not empty
        first_label.configure(text="Thank you for your purchase!")
        second_label.configure(text="")
        third_label.configure(text="")
        cart.clear_cart() #clears the cart
    else: #if the cart is empty
        first_label.configure(text="Cart is empty")
        second_label.configure(text="")
        third_label.configure(text="")
    button1.configure(text="Back to Store", command=store_start)
    button2.configure(text="", command=None)
    button3.configure(text="", command=None)
    button4.configure(text="", command=None)
    button2.grid_remove() #removes button 2 from the screen
    button3.grid_remove()
    button4.grid_remove()

def clear_cart(): #Function to clear the cart
    cart.clear_cart()
    view_cart()

#The labels and button bellow are set up in the grid with their respective text and commands
first_label = ctk.CTkLabel(app, text="", font=("Nunito", 24)) 
first_label.grid(row=0, column=0, padx=10, pady=10)

second_label = ctk.CTkLabel(app, text="", font=("Nunito", 24))
second_label.grid(row=1, column=0, padx=10, pady=50)

third_label = ctk.CTkLabel(app, text="", font=("Nunito", 24))
third_label.grid(row=2, column=0, padx=10, pady=10)

cart_label = ctk.CTkLabel(app, text="Cart: 0 items, Total: $0", font=("Nunito", 18))
cart_label.grid(row=0, column=1, padx=10, pady=10, sticky="e")

button1 = ctk.CTkButton(app, text="")
button1.grid(row=3, column= 0, padx=200, pady=50)

button2 = ctk.CTkButton(app, text="")
button2.grid(row=4, column=0, padx=0, pady=0)

button3 = ctk.CTkButton(app, text="")
button3.grid(row=5, column=0, padx=0, pady=50)

button4 = ctk.CTkButton(app, text="")
button4.grid(row=6, column=0, padx=0, pady=0)

store_start() #Starts the store screen

app.mainloop() #Runs the app