import json
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QFont, QPixmap, QDesktopServices
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox, QScrollArea, QApplication, QHBoxLayout, QGridLayout
from base_window import BaseWindow

class SelfHelpResources(BaseWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #3E721D;")
        self.initContent()
        self.load_resources()

    def initContent(self):
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)

        subtitle = QLabel("Self-Help Resources")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setFont(QFont('Arial', 18))
        subtitle.setStyleSheet("color: white;")
        content_layout.addWidget(subtitle)

        category_type_layout = QVBoxLayout()

        category_layout = QHBoxLayout()
        category_label = QLabel("Choose Category:")
        category_label.setFont(QFont('Arial', 14))
        category_label.setStyleSheet("color: white;")
        category_layout.addWidget(category_label)

        self.category_combo = QComboBox()
        self.category_combo.addItems(["Anxiety", "Depression", "Stress"])
        self.category_combo.setStyleSheet("background-color: white; font-size: 20px;")
        self.category_combo.setFixedWidth(200)
        self.category_combo.currentTextChanged.connect(self.update_resources)
        category_layout.addWidget(self.category_combo)

        category_type_layout.addLayout(category_layout)

        type_layout = QHBoxLayout()
        type_label = QLabel("Choose Type:")
        type_label.setFont(QFont('Arial', 14))
        type_label.setStyleSheet("color: white;")
        type_layout.addWidget(type_label)

        self.type_combo = QComboBox()
        self.type_combo.addItems(["Articles", "Videos", "Podcasts"])
        self.type_combo.setStyleSheet("background-color: white; font-size: 20px;")
        self.type_combo.setFixedWidth(200)
        self.type_combo.currentTextChanged.connect(self.update_resources)
        type_layout.addWidget(self.type_combo)

        category_type_layout.addLayout(type_layout)

        content_layout.addLayout(category_type_layout)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setStyleSheet("QScrollArea { border: none; }")
        self.scroll_content = QWidget()
        self.scroll_layout = QGridLayout(self.scroll_content)
        self.scroll_area.setWidget(self.scroll_content)
        content_layout.addWidget(self.scroll_area)

        self.addContent(content_widget)

    def load_resources(self):
        with open('resources.json', 'r') as file:
            self.resources = json.load(file)
        self.update_resources()

    def update_resources(self):
        selected_category = self.category_combo.currentText()
        selected_type = self.type_combo.currentText()

        for i in reversed(range(self.scroll_layout.count())):
            widget = self.scroll_layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        filtered_resources = [
            res for res in self.resources 
            if res['main_category'] == selected_category and res['category'] == selected_type
        ]

        row, col = 0, 0
        for resource in filtered_resources:
            resource_widget = self.create_resource_widget(resource)
            self.scroll_layout.addWidget(resource_widget, row, col)

            col += 1
            if col > 1:
                col = 0
                row += 1

        self.scroll_layout.setRowStretch(row + 1, 1)

    def create_resource_widget(self, resource):
        resource_widget = QWidget()
        resource_layout = QVBoxLayout(resource_widget)
        resource_layout.setAlignment(Qt.AlignTop)

        img_label = QLabel()
        pixmap = self.get_image_path(resource['category'])
        img_label.setPixmap(pixmap)
        img_label.setScaledContents(True)
        img_label.setFixedSize(200, 150)
        img_label.mousePressEvent = lambda event, url=resource['link']: self.open_link(url)
        resource_layout.addWidget(img_label, alignment=Qt.AlignCenter)

        title_label = QLabel(resource['title'])
        title_label.setFont(QFont('Arial', 12, QFont.Bold))
        title_label.setStyleSheet("color: white;")
        title_label.setWordWrap(True)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setFixedHeight(150)
        title_label.mousePressEvent = lambda event, url=resource['link']: self.open_link(url)
        resource_layout.addWidget(title_label)

        return resource_widget

    def open_link(self, url):
        QDesktopServices.openUrl(QUrl(url))

    def get_image_path(self, category):
        if category == "Videos":
            return QPixmap("images/vid.webp")
        elif category == "Podcasts":
            return QPixmap("images/pod.webp")
        elif category == "Articles":
            return QPixmap("images/art.png")
        return ""

if __name__ == '__main__':
    app = QApplication([])
    window = SelfHelpResources()
    window.show()
    app.exec_()
