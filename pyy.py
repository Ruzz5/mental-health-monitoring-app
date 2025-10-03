
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget,QLabel, QLineEdit, QTextEdit, QPushButton,QVBoxLayout, QHBoxLayout, QListWidget, QFrame
)
from PyQt6.QtGui import QFont, QPalette, QColor


class MoodMonitor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mood and Mental Health Monitor")
        self.setGeometry(450, 200, 800, 450)

        central = QWidget()
        self.setCentralWidget(central)

        main = QHBoxLayout()
        form = QVBoxLayout()
        monitor = QVBoxLayout()

        self.monitor_label = QLabel("Diagnosis: ")
        self.monitor_label.setFont(QFont("Press Start 2P", 10))
        self.monitor_label.setStyleSheet("color: red;")

        self.log_list = QListWidget()
        self.log_list.setFont(QFont("Press Start 2P", 8))
        self.log_list.setStyleSheet("background-color: black; color: red;")
        self.log_list.setFrameShape(QFrame.Shape.Box)

        self.stats_label = QLabel("Stats")
        self.stats_label.setFont(QFont("Press Start 2P", 8))
        self.stats_label.setStyleSheet("color: red;")

        monitor.addWidget(self.monitor_label)
        monitor.addWidget(self.log_list, 4)
        monitor.addWidget(self.stats_label, 1)

        self.mood_label = QLabel("Mood:")
        self.mood_label.setFont(QFont("Press Start 2P", 8))
        self.mood_label.setStyleSheet("color: red;")

        self.mood_input = QLineEdit()
        self.mood_input.setFont(QFont("Press Start 2P", 8))
        self.mood_input.setStyleSheet("background-color: black; color: red;")

        self.note_label = QLabel("Notes:")
        self.note_label.setFont(QFont("Press Start 2P", 8))
        self.note_label.setStyleSheet("color: red;")

        self.note_input = QTextEdit()
        self.note_input.setFont(QFont("Press Start 2P", 8))
        self.note_input.setStyleSheet("background-color: black; color: red;")
        self.note_input.setFixedHeight(80)

        self.add_btn = QPushButton("Enter")
        self.add_btn.setFont(QFont("Press Start 2P", 8))
        self.add_btn.setStyleSheet("background-color: red; color: black;")
        self.add_btn.clicked.connect(self.add_entry)

        self.clear_btn = QPushButton("Clear History")
        self.clear_btn.setFont(QFont("Press Start 2P", 8))
        self.clear_btn.setStyleSheet("background-color: red; color: black;")

        form.addWidget(self.mood_label)
        form.addWidget(self.mood_input)
        form.addWidget(self.note_label)
        form.addWidget(self.note_input)
        form.addWidget(self.add_btn)
        form.addWidget(self.clear_btn)

        main.addLayout(monitor, 2)
        main.addLayout(form, 1)
        central.setLayout(main)

        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor(0, 0, 0)) 
        self.setPalette(palette)

    def add_entry(self):
       
        mood = self.mood_input.text().strip()
        note = self.note_input.toPlainText().strip()

        if mood and note:
            entry = f"Mood: {mood} | Note: {note}"
            self.log_list.addItem(entry)

            self.mood_input.clear()
            self.note_input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MoodMonitor()
    window.show()
    sys.exit(app.exec())
