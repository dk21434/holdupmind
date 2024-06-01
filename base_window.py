from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QWidget, QApplication
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtCore import Qt

class BaseWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("HoldUpMind")
        self.setWindowIcon(QIcon("images/Screenshot 2024-05-25 171055.png"))
        self.setFixedSize(700, 1100) 

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        top = QWidget()
        top_layout = QVBoxLayout(top)
        top_layout.setContentsMargins(10, 10, 10, 10)

        name_label = QLabel("HoldUpMind")
        name_label.setFont(QFont("Arial", 20, QFont.Bold))
        name_label.setStyleSheet("color: #ff630f;")
        name_label.setContentsMargins(0, 30, 0, 0)

        top_layout.addWidget(name_label)
        top_layout.setAlignment(Qt.AlignLeft)

        self.main_layout.addWidget(top)

    def addContent(self, widget):
        self.main_layout.addWidget(widget)
