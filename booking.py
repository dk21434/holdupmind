from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QDateEdit, QTimeEdit, QCheckBox, QWidget, QSpacerItem, QSizePolicy, QMessageBox
from PyQt5.QtGui import QFont
from base_window import BaseWindow
import json

class ScreenBooking(BaseWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #3E721D;")

        content_widget = QWidget()
        layout = QVBoxLayout(content_widget)

        self.subtitle = QLabel("Book Your Appointment")
        self.subtitle.setAlignment(Qt.AlignCenter)
        self.subtitle.setFont(QFont('Arial', 18))
        self.subtitle.setStyleSheet("color: white;")

        layout.addWidget(self.subtitle)

        layout.addItem(QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        date_time_layout = QVBoxLayout()

        date_row = QHBoxLayout()
        self.date_label = QLabel("Choose Date:")
        self.date_label.setFont(QFont('Arial', 14))
        self.date_label.setStyleSheet("color: white;")
        self.date_edit = QDateEdit()
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setDate(QDate.currentDate())
        self.date_edit.setStyleSheet("background-color: white; font-size: 17px; padding: 10px;")
        self.date_edit.setFont(QFont('Arial', 16))
        date_row.addWidget(self.date_label)
        date_row.addWidget(self.date_edit)

        time_row = QHBoxLayout()
        self.time_label = QLabel("Choose Time:")
        self.time_label.setFont(QFont('Arial', 14))
        self.time_label.setStyleSheet("color: white;")
        self.time_edit = QTimeEdit()
        self.time_edit.setStyleSheet("background-color: white; font-size: 17px; padding: 10px;")
        self.time_edit.setFont(QFont('Arial', 16)) 
        time_row.addWidget(self.time_label)
        time_row.addWidget(self.time_edit)

        date_time_layout.addLayout(date_row)
        date_time_layout.addItem(QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Fixed))
        date_time_layout.addLayout(time_row)
        layout.addLayout(date_time_layout)

        layout.addItem(QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.session_checkbox = QCheckBox("Session With Your Therapist")
        self.session_checkbox.setStyleSheet("color: white; font-size: 23px;")
        layout.addWidget(self.session_checkbox, alignment=Qt.AlignCenter)


        self.book_button = QPushButton("Book It!")
        self.book_button.setStyleSheet("background-color: #FFFFFF; color: black; font-size: 18px; padding: 20px; border-radius: 20px;")
        self.book_button.clicked.connect(self.book_appointment)
        layout.addWidget(self.book_button, alignment=Qt.AlignCenter)

        layout.addItem(QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.addContent(content_widget)

    def book_appointment(self):
        if not self.session_checkbox.isChecked():
            QMessageBox.warning(self, 'Session Required', 'You have to choose a therapist.')
            # Potentially open the therapist matching screen
            from therapist_matching import TherapistMatching
            self.setCentralWidget(TherapistMatching())
            return
        
        appointment_data = {
            'date': self.date_edit.date().toString("yyyy-MM-dd"),
            'time': self.time_edit.time().toString("HH:mm:ss")
        }
        with open('appointments.json', 'w') as f:
            json.dump(appointment_data, f, indent=4)
        QMessageBox.information(self, 'Booking Confirmed', 'Your appointment has been booked.')

    
if __name__ == '__main__':
    app = QApplication([])
    window = ScreenBooking()
    window.show()
    app.exec_()
