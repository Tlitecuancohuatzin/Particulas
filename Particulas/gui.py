# First_Package/gui.py

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from Particulas import *
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Aplicación de Ejemplo - First_Package")
        self.setGeometry(100, 100, 400, 200)
        
        # Layout
        layout = QVBoxLayout()
        
        # Etiqueta de instrucciones
        self.instruction_label = QLabel("Elige una función para ejecutar:")
        layout.addWidget(self.instruction_label)
        
        # Botón para example_function
        self.button1 = QPushButton("Llamar a example_function")
        self.button1.clicked.connect(self.call_example_function)
        layout.addWidget(self.button1)
        
        # Botón para another_function
        self.button2 = QPushButton("Llamar a another_function")
        self.button2.clicked.connect(self.call_another_function)
        layout.addWidget(self.button2)
        
        # Etiqueta para mostrar el resultado
        self.result_label = QLabel("")
        layout.addWidget(self.result_label)
        
        # Configurar el layout principal
        self.setLayout(layout)

    def call_example_function(self):
        # Llama a example_function y muestra el resultado
        result = particles.Electrón.info()
        self.result_label.setText(result)

    def call_another_function(self):
        # Llama a another_function y muestra el resultado
        result = particles.Antiup.info()
        self.result_label.setText(result)

def main():
    # Crear la aplicación y la ventana principal
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
