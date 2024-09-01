import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MacOS Calculator")
        self.setFixedSize(300, 400)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
                border-radius: 10px;
            }
            QLineEdit {
                background-color: white;
                border: 1px solid #ccc;
                border-radius: 5px;
                color: #333;
                font-size: 36px;
                padding: 5px;
            }
            QPushButton {
                background-color: #e0e0e0;
                border: none;
                border-radius: 20px;
                padding: 15px;
                color: #333;
                font-size: 18px;
            }
            QPushButton:hover {
                background-color: #d0d0d0;
            }
            QPushButton:pressed {
                background-color: #c0c0c0;
            }
        """)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setSpacing(10)
        self.layout.setContentsMargins(20, 20, 20, 20)

        self.setup_ui()

    def setup_ui(self):
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.layout.addWidget(self.display)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=']
        ]

        for row in buttons:
            h_layout = QHBoxLayout()
            for button in row:
                btn = QPushButton(button)
                btn.clicked.connect(self.on_button_click)
                h_layout.addWidget(btn)
            self.layout.addLayout(h_layout)

    def on_button_click(self):
        button = self.sender()
        key = button.text()

        if key == '=':
            try:
                result = eval(self.display.text())
                self.display.setText(str(result))
            except:
                self.display.setText("Error")
        elif key == 'C':
            self.display.clear()
        else:
            self.display.setText(self.display.text() + key)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = CalculatorApp()
    calculator.show()
    sys.exit(app.exec())

