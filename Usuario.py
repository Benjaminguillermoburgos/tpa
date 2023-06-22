import csv

def verificar_credenciales(correo, contraseña):
    with open('datos_usuarios.csv', 'r') as archivo_csv:
        datos_usuarios = csv.reader(archivo_csv)
        for fila in datos_usuarios:
            if fila[0] == correo and fila[1] == contraseña:
                return True
    return False

def iniciar_sesion():
    correo = input("Ingrese su correo electrónico: ")
    contraseña = input("Ingrese su contraseña: ")
    if verificar_credenciales(correo, contraseña):
        print("Inicio de sesión exitoso.")
    else:
        print("Credenciales inválidas.")

iniciar_sesion()
