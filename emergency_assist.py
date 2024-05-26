from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QVBoxLayout,QHBoxLayout, QWidget, QLabel, QPushButton, QComboBox, QApplication, QSpacerItem, QSizePolicy
from base_window import BaseWindow

class EmergencyAssistance(BaseWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #3E721D;")

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
        therapist_combo.addItems(["Dr. Jane Smith", "Dr. John Doe", "Dr. Emily Johnson"])
        therapist_combo.setStyleSheet("""
            background-color: white; 
            font-size: 17px; 
            padding: 15px; 
            border: 1px solid #3E721D;
            border-radius: 10px;
            min-width: 300px;  /* Adjust the width as needed */
        """)
        therapist_combo.setFont(QFont('Arial', 16))
        combo_row.addWidget(therapist_combo)
        combo_row.addStretch()

        therapist_layout.addItem(QSpacerItem(0, 10, QSizePolicy.Minimum, QSizePolicy.Fixed))
        therapist_layout.addLayout(combo_row)

        layout.addLayout(therapist_layout)

        layout.addItem(QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        confirm_button = QPushButton("Confirm Appointment")
        confirm_button.setStyleSheet("background-color: #FFFFFF; color: black; font-size: 18px; padding: 20px; border-radius: 20px;")
        layout.addWidget(confirm_button, alignment=Qt.AlignCenter)

        layout.addItem(QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.addContent(content_widget)

if __name__ == '__main__':
    app = QApplication([])
    window = EmergencyAssistance()
    window.show()
    app.exec_()
