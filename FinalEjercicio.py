

def contraseñavalidacion(passowrd):
    Mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Minusculas = "abcdefghijklmnopqrstuvwxyz"
    Numeros = "0123456789"
    Caracteres_especiales = "!@#$%^&*()_+-=[]{},.<>/?"
    
    comunes = ["password", "123456", "admin", "qwerty", "letmein"]
    if comunes.__contains__(passowrd):
        return "Contraseña Facil"
    elif len(passowrd) < 8:
        return "Contraseña Muy Corta"
    elif not any(char in Mayusculas for char in passowrd):
        return "Falta una Mayuscula"
    elif not any(char in Minusculas for char in passowrd):
        return "Falta una Minuscula"
    elif not any(char in Numeros for char in passowrd):
        return "Falta un Numero"
    elif not any(char in Caracteres_especiales for char in passowrd):
        return "Falta un Caracter Especial"
    else:
        return "Contraseña Segura\nPass"




def main():
    contraseña = input("ingrese la contraseña: ")
    print(contraseñavalidacion(contraseña))
main()
