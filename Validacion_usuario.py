def validar_usuario_contrasena(usuario, contrasena):
# Comprobar si el usuario y la contraseña cumplen con los requisitos
    if len(usuario) < 5 or len(contrasena) < 8:
        return False

# Comprobar si el usuario contiene solo caracteres alfanuméricos
    if not usuario.isalnum():
        return False

# Comprobar si la contraseña contiene al menos una letra mayúscula, una letra minúscula y un dígito
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_digito = False

    for caracter in contrasena:
        if caracter.isupper():
            tiene_mayuscula = True
        elif caracter.islower():
            tiene_minuscula = True
        elif caracter.isdigit():
            tiene_digito = True

    if not (tiene_mayuscula and tiene_minuscula and tiene_digito):
        return False

# Si todas las comprobaciones pasan, se considera válido
    return True

# Ejemplo de uso
usuario = input("Ingrese su nombre de usuario: ")
contrasena = input("Ingrese su contraseña: ")

if validar_usuario_contrasena(usuario, contrasena):
    print("¡Usuario y contraseña válidos!")
else:
    print("Usuario y/o contraseña inválidos.")
