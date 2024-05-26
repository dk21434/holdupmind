from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget, QApplication, QScrollArea
from base_window import BaseWindow

class Events(BaseWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #3E721D;")
        self.initContent()

    def initContent(self):
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)

        subtitle = QLabel("Events")
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

        events = [
            {"image": "images/image3.jpg", "name": "From Overdrive to Rest: Learning to Find Rest in God's Sovereignty", "datetime": "Wednesday, May 29   2 - 4am EEST", "description": "Join us for practical steps on how to take authority of our Mental Health with God in control."},
            {"image": "images/image1.jpg", "name": "Real Talk: Mental Health Mondays 2024", "datetime": "Mondays    4 - 6am EEST", "description": "Join us for a candid conversation about mental health topics. Share or listen. This is a safe space for black people."},
            {"image": "images/image4.jpg", "name": "Mental Health Skills for Managers", "datetime": "Mon, 23 Sep 2024   15:00 - 19:00 EEST", "description": "A superb half-day course delivered by Beth Goodyear, a leading trainer and facilitator - an essential course for all Managers!"},
            {"image": "images/image5.jpg", "name": "Let's Talk: Mental Health & Coping", "datetime": "Saturday, June 29   2 - 3am EEST", "description": "Let's talk about our mental health and start breaking that stigma!"},
        ]

        for event in events:
            event_row = QVBoxLayout()

            event_image = QLabel()
            pixmap = QPixmap(event["image"])
            event_image.setPixmap(pixmap)
            event_image.setFixedHeight(300)
            event_image.setFixedWidth(600)
            event_image.setScaledContents(True)
            event_image.setStyleSheet("border-radius: 15px;")

            event_name = QLabel(event["name"])
            event_name.setFont(QFont('Arial', 13, QFont.Bold))
            event_name.setStyleSheet("color: black;")
            event_name.setWordWrap(True)

            event_datetime = QLabel(event["datetime"])
            event_datetime.setFont(QFont('Arial', 11))
            event_datetime.setStyleSheet("color: black;")

            event_description = QLabel(event["description"])
            event_description.setFont(QFont('Arial', 8))
            event_description.setStyleSheet("color: black;")
            event_description.setWordWrap(True)

            event_row.addWidget(event_image)
            event_row.addWidget(event_name)
            event_row.addWidget(event_datetime)
            event_row.addWidget(event_description)
            event_row.addSpacing(40)

            scroll_layout.addLayout(event_row)

        scroll_content.setLayout(scroll_layout)
        scroll_area.setWidget(scroll_content)
        content_layout.addWidget(scroll_area)

        self.addContent(content_widget)

if __name__ == '__main__':
    app = QApplication([])
    window = Events()
    window.show()
    app.exec_()
