import sys

from PyQt6.QtCore import (
    QSize,
    Qt,
)
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QWidget,
    QFormLayout,
    QLineEdit,
    QPushButton,
)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Project-Yellow")
        button = QPushButton("Push Me")
        self.setFixedSize(QSize(400, 300))
        self.setCentralWidget(button)


app = QApplication(sys.argv)

window = MainWindow()

# window = QWidget()
# window.setWindowTitle("Project-Yellow")
# window.setGeometry(100, 100, 280, 80)

# layout = QFormLayout()
# layout.addRow("Vechicle No.", QLineEdit())
# layout.addRow("Owner Name", QLineEdit())
# layout.addRow("Phone No.", QLineEdit())
# layout.addRow("Vechile Name", QLineEdit())
# layout.addRow("Fuel", QLineEdit())
# layout.addRow("Expiry", QLineEdit())
# window.setLayout(layout)

window.show()
sys.exit(app.exec())

"""
Buttons = QPushButton
Label = QLabel
    Can accept html elements to modify apperance
    A lot of customization is possible
LineEdit/Input boxes = QLineEdit
    Automatically provide basic editing operations like copy, paste, undo,
    redo, drag, drop and so on.
    Can show placeholder
ComboBox/DropDown = QComboBox
    Is Read-only which means that users can select one of several options
    but can't add their own options
    Can also be editable, allowing users to add new option on the fly.
RadioButton = QRadioButton
Date = QDateEdit
Time = QTimeEdit
QGroupBox  Check it out

"""
