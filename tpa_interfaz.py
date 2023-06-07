import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton

# Creamos una clase que herede de QWidget para nuestra interfaz
class MiVentana(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Creamos los componentes de la interfaz
        etiqueta = QLabel('¡Hola, mundo!')
        boton = QPushButton('Haz clic')

        # Creamos un layout vertical y agregamos los componentes
        layout = QVBoxLayout()
        layout.addWidget(etiqueta)
        layout.addWidget(boton)

        # Configuramos el layout en la ventana principal
        self.setLayout(layout)

        # Configuramos el título y el tamaño de la ventana
        self.setWindowTitle('Mi Ventana')
        self.setGeometry(100, 100, 200, 200)

        # Conectamos una función al evento clic del botón
        boton.clicked.connect(self.mostrar_mensaje)

        # Mostramos la ventana
        self.show()

    def mostrar_mensaje(self):
        print('¡Se hizo clic en el botón!')

# Creamos la aplicación de PyQt
app = QApplication(sys.argv)

# Creamos una instancia de nuestra ventana personalizada
ventana = MiVentana()

# Iniciamos el bucle de eventos de la aplicación
sys.exit(app.exec_())