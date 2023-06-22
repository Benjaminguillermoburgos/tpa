import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton

#Ventana de inicio de sesion

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inicio de Sesión")
        self.setGeometry(100, 100, 300, 200)

        self.username_label = QLabel("Usuario:", self)
        self.username_label.move(50, 50)
        self.username_input = QLineEdit(self)
        self.username_input.move(120, 50)

        self.password_label = QLabel("Contraseña:", self)
        self.password_label.move(50, 80)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.move(120, 80)

        self.login_button = QPushButton("Iniciar Sesión", self)
        self.login_button.move(120, 120)
        self.login_button.clicked.connect(self.login)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

# Aquí puedes agregar la lógica de validación del usuario y contraseña
# Puedes realizar consultas a una base de datos o usar algún otro método de autenticación

        if username == "admin" and password == "12345":
            print("Inicio de sesión exitoso.")
# Aquí puedes abrir la ventana principal de la aplicación o realizar otras acciones
        else:
            print("Inicio de sesión fallido.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
