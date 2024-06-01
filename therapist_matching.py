from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QComboBox, QTextEdit, QWidget, QSpacerItem, QSizePolicy, QMessageBox
from PyQt5.QtGui import QFont
from base_window import BaseWindow
import json

class TherapistMatching(BaseWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #3E721D;")

        self.therapists = self.load_therapists()

        content_widget = QWidget()
        layout = QVBoxLayout(content_widget)

        self.subtitle = QLabel("Find a Therapist")
        self.subtitle.setAlignment(Qt.AlignCenter)
        self.subtitle.setFont(QFont('Arial', 18))
        self.subtitle.setStyleSheet("color: white;")

        layout.addWidget(self.subtitle)

        layout.addItem(QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        matching_layout = QVBoxLayout()

        language_row = QHBoxLayout()
        language_label = QLabel("Language:")
        language_label.setFont(QFont('Arial', 14))
        language_label.setStyleSheet("color: white;")
        self.language_combo = QComboBox()
        self.language_combo.addItems(["English", "Spanish", "French"])
        self.language_combo.setStyleSheet("background-color: white; font-size: 14px; padding: 5px;")
        self.language_combo.setFont(QFont('Arial', 16))
        language_row.addWidget(language_label)
        language_row.addWidget(self.language_combo)
        
        specialty_row = QHBoxLayout()
        specialty_label = QLabel("Specialty:")
        specialty_label.setFont(QFont('Arial', 14))
        specialty_label.setStyleSheet("color: white;")
        self.specialty_combo = QComboBox()
        self.specialty_combo.addItems(["Anxiety", "Depression", "Family Therapy"])
        self.specialty_combo.setStyleSheet("background-color: white; font-size: 14px; padding: 5px;")
        self.specialty_combo.setFont(QFont('Arial', 16))
        specialty_row.addWidget(specialty_label)
        specialty_row.addWidget(self.specialty_combo)
        
        therapy_type_row = QHBoxLayout()
        therapy_type_label = QLabel("Therapy Type:")
        therapy_type_label.setFont(QFont('Arial', 14))
        therapy_type_label.setStyleSheet("color: white;")
        therapy_type_combo = QComboBox()
        therapy_type_combo.addItems(["Cognitive", "Behavioral", "Humanistic"])
        therapy_type_combo.setStyleSheet("background-color: white; font-size: 14px; padding: 5px;")
        therapy_type_combo.setFont(QFont('Arial', 16))
        therapy_type_row.addWidget(therapy_type_label)
        therapy_type_row.addWidget(therapy_type_combo)

        gender_row = QHBoxLayout()
        gender_label = QLabel("Therapist Gender:")
        gender_label.setFont(QFont('Arial', 14))
        gender_label.setStyleSheet("color: white;")
        gender_combo = QComboBox()
        gender_combo.addItems(["Male", "Female", "Any"])
        gender_combo.setStyleSheet("background-color: white; font-size: 14px; padding: 5px;")
        gender_combo.setFont(QFont('Arial', 16))
        gender_row.addWidget(gender_label)
        gender_row.addWidget(gender_combo)
        
        date_row = QHBoxLayout()
        date_label = QLabel("Date:")
        date_label.setFont(QFont('Arial', 14))
        date_label.setStyleSheet("color: white;")
        date_combo = QComboBox()
        date_combo.addItems(["Today", "Tomorrow", "Next Week"])
        date_combo.setStyleSheet("background-color: white; font-size: 14px; padding: 5px;")
        date_combo.setFont(QFont('Arial', 16))
        date_row.addWidget(date_label)
        date_row.addWidget(date_combo)
        
        time_row = QHBoxLayout()
        time_label = QLabel("Time:")
        time_label.setFont(QFont('Arial', 14))
        time_label.setStyleSheet("color: white;")
        time_combo = QComboBox()
        time_combo.addItems(["Morning", "Afternoon", "Evening"])
        time_combo.setStyleSheet("background-color: white; font-size: 14px; padding: 5px;")
        time_combo.setFont(QFont('Arial', 16))
        time_row.addWidget(time_label)
        time_row.addWidget(time_combo)

        matching_layout.addLayout(language_row)
        matching_layout.addLayout(specialty_row)
        matching_layout.addLayout(therapy_type_row)
        matching_layout.addLayout(gender_row)
        matching_layout.addLayout(date_row)
        matching_layout.addLayout(time_row)

        layout.addLayout(matching_layout)

        layout.addItem(QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        find_button = QPushButton("Find Therapist!")
        find_button.setStyleSheet("background-color: #FFFFFF; color: black; font-size: 18px; padding: 20px; border-radius: 20px;")
        find_button.clicked.connect(self.find_therapist)
        layout.addWidget(find_button, alignment=Qt.AlignCenter)

        layout.addItem(QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.addContent(content_widget)

    def load_therapists(self):
        # Load therapist data from JSON
        with open('therapists.json', 'r') as file:
            return json.load(file)

    def find_therapist(self):
        # Fetch selected values
        language = self.language_combo.currentText()
        specialty = self.specialty_combo.currentText()

        # Filter therapists based on language and specialty
        matches = [t for t in self.therapists if t['language'] == language and t['specialty'] == specialty]

        # Display results or an error message
        if matches:
            info = "\n\n".join([f"Name: {t['name']}, Experience: {t['experience']}, Reviews: {t['reviews']}" for t in matches])
            QMessageBox.information(self, "Matching Therapists", info)
        else:
            QMessageBox.warning(self, "No Matches", "No therapists found matching your criteria.")



if __name__ == '__main__':
    app = QApplication([])
    window = TherapistMatching()
    window.show()
    app.exec_()
