# -*- coding: utf-8 -*-

"""
QTextEdit Style Examples
This file demonstrates how to customize various style effects of the QTextEdit control in Qt.
"""

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QTextEdit, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QComboBox, QGroupBox
from PySide6.QtGui import QFont

class TextEditStylesWindow(QMainWindow):
    """QTextEdit style example window"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QTextEdit Style Examples")
        self.resize(800, 600)
        
        # Create central widget and main layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        
        # Add title
        title_label = QLabel("QTextEdit Style Examples")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; margin: 10px;")
        self.main_layout.addWidget(title_label)
        
        # Create style selector
        selector_layout = QHBoxLayout()
        selector_label = QLabel("Select Text Editor Style:")
        self.style_combobox = QComboBox()
        self.style_combobox.addItems([
            "Basic Text Box", 
            "Code Editor", 
            "Rich Text Editor", 
            "Notebook Style",
            "Paper Style",
            "Dark Theme",
            "Read-Only Document",
            "Editor with Line Numbers"
        ])
        self.style_combobox.currentIndexChanged.connect(self.update_textedit_style)
        
        # Function buttons
        self.apply_button = QPushButton("Apply Style")
        self.apply_button.clicked.connect(lambda: self.update_textedit_style(self.style_combobox.currentIndex()))
        self.reset_button = QPushButton("Reset")
        self.reset_button.clicked.connect(self.reset_textedit)
        
        selector_layout.addWidget(selector_label)
        selector_layout.addWidget(self.style_combobox)
        selector_layout.addWidget(self.apply_button)
        selector_layout.addWidget(self.reset_button)
        selector_layout.addStretch()
        
        self.main_layout.addLayout(selector_layout)
        
        # Create text editor container
        self.textedit_container = QWidget()
        self.textedit_layout = QVBoxLayout(self.textedit_container)
        self.main_layout.addWidget(self.textedit_container)
        
        # Create various text editors
        self.create_textedits()
        
        # Add information
        self.info_label = QLabel()
        self.info_label.setWordWrap(True)
        self.info_label.setStyleSheet("margin-top: 10px; color: #666;")
        self.main_layout.addWidget(self.info_label)
        
        # Show basic text box by default
        self.update_textedit_style(0)
    
    def create_textedits(self):
        """Create various text editors"""
        # Basic text box
        self.basic_textedit = QTextEdit()
        self.basic_textedit.setPlaceholderText("This is a basic text editor...")
        self.basic_textedit.setMinimumHeight(300)
        self.textedit_layout.addWidget(QLabel("1. Basic Text Box"))
        self.textedit_layout.addWidget(self.basic_textedit)
        
        # Code editor
        self.code_textedit = QTextEdit()
        self.code_textedit.setPlaceholderText("// This is a code editor\nprint('Hello, World!')")
        self.code_textedit.setMinimumHeight(300)
        self.textedit_layout.addWidget(QLabel("2. Code Editor"))
        self.textedit_layout.addWidget(self.code_textedit)
        
        # Rich text editor
        self.rich_textedit = QTextEdit()
        self.rich_textedit.setPlaceholderText("This is a rich text editor...")
        self.rich_textedit.setMinimumHeight(300)
        self.textedit_layout.addWidget(QLabel("3. Rich Text Editor"))
        self.textedit_layout.addWidget(self.rich_textedit)
        
        # Notebook style
        self.notebook_textedit = QTextEdit()
        self.notebook_textedit.setPlaceholderText("This is a notebook-style text editor...")
        self.notebook_textedit.setMinimumHeight(300)
        self.textedit_layout.addWidget(QLabel("4. Notebook Style"))
        self.textedit_layout.addWidget(self.notebook_textedit)
        
        # Paper style
        self.paper_textedit = QTextEdit()
        self.paper_textedit.setPlaceholderText("This is a paper-style text editor...")
        self.paper_textedit.setMinimumHeight(300)
        self.textedit_layout.addWidget(QLabel("5. Paper Style"))
        self.textedit_layout.addWidget(self.paper_textedit)
        
        # Dark theme
        self.dark_textedit = QTextEdit()
        self.dark_textedit.setPlaceholderText("This is a dark theme text editor...")
        self.dark_textedit.setMinimumHeight(300)
        self.textedit_layout.addWidget(QLabel("6. Dark Theme"))
        self.textedit_layout.addWidget(self.dark_textedit)
        
        # Read-only document
        self.readonly_textedit = QTextEdit()
        self.readonly_textedit.setReadOnly(True)
        self.readonly_textedit.setMinimumHeight(300)
        self.textedit_layout.addWidget(QLabel("7. Read-Only Document"))
        self.textedit_layout.addWidget(self.readonly_textedit)
        
        # Editor with line numbers (simulated)
        self.linenumber_textedit = QTextEdit()
        self.linenumber_textedit.setPlaceholderText("1: This is an editor with line numbers\n2: Second line\n3: Third line")
        self.linenumber_textedit.setMinimumHeight(300)
        self.textedit_layout.addWidget(QLabel("8. Editor with Line Numbers (Simulated)"))
        self.textedit_layout.addWidget(self.linenumber_textedit)
        
        # Apply styles
        self.apply_styles()
        
        # Hide all text editors by default
        for i in range(1, self.textedit_layout.count()):
            widget = self.textedit_layout.itemAt(i).widget()
            if widget:
                widget.hide()
        
        # Set read-only document content
        self.readonly_textedit.setHtml("""
        <h2>Read-Only Document Example</h2>
        <p>This is an example of a read-only document. In Qt, you can create a read-only document by setting QTextEdit's setReadOnly(True) method.</p>
        <h3>Features of read-only documents:</h3>
        <ul>
            <li>Users cannot edit document content</li>
            <li>You can set special styles to distinguish from normal editable documents</li>
            <li>Text can still be selected and copied</li>
        </ul>
        <p>You can use CSS styles to customize the appearance of read-only documents, such as changing background color, text color, fonts, etc.</p>
        """)
    
    def apply_styles(self):
        """Apply various text editor styles"""
        # 1. Basic text box style
        self.basic_textedit.setStyleSheet("""
            QTextEdit {
                background-color: white;
                color: #333333;
                border: 1px solid #CCCCCC;
                border-radius: 4px;
                padding: 10px;
                font-family: 'Microsoft YaHei', Arial, sans-serif;
                font-size: 14px;
                line-height: 1.5;
            }
            QTextEdit:hover {
                border-color: #999999;
            }
            QTextEdit:focus {
                border-color: #2196F3;
                background-color: #FAFAFA;
                outline: none;
            }
        """)
        
        # 2. Code editor style
        code_font = QFont()
        code_font.setFamily("Consolas")
        code_font.setStyleHint(QFont.Monospace)
        code_font.setFixedPitch(True)
        code_font.setPointSize(10)
        self.code_textedit.setFont(code_font)
        
        self.code_textedit.setStyleSheet("""
            QTextEdit {
                background-color: #2D2D2D;
                color: #D4D4D4;
                border: 1px solid #444444;
                border-radius: 4px;
                padding: 10px;
                font-family: 'Consolas', 'Courier New', monospace;
                font-size: 14px;
                line-height: 1.4;
            }
            QTextEdit:hover {
                border-color: #666666;
            }
            QTextEdit:focus {
                border-color: #007ACC;
                background-color: #2D2D2D;
                outline: none;
            }
        """)
        
        # 3. Rich text editor style
        self.rich_textedit.setStyleSheet("""
            QTextEdit {
                background-color: white;
                color: #333333;
                border: 1px solid #CCCCCC;
                border-radius: 4px;
                padding: 15px;
                font-family: 'Microsoft YaHei', Arial, sans-serif;
                font-size: 14px;
                line-height: 1.6;
                selection-background-color: #2196F3;
                selection-color: white;
            }
            QTextEdit:hover {
                border-color: #999999;
            }
            QTextEdit:focus {
                border-color: #2196F3;
                outline: none;
            }
        """)
        
        # 4. Notebook style
        self.notebook_textedit.setStyleSheet("""
            QTextEdit {
                background-color: #FFFBE6;
                color: #333333;
                border: 1px solid #FFD700;
                border-radius: 4px;
                padding: 15px;
                font-family: 'SimSun', '宋体', serif;
                font-size: 14px;
                line-height: 1.6;
                background-image: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMDAlIiBoZWlnaHQ9IjEwMCUiPjxkZWZzPjxwYXR0ZXJuIGlkPSJwYXR0ZXJuIiB4PSIwIiB5PSIwIiB3aWR0aD0iMTAwIiBoZWlnaHQ9IjIwIiBwYXR0ZXJuVW5pdHM9InVzZXJTcGFjZU9uVXNlIiBwYXR0ZXJuVHJhbnNmb3JtPSJyb3RhdGUoNDUpIj48bGluZSB4MT0iMCIgeTE9IjAiIHgyPSIxMDAiIHkyPSIwIiBzdHJva2U9IiNmZmQ3MDAiIHN0cm9rZS13aWR0aD0iMC41Ii8+PC9wYXR0ZXJuPjwvZGVmcz48cmVjdCB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiBmaWxsPSJ1cmwoI3BhdHRlcm4pIiAvPjwvc3ZnPg==);
            }
            QTextEdit:hover {
                border-color: #FFA500;
            }
            QTextEdit:focus {
                border-color: #FFA500;
                background-color: #FFF8E1;
                outline: none;
            }
        """)
        
        # 5. Paper style
        self.paper_textedit.setStyleSheet("""
            QTextEdit {
                background-color: white;
                color: #333333;
                border: 1px solid #CCCCCC;
                border-radius: 4px;
                padding: 20px;
                font-family: 'SimSun', '宋体', serif;
                font-size: 14px;
                line-height: 1.8;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                background-image: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMDAlIiBoZWlnaHQ9IjEwMCUiPjxkZWZzPjxwYXR0ZXJuIGlkPSJwYXR0ZXJuIiB4PSIwIiB5PSIwIiB3aWR0aD0iMTAwIiBoZWlnaHQ9IjIwIiBwYXR0ZXJuVW5pdHM9InVzZXJTcGFjZU9uVXNlIiBwYXR0ZXJuVHJhbnNmb3JtPSJyb3RhdGUoNDUpIj48bGluZSB4MT0iMCIgeTE9IjAiIHgyPSIxMDAiIHkyPSIwIiBzdHJva2U9IiNmNWY1ZjUiIHN0cm9rZS13aWR0aD0iMC41Ii8+PC9wYXR0ZXJuPjwvZGVmcz48cmVjdCB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiBmaWxsPSJ1cmwoI3BhdHRlcm4pIiAvPjwvc3ZnPg==);
            }
            QTextEdit:hover {
                border-color: #999999;
            }
            QTextEdit:focus {
                border-color: #2196F3;
                box-shadow: 0 2px 15px rgba(33, 150, 243, 0.2);
                outline: none;
            }
        """)
        
        # 6. Dark theme style
        self.dark_textedit.setStyleSheet("""
            QTextEdit {
                background-color: #1E1E1E;
                color: #D4D4D4;
                border: 1px solid #444444;
                border-radius: 4px;
                padding: 15px;
                font-family: 'Microsoft YaHei', Arial, sans-serif;
                font-size: 14px;
                line-height: 1.5;
                selection-background-color: #007ACC;
                selection-color: white;
            }
            QTextEdit:hover {
                border-color: #666666;
            }
            QTextEdit:focus {
                border-color: #007ACC;
                outline: none;
            }
        """)
        
        # 7. Read-only document style
        self.readonly_textedit.setStyleSheet("""
            QTextEdit {
                background-color: #F5F5F5;
                color: #666666;
                border: 1px solid #E0E0E0;
                border-radius: 4px;
                padding: 15px;
                font-family: 'Microsoft YaHei', Arial, sans-serif;
                font-size: 14px;
                line-height: 1.6;
            }
            QTextEdit QScrollBar:vertical {
                background-color: #F5F5F5;
                width: 10px;
            }
            QTextEdit QScrollBar::handle:vertical {
                background-color: #BDBDBD;
                border-radius: 5px;
            }
            QTextEdit QScrollBar::handle:vertical:hover {
                background-color: #9E9E9E;
            }
        """)
        
        # 8. Editor with line numbers style (simulated)
        self.linenumber_textedit.setStyleSheet("""
            QTextEdit {
                background-color: #F7F7F7;
                color: #333333;
                border: 1px solid #CCCCCC;
                border-radius: 4px;
                padding: 10px 10px 10px 40px;
                font-family: 'Consolas', 'Courier New', monospace;
                font-size: 14px;
                line-height: 1.4;
                background-image: 
                    linear-gradient(to right, #E0E0E0 0px, #E0E0E0 30px, transparent 30px),
                    url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMDAlIiBoZWlnaHQ9IjEwMCUiPjxkZWZzPjxwYXR0ZXJuIGlkPSJwYXR0ZXJuIiB4PSIzMCIgeT0iMCIgd2lkdGg9IjcwIiBoZWlnaHQ9IjIwIiBwYXR0ZXJuVW5pdHM9InVzZXJTcGFjZU9uVXNlIiBwYXR0ZXJuVHJhbnNmb3JtPSJyb3RhdGUoNDUpIj48bGluZSB4MT0iMCIgeTE9IjAiIHgyPSI3MCIgeTI9IjAiIHN0cm9rZT0iI2ZmZiIgc3Ryb2tlLXdpZHRoPSIwLjUiLz48L3BhdHRlcm4+PC9kZWZzPjxyZWN0IHdpZHRoPSIxMDAlIiBoZWlnaHQ9IjEwMCUiIGZpbGw9InVybCgjcGF0dGVybikiIC8+PC9zdmc+);
            }
            QTextEdit:hover {
                border-color: #999999;
            }
            QTextEdit:focus {
                border-color: #2196F3;
                background-color: #F5F5F5;
                outline: none;
            }
        """)
    
    def update_textedit_style(self, index):
        """Update the displayed text editor style based on selection"""
        # Hide all text editors
        for i in range(1, self.textedit_layout.count()):
            widget = self.textedit_layout.itemAt(i).widget()
            if widget:
                widget.hide()
        
        # Show the selected text editor
        textedits = [
            self.basic_textedit,
            self.code_textedit,
            self.rich_textedit,
            self.notebook_textedit,
            self.paper_textedit,
            self.dark_textedit,
            self.readonly_textedit,
            self.linenumber_textedit
        ]
        
        # Show the corresponding label and text editor
        self.textedit_layout.itemAt(index * 2).widget().show()  # Show label
        textedits[index].show()  # Show text editor
        
        # Update description information
        descriptions = [
            "Basic text box uses a simple design, suitable for most general text input scenarios.",
            "Code editor uses monospaced font and dark theme, suitable for programming and code editing.",
            "Rich text editor optimizes rich text display and editing, supports HTML formatting.",
            "Notebook style uses yellow background and simulated lines to create the feeling of a paper notebook.",
            "Paper style creates the effect of real paper through shadows and textures.",
            "Dark theme is suitable for long periods of reading and editing, reducing eye strain.",
            "Read-only document style is suitable for displaying non-editable content.",
            "Editor with line numbers (simulated) demonstrates how to create an IDE-like editing environment."
        ]
        self.info_label.setText(descriptions[index])
    
    def reset_textedit(self):
        """Reset text editors"""
        # Clear all text editor contents
        textedits = [
            self.basic_textedit,
            self.code_textedit,
            self.rich_textedit,
            self.notebook_textedit,
            self.paper_textedit,
            self.dark_textedit,
            # Don't reset read-only document
            self.linenumber_textedit
        ]
        
        for textedit in textedits:
            textedit.clear()

# Startup function
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TextEditStylesWindow()
    window.show()
    sys.exit(app.exec())