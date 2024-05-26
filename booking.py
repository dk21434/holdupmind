from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QDateEdit, QTimeEdit, QCheckBox, QWidget, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QFont
from base_window import BaseWindow

class ScreenBooking(BaseWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #3E721D;")

        content_widget = QWidget()
        layout = QVBoxLayout(content_widget)

        subtitle = QLabel("Book Your Appointment")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setFont(QFont('Arial', 18))
        subtitle.setStyleSheet("color: white;")

        layout.addWidget(subtitle)

        layout.addItem(QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        date_time_layout = QVBoxLayout()

        date_row = QHBoxLayout()
        date_label = QLabel("Choose Date:")
        date_label.setFont(QFont('Arial', 14))
        date_label.setStyleSheet("color: white;")
        date_edit = QDateEdit()
        date_edit.setCalendarPopup(True)
        date_edit.setDate(QDate.currentDate())
        date_edit.setStyleSheet("background-color: white; font-size: 17px; padding: 10px;")
        date_edit.setFont(QFont('Arial', 16))
        date_row.addWidget(date_label)
        date_row.addWidget(date_edit)

        time_row = QHBoxLayout()
        time_label = QLabel("Choose Time:")
        time_label.setFont(QFont('Arial', 14))
        time_label.setStyleSheet("color: white;")
        time_edit = QTimeEdit()
        time_edit.setStyleSheet("background-color: white; font-size: 17px; padding: 10px;")
        time_edit.setFont(QFont('Arial', 16)) 
        time_row.addWidget(time_label)
        time_row.addWidget(time_edit)

        date_time_layout.addLayout(date_row)
        date_time_layout.addItem(QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Fixed))
        date_time_layout.addLayout(time_row)
        layout.addLayout(date_time_layout)

        layout.addItem(QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        session_checkbox = QCheckBox("Session With Your Therapist")
        session_checkbox.setStyleSheet("color: white; font-size: 23px;")
        layout.addWidget(session_checkbox, alignment=Qt.AlignCenter)


        book_button = QPushButton("Book It!")
        book_button.setStyleSheet("background-color: #FFFFFF; color: black; font-size: 18px; padding: 20px; border-radius: 20px;")
        layout.addWidget(book_button, alignment=Qt.AlignCenter)

        layout.addItem(QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.addContent(content_widget)

if __name__ == '__main__':
    app = QApplication([])
    window = ScreenBooking()
    window.show()
    app.exec_()
