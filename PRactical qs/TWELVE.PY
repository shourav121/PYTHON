import tkinter as tk
from tkinter import messagebox

# Prices
PRICES = {
    "Burger": 50,
    "Fries": 30,
    "Drinks": 20
}

# Function to calculate total
def calculate_total():
    try:
        burger_qty = int(burger_entry.get() or 0)
        fries_qty = int(fries_entry.get() or 0)
        drinks_qty = int(drinks_entry.get() or 0)

        total = (burger_qty * PRICES["Burger"] +
                 fries_qty * PRICES["Fries"] +
                 drinks_qty * PRICES["Drinks"])

        total_var.set(f"₹ {total}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Function to clear all fields
def reset_fields():
    burger_entry.delete(0, tk.END)
    fries_entry.delete(0, tk.END)
    drinks_entry.delete(0, tk.END)
    total_var.set("₹ 0")

# Function to show receipt
def generate_receipt():
    try:
        burger_qty = int(burger_entry.get() or 0)
        fries_qty = int(fries_entry.get() or 0)
        drinks_qty = int(drinks_entry.get() or 0)
        total = (burger_qty * PRICES["Burger"] +
                 fries_qty * PRICES["Fries"] +
                 drinks_qty * PRICES["Drinks"])

        receipt = (
            f"----- Receipt -----\n"
            f"Burger x {burger_qty} = ₹{burger_qty * PRICES['Burger']}\n"
            f"Fries x {fries_qty} = ₹{fries_qty * PRICES['Fries']}\n"
            f"Drinks x {drinks_qty} = ₹{drinks_qty * PRICES['Drinks']}\n"
            f"--------------------\n"
            f"Total: ₹{total}"
        )

        messagebox.showinfo("Receipt", receipt)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# GUI setup
root = tk.Tk()
root.title("Restaurant Management System")
root.geometry("350x400")
root.resizable(False, False)

# Title
tk.Label(root, text="Restaurant Billing", font=("Arial", 18, "bold")).pack(pady=10)

# Input Fields
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Burger (₹50)").grid(row=0, column=0, padx=10, pady=5, sticky='w')
burger_entry = tk.Entry(frame)
burger_entry.grid(row=0, column=1)

tk.Label(frame, text="Fries (₹30)").grid(row=1, column=0, padx=10, pady=5, sticky='w')
fries_entry = tk.Entry(frame)
fries_entry.grid(row=1, column=1)

tk.Label(frame, text="Drinks (₹20)").grid(row=2, column=0, padx=10, pady=5, sticky='w')
drinks_entry = tk.Entry(frame)
drinks_entry.grid(row=2, column=1)

# Total Display
tk.Label(root, text="Total", font=("Arial", 14)).pack()
total_var = tk.StringVar(value="₹ 0")
tk.Label(root, textvariable=total_var, font=("Arial", 16, "bold"), fg="green").pack()

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=15)

tk.Button(btn_frame, text="Calculate Total", command=calculate_total, width=15).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Generate Receipt", command=generate_receipt, width=15).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Reset", command=reset_fields, width=32).grid(row=1, columnspan=2, pady=10)

# Run the app
root.mainloop()
