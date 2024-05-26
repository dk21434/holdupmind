from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget, QTextEdit, QApplication, QScrollArea
from base_window import BaseWindow

class ProgressTracking(BaseWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #3E721D;")
        self.initContent()

    def initContent(self):
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)

        subtitle = QLabel("Progress Tracking")
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
        scroll_layout.setContentsMargins(40, 0, 40, 20)

        progress_report = """
        <h3>Your Progress Report</h3>
        <p><strong>Date:</strong> 2024-05-25</p>
        <p><strong>Therapist:</strong> Dr. Jane Smith</p>
        <p><strong>Session Summary:</strong> This week, the patient showed significant improvement in managing anxiety symptoms. We focused on cognitive-behavioral techniques to address negative thought patterns.</p>
        <p><strong>Goals:</strong></p>
        <ul>
            <li>Reduce anxiety levels from 8/10 to 4/10.</li>
            <li>Improve sleep quality and duration.</li>
            <li>Increase social interactions and participation in group activities.</li>
        </ul>
        <p><strong>Achievements:</strong></p>
        <ul>
            <li>Anxiety levels reduced to 5/10.</li>
            <li>Reported better sleep quality, falling asleep within 30 minutes.</li>
            <li>Attended two social events this week.</li>
        </ul>
        <p><strong>Recommendations:</strong> Continue practicing relaxation techniques daily, schedule at least one social activity per week, and keep a sleep diary to monitor sleep patterns.</p>
        <p><strong>Next Session:</strong> Focus on deepening relaxation techniques and exploring the impact of diet on anxiety.</p>
        """

        progress_label = QLabel(progress_report)
        progress_label.setFont(QFont('Arial', 14))
        progress_label.setStyleSheet("color: black;")
        progress_label.setWordWrap(True)
        progress_label.setAlignment(Qt.AlignTop)

        scroll_layout.addWidget(progress_label)
        scroll_content.setLayout(scroll_layout)
        scroll_area.setWidget(scroll_content)
        content_layout.addWidget(scroll_area)

        self.addContent(content_widget)


if __name__ == '__main__':
    app = QApplication([])
    window = ProgressTracking()
    window.show()
    app.exec_()
