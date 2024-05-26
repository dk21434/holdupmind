from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from base_window import BaseWindow

class ScreenMain(BaseWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #3E721D;")
        self.initContent()

    def initContent(self):
        content_widget = QWidget()
        layout = QVBoxLayout(content_widget)

        subtitle = QLabel("Ready for your next Therapy?")
        subtitle.setAlignment(Qt.AlignLeft)
        subtitle.setFont(QFont('Arial', 14))
        subtitle.setStyleSheet("color: white;")

        subtitle1 = QLabel("Book your Appointment here!")
        subtitle1.setAlignment(Qt.AlignCenter)
        subtitle1.setFont(QFont('Arial', 16))
        subtitle1.setStyleSheet("color: white;")

        pick_therapist_btn = QPushButton("Pick a Therapist")
        pick_therapist_btn.setStyleSheet("background-color: #FFFFFF; color: black; font-size: 18px; padding: 20px; border-radius: 20px;")
        your_progress_btn = QPushButton("Your Progress")
        your_progress_btn.setStyleSheet("background-color: #FFFFFF; color: black; font-size: 18px; padding: 20px; border-radius: 20px;")

        button_layout = QHBoxLayout()
        button_layout.addWidget(pick_therapist_btn)
        button_layout.addWidget(your_progress_btn)
        button_layout.setSpacing(20)

        layout.addStretch()
        layout.addWidget(subtitle)
        layout.addStretch()
        layout.addWidget(subtitle1)
        layout.addStretch()
        layout.addLayout(button_layout)
        layout.addStretch()

        self.addContent(content_widget)

if __name__ == "__main__":
    app = QApplication([])
    main_screen = ScreenMain()
    main_screen.show()
    app.exec_()