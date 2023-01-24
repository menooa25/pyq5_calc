import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QGridLayout, QLineEdit, QPushButton, QVBoxLayout, QWidget


class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        # Create a QLineEdit for the display
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignLeft)

        # Create the buttons
        self.button_1 = QPushButton("1")
        self.button_2 = QPushButton("2")
        self.button_3 = QPushButton("3")
        self.button_4 = QPushButton("4")
        self.button_5 = QPushButton("5")
        self.button_6 = QPushButton("6")
        self.button_7 = QPushButton("7")
        self.button_8 = QPushButton("8")
        self.button_9 = QPushButton("9")
        self.button_0 = QPushButton("0")
        self.button_add = QPushButton("+")
        self.button_sub = QPushButton("-")
        self.button_mul = QPushButton("*")
        self.button_div = QPushButton("/")
        self.button_eq = QPushButton("=")
        self.button_cl = QPushButton("Clear")

        # Add button clicks event to buttons
        self.button_1.clicked.connect(lambda: self.button_click(1))
        self.button_2.clicked.connect(lambda: self.button_click(2))
        self.button_3.clicked.connect(lambda: self.button_click(3))
        self.button_4.clicked.connect(lambda: self.button_click(4))
        self.button_5.clicked.connect(lambda: self.button_click(5))
        self.button_6.clicked.connect(lambda: self.button_click(6))
        self.button_7.clicked.connect(lambda: self.button_click(7))
        self.button_8.clicked.connect(lambda: self.button_click(8))
        self.button_9.clicked.connect(lambda: self.button_click(9))
        self.button_0.clicked.connect(lambda: self.button_click(0))
        self.button_add.clicked.connect(lambda: self.button_click("+"))
        self.button_sub.clicked.connect(lambda: self.button_click("-"))
        self.button_mul.clicked.connect(lambda: self.button_click("*"))
        self.button_div.clicked.connect(lambda: self.button_click("/"))
        self.button_eq.clicked.connect(self.calculate)
        self.button_cl.clicked.connect(self.clear)

        # Create a grid layout for the buttons
        grid = QGridLayout()
        grid.addWidget(self.button_1, 0, 0)
        grid.addWidget(self.button_2, 0, 1)
        grid.addWidget(self.button_3, 0, 2)
        grid.addWidget(self.button_4, 1, 0)
        grid.addWidget(self.button_5, 1, 1)
        grid.addWidget(self.button_6, 1, 2)
        grid.addWidget(self.button_7, 2, 0)
        grid.addWidget(self.button_8, 2, 1)
        grid.addWidget(self.button_9, 2, 2)
        grid.addWidget(self.button_0, 3, 1)
        grid.addWidget(self.button_add, 0, 3)
        grid.addWidget(self.button_sub, 1, 3)
        grid.addWidget(self.button_mul, 2, 3)
        grid.addWidget(self.button_div, 3, 3)
        grid.addWidget(self.button_eq, 3, 2)
        grid.addWidget(self.button_cl, 4, 0, 1, 4)

        # Create a vertical layout for the display and the buttons
        vbox = QVBoxLayout()
        vbox.addWidget(self.display)
        vbox.addLayout(grid)

        # Set the layout for the calculator
        self.setLayout(vbox)

    def button_click(self, number):
        """
        Handle button clicks
        """
        current = self.display.text()
        if current and current[-1] in "+-*/":
            if str(number) in "+-*/":
                return
        current += str(number)
        self.display.setText(current)

    def calculate(self):
        """
        Handle calculations
        """
        current = self.display.text()
        if current[-1] in "+-*/":
            current = current[:-1]
        try:
            result = eval(current)
            self.display.setText(str(result))
        except:
            self.display.setText("Error")

    def clear(self):
        """
        Handle clear button
        """
        self.display.clear()


app = QApplication(sys.argv)
calculator = Calculator()
calculator.show()
sys.exit(app.exec_())
