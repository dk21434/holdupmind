from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLabel, QPushButton, QTextEdit, QApplication, QScrollArea, QLineEdit
from base_window import BaseWindow

class PersonalizedQuestionnaires(BaseWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #3E721D;")
        self.initContent()

    def initContent(self):
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)

        subtitle = QLabel("Personalized Questionnaire")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setFont(QFont('Arial', 18))
        subtitle.setStyleSheet("color: white;")
        content_layout.addWidget(subtitle)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setStyleSheet("QScrollArea { border: none; }")
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)

        questions = [
            "How are you feeling today?",
            "What is your primary reason for seeking therapy?",
            "Have you had therapy before?",
            "What are your therapy goals?",
            "Are you experiencing any current stressors?",
            "Do you have a support system?",
            "How do you usually cope with stress?",
            "What is your preferred type of therapy?",
            "How often would you like to attend therapy sessions?",
            "Is there anything else you would like your therapist to know?"
        ]

        for question in questions:
            question_row = QVBoxLayout()

            question_label = QLabel(question)
            question_label.setFont(QFont('Arial', 14))
            question_label.setStyleSheet("color: black;")
            question_label.setWordWrap(True)

            answer_input = QLineEdit()
            answer_input.setStyleSheet("background-color: #c4bbb7; font-size: 14px; padding: 5px;")

            question_row.addWidget(question_label)
            question_row.addWidget(answer_input)

            scroll_layout.addLayout(question_row)
            scroll_layout.addSpacing(10)

        scroll_content.setLayout(scroll_layout)
        scroll_area.setWidget(scroll_content)
        content_layout.addWidget(scroll_area)

        self.addContent(content_widget)

if __name__ == '__main__':
    app = QApplication([])
    window = PersonalizedQuestionnaires()
    window.show()
    app.exec_()
