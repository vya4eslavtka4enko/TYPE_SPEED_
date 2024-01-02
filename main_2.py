import sys

from datetime import datetime

from PySide6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget


class TypingSpeedApp(QApplication):

    def __init__(self, sys_argv):

        super().__init__(sys_argv)

        self.window = QWidget()

        self.window.setWindowTitle("Typing Speed Test")

        self.sample_text = "The quick brown fox jumps over the lazy dog."

        self.user_input = QLineEdit()

        self.start_time = None

        self.create_widgets()

        self.window.show()

    def create_widgets(self):

        layout = QVBoxLayout()

        instruction_label = QLabel("Type the following text:")

        layout.addWidget(instruction_label)

        sample_text_label = QLabel(self.sample_text)

        sample_text_label.setFont("Arial,12")

        layout.addWidget(sample_text_label)

        layout.addWidget(self.user_input)

        start_button = QPushButton("Start Typing")

        start_button.clicked.connect(self.start_typing)

        layout.addWidget(start_button)

        self.result_label = QLabel("")

        self.result_label.setFont("Arial,14,bold")

        layout.addWidget(self.result_label)

        self.window.setLayout(layout)

    def start_typing(self):

        self.user_input.clear()

        self.result_label.setText("")

        self.start_time = datetime.now()

        self.user_input.textChanged.connect(self.check_typing)

    def check_typing(self):

        typed_text = self.user_input.text()

        if self.sample_text.startswith(typed_text):

            if self.sample_text == typed_text:
                # Typing completed

                self.calculate_typing_speed()

        else:

            self.user_input.clear()

    def calculate_typing_speed(self):

        end_time = datetime.now()

        elapsed_time = (end_time - self.start_time).total_seconds() / 60.0  # Convert to minutes

        words_typed = len(self.sample_text.split())

        typing_speed = words_typed / elapsed_time

        self.result_label.setText(f"Typing Speed: {typing_speed:.2f} WPM")

        self.user_input.textChanged.disconnect(self.check_typing)


if __name__ == "__main__":
    app = TypingSpeedApp(sys.argv)

    sys.exit(app.exec())