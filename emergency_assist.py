from PyQt5.QtCore import Qt, QDateTime
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QVBoxLayout,QHBoxLayout, QWidget, QLabel, QPushButton, QComboBox, QApplication, QSpacerItem, QSizePolicy, QMessageBox
from base_window import BaseWindow
import json

class EmergencyAssistance(BaseWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #3E721D;")

        self.therapists = self.load_therapists()

        content_widget = QWidget()
        layout = QVBoxLayout(content_widget)

        subtitle = QLabel("Emergency Assistance")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setFont(QFont('Arial', 18))
        subtitle.setStyleSheet("color: white;")

        layout.addWidget(subtitle)

        layout.addItem(QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        therapist_layout = QVBoxLayout()

        therapist_label = QLabel("Choose Therapist:")
        therapist_label.setFont(QFont('Arial', 14))
        therapist_label.setStyleSheet("color: white; margin-left: 20px;")
        therapist_layout.addWidget(therapist_label, alignment=Qt.AlignLeft)

        combo_row = QHBoxLayout()
        combo_row.addStretch()

        therapist_combo = QComboBox()
        therapist_combo.setStyleSheet("""
            background-color: white; 
            font-size: 17px; 
            padding: 15px; 
            border: 1px solid #3E721D;
            border-radius: 10px;
        """)
        therapist_combo.setFont(QFont('Arial', 16))
        # therapist_combo.setFixedWidth(300)
        therapist_combo.addItems([therapist['name'] for therapist in self.therapists])
        therapist_layout.addWidget(therapist_combo)

        layout.addLayout(therapist_layout)

        layout.addItem(QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        confirm_button = QPushButton("Confirm Appointment")
        confirm_button.setStyleSheet("background-color: #FFFFFF; color: black; font-size: 18px; padding: 20px; border-radius: 20px;")
        confirm_button.clicked.connect(lambda: self.confirm_appointment(therapist_combo.currentText()))
        layout.addWidget(confirm_button, alignment=Qt.AlignCenter)

        layout.addItem(QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.addContent(content_widget)

    def load_therapists(self):
        with open('therapists.json', 'r') as file:
            return json.load(file)

    def confirm_appointment(self, therapist_name):
        current_datetime = QDateTime.currentDateTime().toString(Qt.DefaultLocaleLongDate)
        message = f"Therapist: {therapist_name}\nAppointment Time: {current_datetime}\n"
        message_box = QMessageBox(self)
        message_box.setWindowTitle("Appointment Confirmation")
        message_box.setText(message)
        message_box.setStandardButtons(QMessageBox.Ok)
        message_box.addButton("Start Meeting", QMessageBox.AcceptRole)
        message_box.exec_()

if __name__ == '__main__':
    app = QApplication([])
    window = EmergencyAssistance()
    window.show()
    app.exec_()
