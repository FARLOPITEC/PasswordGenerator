import os
import time
import secrets
import string

# Función para limpiar la pantalla
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Caracteres disponibles para la generación de contraseñas
CAPITAL_LETTERS = string.ascii_uppercase
LOWERCASE_LETTERS = string.ascii_lowercase
NUMBERS = string.digits
CHARACTERS = string.punctuation
SPANISH_LETTERS = "áéíóúüñçÁÉÍÓÚÜÑÇ"
SPACES = " "

def Quiz():
    LengthPass = int(input("Longitud de la contraseña: "))

    capital_letters = input("¿Incluir mayúsculas? [Y/N]: ").strip().lower() in ['y', 's']   #true si se escribe 'y' o 's
    numbers = input("¿Incluir números? [Y/N]: ").strip().lower() in ['y', 's']
    characters = input("¿Incluir caracteres especiales? [Y/N]: ").strip().lower() in ['y', 's']
    
    spanish_letters = input("¿Incluir letras españolas? [Y/N]: ").strip().lower() in ['y', 's']
    if spanish_letters:
        spanish_letters_confirm = input("Es posible que no sean aceptadas por algunos servicios, ¿estás seguro? [Y/N]: ").strip().lower() in ['y', 's']
        spanish_letters = spanish_letters_confirm

    spaces = input("¿Incluir espacios? [Y/N]: ").strip().lower() in ['y', 's']
    if spaces:
        spaces_confirm = input("Es posible que no sean aceptadas por algunos servicios, ¿estás seguro? [Y/N]: ").strip().lower() in ['y', 's']
        spaces = spaces_confirm

    return LengthPass, capital_letters, numbers, characters, spanish_letters, spaces

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
        print("No se ha seleccionado ninguna opción.")
        exit(1)

    Password = ''.join(secrets.choice(available_characters) for _ in range(length))
    print(f"Contraseña generada: {Password}")

def main():
    length, capitals, nums, chars, spanish, spaces = Quiz()
    PasswordGenerator(length, capitals, nums, chars, spanish, spaces)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:   # Ctrl + C
        print("\nInterrupción del usuario.")
        print("Saliendo...")
        time.sleep(1)
        clear()
        exit(0)
    except Exception as e: # Control de errores
        print(f"Error: {e}")
        print("Saliendo...")
        time.sleep(1)
        clear()
        exit(1)
