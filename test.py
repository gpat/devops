import tkinter as tk

def on_button_click():
    label.config(text="Button Clicked!")

# Create the main window
app = tk.Tk()
app.title("Test Application")

# Create a button
button = tk.Button(app, text="Click me!", command=on_button_click)

# Create a label
label = tk.Label(app, text="Welcome to the Test Application")

# Pack the button and label into the window
button.pack(pady=10)
label.pack(pady=10)

# Start the application loop
app.mainloop()
