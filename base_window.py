from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QWidget, QApplication, QPushButton, QMenu
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, QPoint

class BaseWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("HoldUpMind")
        self.setWindowIcon(QIcon("images/Screenshot 2024-05-25 171055.png"))
        self.setFixedSize(700, 1100) 

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        top = QWidget()
        top_layout = QHBoxLayout(top)
        top_layout.setContentsMargins(10, 10, 10, 10)

        name_label = QLabel("HoldUpMind")
        name_label.setFont(QFont("Arial", 20, QFont.Bold))
        name_label.setStyleSheet("color: #ff630f;")

        self.menu_button = QPushButton()
        self.menu_button.setIcon(QIcon("images/menu_button.png"))
        self.menu_button.setFixedSize(50, 50)
        self.menu_button.setStyleSheet("""
            QPushButton { background: transparent; }
            QPushButton::menu-indicator { image: none; }
        """)

        top_layout.addWidget(name_label)
        top_layout.addStretch()
        top_layout.addWidget(self.menu_button)

        self.main_layout.addWidget(top)

        self.initMenu()

    def addContent(self, widget):
        self.main_layout.addWidget(widget)

    def initMenu(self):
        self.menu = QMenu()
        self.menu.setLayoutDirection(Qt.RightToLeft)
        self.menu.setStyleSheet("QMenu { background-color: #ff630f; }")
        self.menu.addAction('Home Page', lambda: self.change_screen('home'))
        self.menu.addAction('Booking', lambda: self.change_screen('booking'))
        self.menu.addAction('Therapist Matching', lambda: self.change_screen('therapist'))
        self.menu.addAction('Emergency Assistance', lambda: self.change_screen('emergency'))
        self.menu.addAction('Proggress Tracking', lambda: self.change_screen('progress'))
        self.menu.addAction('Events', lambda: self.change_screen('events'))
        self.menu.addAction('Journal and Reflection', lambda: self.change_screen('journal'))
        self.menu.addAction('Pernonalized Questionnaire', lambda: self.change_screen('quest'))
        self.menu.addAction('Self-Help Resources', lambda: self.change_screen('resources'))



        self.menu_button.setMenu(self.menu)

    def change_screen(self, screen_type):
        if screen_type == 'home':
            from screen_main import ScreenMain
            self.setCentralWidget(ScreenMain())
        elif screen_type == 'booking':
            from booking import ScreenBooking
            self.setCentralWidget(ScreenBooking())
        elif screen_type == 'therapist':
            from therapist_matching import TherapistMatching
            self.setCentralWidget(TherapistMatching())
        elif screen_type == 'emergency':
            from emergency_assist import EmergencyAssistance
            self.setCentralWidget(EmergencyAssistance())
        elif screen_type == 'progress':
            from progress_tracking import ProgressTracking
            self.setCentralWidget(ProgressTracking())
        elif screen_type == 'events':
            from events import Events
            self.setCentralWidget(Events())
        elif screen_type == 'journal':
            from journ_reflec import Journaling
            self.setCentralWidget(Journaling())
        elif screen_type == 'quest':
            from personal_quest import PersonalizedQuestionnaires
            self.setCentralWidget(PersonalizedQuestionnaires())
        elif screen_type == 'resources':
            from self_help import SelfHelpResources
            self.setCentralWidget(SelfHelpResources())


if __name__ == '__main__':
    app = QApplication([])
    window = BaseWindow()
    window.show()
    app.exec_()
