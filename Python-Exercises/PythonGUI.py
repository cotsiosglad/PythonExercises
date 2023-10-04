import tkinter as tk

def button_click(button_num):
    label.config(text=f"Button {button_num} clicked!")

window = tk.Tk()
window.title("Stylish Buttons")

# Create a custom style for buttons
button_style = {"bg": "lightblue", "fg": "black", "font": ("Helvetica", 12)}

button1 = tk.Button(window, text="Button 1", command=lambda: button_click(1), **button_style)
button2 = tk.Button(window, text="Button 2", command=lambda: button_click(2), **button_style)
button3 = tk.Button(window, text="Button 3", command=lambda: button_click(3), **button_style)

label = tk.Label(window, text="Click a button!", font=("Helvetica", 14))

label.pack(pady=10)
button1.pack(padx=10, pady=5)
button2.pack(padx=10, pady=5)
button3.pack(padx=10, pady=5)

window.mainloop()
