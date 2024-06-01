from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QLabel, QPushButton, QTextEdit, QApplication, QScrollArea, QLineEdit, QMessageBox
from base_window import BaseWindow
import json

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

        self.questions = [
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

        self.answers = []

        for question in self.questions:
            question_row = QVBoxLayout()

            question_label = QLabel(question)
            question_label.setFont(QFont('Arial', 14))
            question_label.setStyleSheet("color: black;")
            question_label.setWordWrap(True)

            answer_input = QLineEdit()
            answer_input.setStyleSheet("background-color: #c4bbb7; font-size: 14px; padding: 5px;")
            self.answers.append(answer_input)

            question_row.addWidget(question_label)
            question_row.addWidget(answer_input)

            scroll_layout.addLayout(question_row)
            scroll_layout.addSpacing(10)

        scroll_content.setLayout(scroll_layout)
        scroll_area.setWidget(scroll_content)
        content_layout.addWidget(scroll_area)

        submit_button = QPushButton("Submit")
        submit_button.setStyleSheet("background-color: #FFFFFF; color: black; font-size: 16px; padding: 10px; border-radius: 10px;")
        submit_button.clicked.connect(self.submit_answers)
        submit_button_layout = QHBoxLayout()
        submit_button_layout.addStretch()
        submit_button_layout.addWidget(submit_button)
        submit_button_layout.addStretch()
        content_layout.addLayout(submit_button_layout)

        self.addContent(content_widget)

    def submit_answers(self):
        answers_data = {}
        all_answered = True
        for question, answer_widget in zip(self.questions, self.answers):
            answer = answer_widget.text().strip()
            if not answer:
                all_answered = False
                break
            answers_data[question] = answer

        if all_answered:
            with open('answers.json', 'w') as file:
                json.dump(answers_data, file, indent=4)
            QMessageBox.information(self, "Submission Successful", "Thank you for completing the questionnaire.")
        else:
            QMessageBox.warning(self, "Submission Error", "Please answer all questions before submitting.")


if __name__ == '__main__':
    app = QApplication([])
    window = PersonalizedQuestionnaires()
    window.show()
    app.exec_()
