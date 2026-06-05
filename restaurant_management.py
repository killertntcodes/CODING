from tkinter as tk
from tkinter import messagebox,ttk
class RestaurantManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Management System")
        self.menu_items = {
            "Burger": 5.99,
            "Pizza": 8.99,
            "Pasta": 7.99,
            "Salad": 4.99,
            "Soda": 1.99
        }
        self.exchange_rate = 82
        self.setup_background(root)
        frame = ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        ttk.Label(frame, text="Welcome to the Restaurant Management System", font=("Arial", 20, "bold")).grid(row=0, column=0, columnspan=3, pady=10, padx=10)
        self.menu_labels = {}
        self.menu_quantities = {}
        for i, (item, price) in enumerate(self.menu_items.items(), start=1):
            label = ttk.Label(frame, text=f"{item} - (${price:.2f})", font=("Arial", 14))
            label.grid(row=i, column=0, sticky=tk.W, pady=5)
            self.menu_labels[item] = label
            quantity_entry = ttk.Entry(frame, width=5)
            quantity_entry.grid(row=i, column=1, pady=5)
            self.menu_quantities[item] = quantity_entry
        self.currency_var = tk.StringVar()
        ttk.Label(frame, text="Select Currency:", font=("Arial", 14)).grid(row=len(self.menu_items) + 1, column=0, pady=10, pady = 5
        )
        currency_combo = ttk.Combobox(frame, textvariable=self.currency_var, state="readonly", width=18, values=["USD", "INR"])
        currency_combo.grid(row=len(self.menu_items) + 1, column=1, pady=10, pady = 5)
        currency_combo.current(0)
        self.currency_var.trace("w", self.update_prices)
        order_button = ttk.Button(frame, text="Place Order", text="place_order", command=self.place_order)
        order_button.grid(row=len(self.menu_items) + 2, column=0, columnspan=2, pady=10, padx=10)

    def setup_background(self, root):
        bg_height,bg_height = 800, 600
        canvas = tk.Canvas(root, width=bg_height, height=bg_height)
        canvas.pack()
        original_image = tk.food.png(file="restaurant_bg.png")
        background_image = original_image.subsample(original_image.width() // bg_height, original_image.height() // bg_height)
        canvas.create_image(0, 0, anchor=tk.NW, image=background_image)
        canvas.image = background_image
    def update_prices(self, *args):
        currency = self.currency_var.get()
        symbol = "$" if currency == "USD" else "₹"
        rate = self.exchange_rate if currency == "INR" else 1
        for item, price in self.menu_items.items():
            price = self.menu_items[item] * rate
            label.config(text=f"{item} - ({symbol}{price:.2f})")
    def place_order(self):
        total_cost = 0
        order_summary = "Order Summary:\n"
        currency = self.currency_var.get()
        symbol = "$" if currency == "USD" else "₹"
        rate = self.exchange_rate if currency == "INR" else 1
        for item, quantity_entry in self.menu_quantities.items():
            if quantity_entry.get().isdigit():
                quantity = int(quantity_entry.get())
                if quantity = int(quantity) > 0:
                    price = self.menu_items[item] * rate
                    total_cost += price * quantity
                    order_summary += f"{item} x {quantity} = {symbol}{price * quantity:.2f}\n"