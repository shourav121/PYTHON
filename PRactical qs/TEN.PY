import tkinter as tk

# Function to evaluate the expression
def calculate():
    try:
        result = eval(entry.get())
        output_label.config(text=f"Result: {result}")
    except Exception as e:
        output_label.config(text="Error!")

# Function to clear the entry
def clear():
    entry.delete(0, tk.END)
    output_label.config(text="Result:")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x250")
root.resizable(False, False)

# Entry field
entry = tk.Entry(root, font=("Arial", 16), justify='right')
entry.pack(pady=10, padx=10, fill='x')

# Result label
output_label = tk.Label(root, text="Result:", font=("Arial", 14))
output_label.pack(pady=5)

# Buttons frame
buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=10)

# Define button values
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+')
]

# Add buttons to the frame
for row in buttons:
    row_frame = tk.Frame(buttons_frame)
    row_frame.pack(side='top', fill='x')
    for char in row:
        if char == '=':
            btn = tk.Button(row_frame, text=char, width=5, font=("Arial", 12), command=calculate)
        else:
            btn = tk.Button(row_frame, text=char, width=5, font=("Arial", 12),
                            command=lambda ch=char: entry.insert(tk.END, ch))
        btn.pack(side='left', padx=2, pady=2)

# Clear button
clear_btn = tk.Button(root, text="Clear", font=("Arial", 12), command=clear)
clear_btn.pack(pady=5)

# Run the app
root.mainloop()
