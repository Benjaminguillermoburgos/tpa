import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QTableWidget

class RestaurantInventory(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Inventario del Restaurante')
    
        # Crear una tabla para mostrar el inventario
        self.table = QTableWidget(self)
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['Plato', 'Cantidad'])
        
        # Agregar los platos al inventario
        self.add_dish('Pizza', 10)
        self.add_dish('Hamburguesa', 15)
        self.add_dish('Sushi', 8)
        self.add_dish('Pasta', 12)
        self.add_dish('Ensalada', 5)
        # Agrega más platos si lo deseas
        
        # Ajustar el tamaño de las columnas para que se ajusten al contenido
        self.table.resizeColumnsToContents()
        
        # Agregar la tabla al layout principal
        self.setCentralWidget(self.table)
    
    def add_dish(self, dish_name, quantity):
        # Obtener el número de filas actual en la tabla
        row_count = self.table.rowCount()
        
        # Insertar una nueva fila en la tabla
        self.table.insertRow(row_count)
        
        # Agregar el nombre del plato a la celda de la primera columna
        dish_item = QTableWidgetItem(dish_name)
        self.table.setItem(row_count, 0, dish_item)
        
        # Agregar la cantidad del plato a la celda de la segunda columna
        quantity_item = QTableWidgetItem(str(quantity))
        self.table.setItem(row_count, 1, quantity_item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RestaurantInventory()
    window.show()
    sys.exit(app.exec_())
