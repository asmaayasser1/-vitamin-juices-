def submit_order(self):
    juice_base = self.juice_base_entry.get()
    supplements = self.supplements_entry.get()
    size = self.size_entry.get()

    if not juice_base or not supplements or not size:
        messagebox.showerror("Input Error", "All fields must be filled out!")
    elif not size.isdigit():  
        messagebox.showerror("Input Error", "Size must be a number!")
    else:
        messagebox.showinfo("Order Submitted", f"Juice Order: {juice_base}, Supplements: {supplements}, Size: {size} oz")
        self.clear_selections()
