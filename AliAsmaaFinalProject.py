"""
Author: Asmaa Ali
Date: 10/1/24
File: finalProjectMod06.py
Github link:https://github.com/asmaayasser1/-vitamin-juices-/tree/main
 
 This application is to allow users to create custom juice blends by selecting 
a juice base, adding supplements, and specifying the size of the drink. 

"""
import tkinter as tk
from tkinter import messagebox, PhotoImage

class VitaminJuicesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Vitamin Juices")
        self.root.geometry("500x400")

        # Correct file references based on the image types and names
        self.juice_image = PhotoImage(file="fruit.png")  
        self.logo_image = PhotoImage(file="logo Juice.png")  

        # Main frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()

        # Display the logo image at the top
        self.logo_label = tk.Label(self.main_frame, image=self.logo_image)
        self.logo_label.pack(pady=10)

        # Title label
        self.title_label = tk.Label(self.main_frame, text="Welcome to Vitamin Juices", font=("Arial", 24))
        self.title_label.pack(pady=10)

        # Buttons in the Main Window
        self.create_juice_button = tk.Button(self.main_frame, text="Create Your Juice", command=self.open_order_window)
        self.create_juice_button.pack(pady=10)

        self.view_orders_button = tk.Button(self.main_frame, text="View Previous Orders", command=self.view_orders)
        self.view_orders_button.pack(pady=10)

        self.exit_button = tk.Button(self.main_frame, text="Exit", command=self.root.quit)
        self.exit_button.pack(pady=10)

        # Initialize Order Window (hidden at first)
        self.init_order_window()

    def init_order_window(self):
        self.order_window = tk.Toplevel(self.root)
        self.order_window.title("Customize Your Juice")
        self.order_window.geometry("500x400")
        self.order_window.withdraw()  # Hide until the user clicks "Create Your Juice"

        # Variables to store user selections
        self.juice_base_var = tk.StringVar()
        self.supplement_var = tk.StringVar()
        self.size_var = tk.StringVar()

        # Title label for Order Window
        tk.Label(self.order_window, text="Customize Your Juice", font=("Arial", 18)).pack(pady=10)

        # Juice Base
        tk.Label(self.order_window, text="Select Juice Base").pack(pady=5)
        tk.Entry(self.order_window, textvariable=self.juice_base_var).pack()

        # Supplement
        tk.Label(self.order_window, text="Select Supplement").pack(pady=5)
        tk.Entry(self.order_window, textvariable=self.supplement_var).pack()

        # Size
        tk.Label(self.order_window, text="Select Size").pack(pady=5)
        tk.Entry(self.order_window, textvariable=self.size_var).pack()

        # Buttons in Order Window
        tk.Button(self.order_window, text="Submit Order", command=self.submit_order).pack(pady=10)
        tk.Button(self.order_window, text="Clear Selections", command=self.clear_selections).pack(pady=10)
        tk.Button(self.order_window, text="Back to Main Menu", command=self.back_to_main).pack(pady=10)

    def open_order_window(self):
        self.root.withdraw()
        self.order_window.deiconify()

    def back_to_main(self):
        self.order_window.withdraw()
        self.root.deiconify()

    def submit_order(self):
        juice_base = self.juice_base_var.get()
        supplement = self.supplement_var.get()
        size = self.size_var.get()

        # Validate input
        if not juice_base or not supplement or not size:
            messagebox.showerror("Input Error", "All fields must be filled.")
        else:
            messagebox.showinfo("Order Submitted", f"Order: {juice_base} juice with {supplement} (Size: {size})")

    def clear_selections(self):
        self.juice_base_var.set("")
        self.supplement_var.set("")
        self.size_var.set("")

    def view_orders(self):
        messagebox.showinfo("Orders", "No previous orders to display.")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = VitaminJuicesApp(root)
    root.mainloop()
