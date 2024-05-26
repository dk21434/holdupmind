import os
import json
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QFont, QCursor
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTextEdit, QLineEdit, QListWidget, QWidget, QSpacerItem, QSizePolicy, QScrollArea, QMenu
from base_window import BaseWindow

JOURNAL_FILE = 'journals.json'

class Journaling(BaseWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #3E721D;")
        self.initContent()
        self.load_journals()

    def initContent(self):
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)

        title = QLabel("Journaling")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont('Arial', 18))
        title.setStyleSheet("color: white;")

        content_layout.addWidget(title)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setStyleSheet("QScrollArea { border: none; }")
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)

        name_row = QHBoxLayout()
        name_label = QLabel("Journal Name:")
        name_label.setFont(QFont('Arial', 14))
        name_label.setStyleSheet("color: black;")
        self.name_input = QLineEdit()
        self.name_input.setStyleSheet("background-color: #c4bbb7; font-size: 22px; padding: 5px;")
        name_row.addWidget(name_label)
        name_row.addWidget(self.name_input)

        scroll_layout.addLayout(name_row)

        journal_label = QLabel("Write your journal:")
        journal_label.setFont(QFont('Arial', 14))
        journal_label.setStyleSheet("color: black;")
        self.journal_input = QTextEdit()
        self.journal_input.setStyleSheet("background-color: #c4bbb7; font-size: 22px; padding: 5px;")
        scroll_layout.addWidget(journal_label)
        scroll_layout.addWidget(self.journal_input)

        save_button = QPushButton("Save Journal")
        save_button.setStyleSheet("background-color: #FFFFFF; color: black; font-size: 18px; padding: 20px; border-radius: 20px;")
        save_button.clicked.connect(self.save_journal)
        scroll_layout.addWidget(save_button, alignment=Qt.AlignCenter)

        scroll_layout.addItem(QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Fixed))

        old_journals_label = QLabel("Old Journals")
        old_journals_label.setFont(QFont('Arial', 16))
        old_journals_label.setStyleSheet("color: white;")
        scroll_layout.addWidget(old_journals_label, alignment=Qt.AlignLeft)

        self.old_journals_list = QListWidget()
        self.old_journals_list.setStyleSheet("font-size: 30px; padding: 10px; border: none;")
        self.old_journals_list.setFont(QFont('Arial', 18))
        self.old_journals_list.setContextMenuPolicy(Qt.CustomContextMenu)
        self.old_journals_list.customContextMenuRequested.connect(self.show_context_menu)
        self.old_journals_list.itemClicked.connect(self.display_journal)
        scroll_layout.addWidget(self.old_journals_list)

        scroll_content.setLayout(scroll_layout)
        scroll_area.setWidget(scroll_content)
        content_layout.addWidget(scroll_area)

        self.addContent(content_widget)

        self.create_fake_journals()

    def create_fake_journals(self):
        if not os.path.exists(JOURNAL_FILE):
            fake_journals = [
                {'name': 'First Session', 'text': 'This is the journal entry for the first session.', 'date': '2023-05-01'},
                {'name': 'Second Session', 'text': 'This is the journal entry for the second session.', 'date': '2023-05-15'},
                {'name': 'Third Session', 'text': 'This is the journal entry for the third session.', 'date': '2023-06-01'},
                {'name': 'Fourth Session', 'text': 'This is the journal entry for the fourth session.', 'date': '2023-06-15'},
                {'name': 'Fifth Session', 'text': 'This is the journal entry for the fifth session.', 'date': '2023-07-01'}
            ]

            with open(JOURNAL_FILE, 'w') as file:
                json.dump(fake_journals, file, indent=4)

            self.load_journals()

    def save_journal(self):
        journal_name = self.name_input.text().strip()
        journal_text = self.journal_input.toPlainText().strip()
        journal_date = QDate.currentDate().toString("yyyy-MM-dd")

        if not journal_name or not journal_text:
            print("Please provide a journal name and text.")
            return

        journal_entry = {
            'name': journal_name,
            'text': journal_text,
            'date': journal_date
        }

        journals = []
        if os.path.exists(JOURNAL_FILE):
            with open(JOURNAL_FILE, 'r') as file:
                journals = json.load(file)

        journals.append(journal_entry)

        with open(JOURNAL_FILE, 'w') as file:
            json.dump(journals, file, indent=4)

        self.load_journals()
        self.name_input.clear()
        self.journal_input.clear()
        print("Journal saved.")

    def load_journals(self):
        self.old_journals_list.clear()
        if os.path.exists(JOURNAL_FILE):
            with open(JOURNAL_FILE, 'r') as file:
                journals = json.load(file)
                for journal in journals:
                    self.old_journals_list.addItem(f"{journal['date']} - {journal['name']}")

    def display_journal(self, item):
        selected_journal = item.text()
        if os.path.exists(JOURNAL_FILE):
            with open(JOURNAL_FILE, 'r') as file:
                journals = json.load(file)
                for journal in journals:
                    if f"{journal['date']} - {journal['name']}" == selected_journal:
                        self.name_input.setText(journal['name'])
                        self.journal_input.setText(journal['text'])
                        break

    def show_context_menu(self, position):
        menu = QMenu()
        edit_action = menu.addAction("Edit")
        delete_action = menu.addAction("Delete")
        
        action = menu.exec_(QCursor.pos())
        if action == edit_action:
            self.edit_journal(self.old_journals_list.itemAt(position))
        elif action == delete_action:
            self.delete_journal(self.old_journals_list.itemAt(position))

    def edit_journal(self, item):
        self.display_journal(item)

    def delete_journal(self, item):
        selected_journal = item.text()
        journals = []
        if os.path.exists(JOURNAL_FILE):
            with open(JOURNAL_FILE, 'r') as file:
                journals = json.load(file)

        journals = [journal for journal in journals if f"{journal['date']} - {journal['name']}" != selected_journal]

        with open(JOURNAL_FILE, 'w') as file:
            json.dump(journals, file, indent=4)

        self.load_journals()
        print("Journal deleted.")

if __name__ == '__main__':
    app = QApplication([])
    window = Journaling()
    window.show()
    app.exec_()
