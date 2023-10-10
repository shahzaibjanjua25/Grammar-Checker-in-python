import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton, QFileDialog, QHBoxLayout
from PyQt5.QtGui import QTextCursor, QTextCharFormat, QColor
from PyQt5.QtCore import Qt
from backendcode import correct_text, irregular_words
import difflib
class GrammarCheckerGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        input_layout = QHBoxLayout()
        self.text_edit_input = QTextEdit(self)
        input_layout.addWidget(self.text_edit_input)

        output_layout = QHBoxLayout()
        self.text_edit_output = QTextEdit(self)
        output_layout.addWidget(self.text_edit_output)

        layout.addLayout(input_layout)
        layout.addLayout(output_layout)

        button_layout = QHBoxLayout()

        self.open_button = QPushButton('Open File', self)
        self.open_button.clicked.connect(self.openFile)
        button_layout.addWidget(self.open_button)

        self.correct_button = QPushButton('Correct Grammar', self)
        self.correct_button.clicked.connect(self.correctGrammar)
        button_layout.addWidget(self.correct_button)

        self.save_button = QPushButton('Save Corrected Text', self)
        self.save_button.clicked.connect(self.saveFile)
        button_layout.addWidget(self.save_button)

        self.highlight_button = QPushButton('Show Changes', self)
        self.highlight_button.clicked.connect(self.highlightChanges)
        button_layout.addWidget(self.highlight_button)

        self.clear_button = QPushButton('Clear', self)
        self.clear_button.clicked.connect(self.clearText)
        button_layout.addWidget(self.clear_button)

        layout.addLayout(button_layout)
        dark_mode_stylesheet = """
    QWidget {
        background-color: #1e1e1e;
        font-size: 12pt;
        color: #ffffff;
    }
    QTextEdit {
        background-color: white;
        color: black;
        border: 2px solid #555555;
        border-radius: 10px;
        margin: 10px;
        padding: 10px;
        font-size:12px;
    }
    QPushButton {
        background-color: #3333FF;
        color: #ffffff;
        border: 2px solid #336699;
        border-radius: 10px;
        height: 20px;
        font-size: 10pt;
        margin: 10px;
        padding: 3px 1px;
    }
    QPushButton:hover {
        background-color: rgb(100, 160, 210);
        border-color: #5599cc;
    }
    QPushButton:pressed {
        background-color: rgb(50, 100, 150);
        border-color: #335599;
    }
"""




        self.setStyleSheet(dark_mode_stylesheet)
        self.setLayout(layout)
        self.setWindowTitle('Grammar Checker')
        self.setGeometry(100, 100, 800, 600)
        self.show()

    def openFile(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_name:
            with open(file_name, 'r') as file:
                self.text_edit_input.setPlainText(file.read())

    def correctGrammar(self):
        input_text = self.text_edit_input.toPlainText()
        corrected_text = correct_text(input_text)
        self.text_edit_output.setPlainText(corrected_text)

    def saveFile(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Corrected Text", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_name:
            with open(file_name, 'w') as file:
                file.write(self.text_edit_output.toPlainText())

    def clearText(self):
        self.text_edit_input.clear()
        self.text_edit_output.clear()

    def highlightChanges(self):
        input_text = self.text_edit_input.toPlainText()
        corrected_text = correct_text(input_text)

        d = difflib.Differ()
        diff = list(d.compare(input_text.split(), corrected_text.split()))

        input_cursor = self.text_edit_input.textCursor()
        corrected_cursor = self.text_edit_output.textCursor()

        input_cursor.setPosition(0)
        input_cursor.movePosition(QTextCursor.End, QTextCursor.KeepAnchor)
        input_cursor.mergeCharFormat(QTextCharFormat())

        corrected_cursor.setPosition(0)
        corrected_cursor.movePosition(QTextCursor.End, QTextCursor.KeepAnchor)
        corrected_cursor.mergeCharFormat(QTextCharFormat())

        diff_format_input = QTextCharFormat()
        diff_format_input.setBackground(QColor('red'))

        diff_format_corrected = QTextCharFormat()
        diff_format_corrected.setBackground(QColor('white'))

        input_idx, corrected_idx = 0, 0

        for line in diff:
            if line.startswith('- '):
                input_word = line[2:]
                start = input_text.find(input_word, input_idx)
                end = start + len(input_word)
                input_cursor.setPosition(start, QTextCursor.MoveAnchor)
                input_cursor.setPosition(end, QTextCursor.KeepAnchor)
                input_cursor.mergeCharFormat(diff_format_input)
                input_idx = end
            elif line.startswith('+ '):
                corrected_word = line[2:]
                start = corrected_text.find(corrected_word, corrected_idx)
                end = start + len(corrected_word)
                corrected_cursor.setPosition(start, QTextCursor.MoveAnchor)
                corrected_cursor.setPosition(end, QTextCursor.KeepAnchor)
                corrected_cursor.mergeCharFormat(diff_format_corrected)
                corrected_idx = end
            elif line.startswith('  '):
                input_idx += len(line[2:])
                corrected_idx += len(line[2:])

if __name__ == '__main__':
    app = QApplication([])
    window = GrammarCheckerGUI()
    window.show()
    sys.exit(app.exec_())
