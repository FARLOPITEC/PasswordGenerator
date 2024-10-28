import os
import secrets
import string
import tkinter as tk
from tkinter import ttk, messagebox

# Function to clear the screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Password character sets
CAPITAL_LETTERS = string.ascii_uppercase
LOWERCASE_LETTERS = string.ascii_lowercase
NUMBERS = string.digits
CHARACTERS = string.punctuation
SPANISH_LETTERS = "áéíóúüñçÁÉÍÓÚÜÑÇ"
SPACES = " "

def PasswordGenerator(length, capitals, nums, chars, spanish, spaces):
    available_characters = LOWERCASE_LETTERS

    if capitals:
        available_characters += CAPITAL_LETTERS
    if nums:
        available_characters += NUMBERS
    if chars:
        available_characters += CHARACTERS
    if spanish:
        available_characters += SPANISH_LETTERS
    if spaces:
        available_characters += SPACES

    if not available_characters:
        messagebox.showerror("Error", "No se ha seleccionado ninguna opción.")
        return

    Password = ''.join(secrets.choice(available_characters) for _ in range(length))
    result_var.set(f"Contraseña generada: {Password}")

def generate_password():
    try:
        length = int(length_var.get())
        capitals = capitals_var.get()
        nums = nums_var.get()
        chars = chars_var.get()
        spanish = spanish_var.get()
        spaces = spaces_var.get()
        PasswordGenerator(length, capitals, nums, chars, spanish, spaces)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número válido para la longitud.")

def copy_to_clipboard():
    password = result_var.get().replace("Contraseña generada: ", "")
    root.clipboard_clear()
    root.clipboard_append(password)
    messagebox.showinfo("Información", "Contraseña copiada al portapapeles")

# Set up the main Tkinter window
root = tk.Tk()
root.title("Generador de Contraseñas")
root.geometry("400x400")

# Length input
length_frame = tk.Frame(root)
length_frame.pack(pady=5)
tk.Label(length_frame, text="Longitud de la contraseña:").pack(side=tk.LEFT, padx=5)
length_var = tk.IntVar(value=8)
length_spinner = ttk.Spinbox(length_frame, from_=1, to=100, textvariable=length_var, width=5)
length_spinner.pack(side=tk.LEFT, padx=5)

# Radiobuttons for password options
capitals_var = tk.BooleanVar()
nums_var = tk.BooleanVar()
chars_var = tk.BooleanVar()
spanish_var = tk.BooleanVar()
spaces_var = tk.BooleanVar()

options_frame = tk.Frame(root)
options_frame.pack(pady=5)

tk.Label(options_frame, text="Opciones de contraseña:").grid(row=0, columnspan=2, pady=5)
tk.Checkbutton(options_frame, text="Incluir mayúsculas", variable=capitals_var).grid(row=1, column=0, sticky="w")
tk.Checkbutton(options_frame, text="Incluir números", variable=nums_var).grid(row=2, column=0, sticky="w")
tk.Checkbutton(options_frame, text="Incluir caracteres especiales", variable=chars_var).grid(row=3, column=0, sticky="w")
tk.Checkbutton(options_frame, text="Incluir letras españolas", variable=spanish_var).grid(row=4, column=0, sticky="w")
tk.Checkbutton(options_frame, text="Incluir espacios", variable=spaces_var).grid(row=5, column=0, sticky="w")

# Button to generate password
tk.Button(root, text="Generar Contraseña", command=generate_password).pack(pady=5)

# Text widget to display the generated password
result_var = tk.StringVar()
tk.Label(root, textvariable=result_var).pack(pady=5)

# Button to copy password to clipboard
tk.Button(root, text="Copiar Contraseña", command=copy_to_clipboard).pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
