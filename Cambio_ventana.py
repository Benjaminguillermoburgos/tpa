import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QStackedWidget

class Ventana1(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.button = QPushButton('Ir a Ventana 2')
        layout.addWidget(self.button)
        self.setLayout(layout)
        self.button.clicked.connect(self.ir_a_ventana2)

    def ir_a_ventana2(self):
        stacked_widget.setCurrentIndex(1)  # Cambia al índice de la ventana 2


class Ventana2(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.button = QPushButton('Ir a Ventana 1')
        layout.addWidget(self.button)
        self.setLayout(layout)
        self.button.clicked.connect(self.ir_a_ventana1)

    def ir_a_ventana1(self):
        stacked_widget.setCurrentIndex(0)  # Cambia al índice de la ventana 1


if __name__ == '__main__':
    app = QApplication(sys.argv)

    stacked_widget = QStackedWidget()
    ventana1 = Ventana1()
    ventana2 = Ventana2()
    stacked_widget.addWidget(ventana1)
    stacked_widget.addWidget(ventana2)
    stacked_widget.show()

    sys.exit(app.exec())
