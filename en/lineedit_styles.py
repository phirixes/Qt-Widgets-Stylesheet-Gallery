#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
QLineEdit Style Sheet Example
This file demonstrates various stylesheet usages for the QLineEdit widget in Qt, with detailed comments for each style.
"""

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QWidget, 
    QLineEdit, 
    QVBoxLayout, 
    QHBoxLayout, 
    QLabel
)
from PySide6.QtGui import QFont, QColor

class LineEditStylesWindow(QMainWindow):
    """QLineEdit stylesheet example window"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QLineEdit Style Sheet Example")
        self.resize(800, 600)
        
        # Create central widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        
        # Add title
        title_label = QLabel("QLineEdit Style Sheet Example")
        title_label.setAlignment(Qt.AlignCenter)
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title_label.setFont(title_font)
        self.main_layout.addWidget(title_label)
        
        # Create stylesheet explanations and line edit examples
        self.create_basic_style_example()
        self.create_state_style_example()
        self.create_placeholder_style_example()
        self.create_password_style_example()
        self.create_gradient_style_example()
        self.create_custom_cursor_style_example()
        self.create_icon_style_example()
        self.create_readonly_style_example()
    
    def create_basic_style_example(self):
        """Basic style sheet example"""
        section_label = QLabel("Basic Styles")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # Default line edit
        default_lineedit = QLineEdit()
        default_lineedit.setPlaceholderText("Default Line Edit")
        layout.addWidget(default_lineedit)
        
        # Basic style line edit
        basic_lineedit = QLineEdit()
        basic_lineedit.setPlaceholderText("Basic Style")
        basic_lineedit.setStyleSheet("""
            QLineEdit {
                background-color: #FFFFFF;
                color: #333333;
                border: 2px solid #CCCCCC;
                border-radius: 4px;
                padding: 5px;
            }
        """)
        layout.addWidget(basic_lineedit)
        
        self.main_layout.addLayout(layout)
    
    def create_state_style_example(self):
        """State style sheet example (normal, hover, focus)"""
        section_label = QLabel("State Styles")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # Hover and focus state styles
        state_lineedit = QLineEdit()
        state_lineedit.setPlaceholderText("Hover and Focus Effects")
        state_lineedit.setStyleSheet("""
            QLineEdit {
                background-color: #FFFFFF;
                color: #333333;
                border: 2px solid #CCCCCC;
                border-radius: 4px;
                padding: 5px;
                transition: border-color 0.3s ease;
            }
            QLineEdit:hover {
                border-color: #999999;
            }
            QLineEdit:focus {
                border-color: #2196F3;
                background-color: #F5F5F5;
                outline: none;  /* Remove default focus outline */
            }
        """)
        layout.addWidget(state_lineedit)
        
        # Different color theme line edit
        blue_lineedit = QLineEdit()
        blue_lineedit.setPlaceholderText("Blue Theme")
        blue_lineedit.setStyleSheet("""
            QLineEdit {
                background-color: #E3F2FD;
                color: #1565C0;
                border: 2px solid #90CAF9;
                border-radius: 4px;
                padding: 5px;
            }
            QLineEdit:focus {
                border-color: #1976D2;
                background-color: #BBDEFB;
            }
        """)
        layout.addWidget(blue_lineedit)
        
        self.main_layout.addLayout(layout)
    
    def create_placeholder_style_example(self):
        """Placeholder text style sheet example"""
        section_label = QLabel("Placeholder Text Styles")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # Custom placeholder text style
        placeholder_lineedit = QLineEdit()
        placeholder_lineedit.setPlaceholderText("Custom Placeholder Style")
        placeholder_lineedit.setStyleSheet("""
            QLineEdit {
                background-color: #FFFFFF;
                color: #333333;
                border: 2px solid #CCCCCC;
                border-radius: 4px;
                padding: 5px;
            }
            QLineEdit::placeholder {
                color: #999999;
                font-style: italic;
            }
        """)
        layout.addWidget(placeholder_lineedit)
        
        # Colored placeholder
        color_placeholder_lineedit = QLineEdit()
        color_placeholder_lineedit.setPlaceholderText("Colored Placeholder")
        color_placeholder_lineedit.setStyleSheet("""
            QLineEdit {
                background-color: #FFFFFF;
                border: 2px solid #CCCCCC;
                border-radius: 4px;
                padding: 5px;
            }
            QLineEdit::placeholder {
                color: #FF9800;
                font-weight: bold;
            }
        """)
        layout.addWidget(color_placeholder_lineedit)
        
        self.main_layout.addLayout(layout)
    
    def create_password_style_example(self):
        """Password field style sheet example"""
        section_label = QLabel("Password Field Styles")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # Normal password field
        password_lineedit = QLineEdit()
        password_lineedit.setEchoMode(QLineEdit.Password)
        password_lineedit.setPlaceholderText("Password")
        password_lineedit.setStyleSheet("""
            QLineEdit {
                background-color: #FFFFFF;
                border: 2px solid #CCCCCC;
                border-radius: 4px;
                padding: 5px;
            }
        """)
        layout.addWidget(password_lineedit)
        
        # Custom password symbols
        custom_password_lineedit = QLineEdit()
        custom_password_lineedit.setEchoMode(QLineEdit.Password)
        custom_password_lineedit.setPlaceholderText("Custom Password Style")
        custom_password_lineedit.setStyleSheet("""
            QLineEdit {
                background-color: #FFF3E0;
                border: 2px solid #FFCC80;
                border-radius: 4px;
                padding: 5px;
                color: #E65100;
            }
            /* Note: Qt stylesheets don't directly support custom password symbols */
            /* In real projects, you need to subclass QLineEdit to implement this */
        """)
        layout.addWidget(custom_password_lineedit)
        
        self.main_layout.addLayout(layout)
    
    def create_gradient_style_example(self):
        """Gradient background style sheet example"""
        section_label = QLabel("Gradient Background Styles")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # Linear gradient line edit
        gradient_lineedit = QLineEdit()
        gradient_lineedit.setPlaceholderText("Gradient Background")
        gradient_lineedit.setStyleSheet("""
            QLineEdit {
                background: qlineargradient(
                    x1: 0, y1: 0,
                    x2: 1, y2: 0,
                    stop: 0 #E1BEE7,
                    stop: 1 #D1C4E9
                );
                color: #4A148C;
                border: 2px solid #9575CD;
                border-radius: 4px;
                padding: 5px;
                font-weight: bold;
            }
        """)
        layout.addWidget(gradient_lineedit)
        
        # Glow effect line edit
        glow_lineedit = QLineEdit()
        glow_lineedit.setPlaceholderText("Glow Effect")
        glow_lineedit.setStyleSheet("""
            QLineEdit {
                background-color: #FFFFFF;
                color: #333333;
                border: 2px solid #4CAF50;
                border-radius: 4px;
                padding: 5px;
            }
            QLineEdit:focus {
                border-color: #8BC34A;
                /* Qt stylesheets don't directly support box-shadow, but can be achieved with custom painting */
                /* Here we use border color change to simulate glow effect */
            }
        """)
        layout.addWidget(glow_lineedit)
        
        self.main_layout.addLayout(layout)
    
    def create_custom_cursor_style_example(self):
        """Custom cursor style sheet example"""
        section_label = QLabel("Custom Cursor Styles")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # Custom cursor color
        cursor_lineedit = QLineEdit()
        cursor_lineedit.setPlaceholderText("Custom Cursor Color")
        cursor_lineedit.setStyleSheet("""
            QLineEdit {
                background-color: #FFFFFF;
                color: #333333;
                border: 2px solid #CCCCCC;
                border-radius: 4px;
                padding: 5px;
                /* Custom cursor color via caret-color property */
                caret-color: #F44336;
            }
        """)
        layout.addWidget(cursor_lineedit)
        
        # Big cursor line edit
        big_cursor_lineedit = QLineEdit()
        big_cursor_lineedit.setPlaceholderText("Big Cursor")
        big_cursor_lineedit.setStyleSheet("""
            QLineEdit {
                background-color: #FFFFFF;
                color: #333333;
                border: 2px solid #CCCCCC;
                border-radius: 4px;
                padding: 8px;
                font-size: 16px;
                caret-color: #2196F3;
            }
            /* Note: Qt stylesheets don't directly support setting cursor width */
            /* In real projects, you need to subclass QLineEdit and override paintEvent to implement this */
        """)
        layout.addWidget(big_cursor_lineedit)
        
        self.main_layout.addLayout(layout)
    
    def create_icon_style_example(self):
        """Line edit with icon style sheet example"""
        section_label = QLabel("Line Edit with Icon Styles")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # Line edit with left icon
        left_icon_lineedit = QLineEdit()
        left_icon_lineedit.setPlaceholderText("Search...")
        left_icon_lineedit.setStyleSheet("""
            QLineEdit {
                background-color: #FFFFFF;
                color: #333333;
                border: 2px solid #CCCCCC;
                border-radius: 4px;
                padding: 5px;
                padding-left: 30px;  /* Space for left icon */
                background-image: url(:/icons/search.png);  /* Use icon in real projects */
                background-repeat: no-repeat;
                background-position: left center;
                background-origin: content;
            }
            /* Since we don't have actual icon files, we simulate with Unicode symbols */
        """)
        # In real projects, you can add icons using QAction
        # action = QAction(self)
        # action.setIcon(QIcon("search.png"))
        # left_icon_lineedit.addAction(action, QLineEdit.LeadingPosition)
        layout.addWidget(left_icon_lineedit)
        
        # Line edit with right icon
        right_icon_lineedit = QLineEdit()
        right_icon_lineedit.setPlaceholderText("With Right Icon")
        right_icon_lineedit.setStyleSheet("""
            QLineEdit {
                background-color: #FFFFFF;
                color: #333333;
                border: 2px solid #CCCCCC;
                border-radius: 4px;
                padding: 5px;
                padding-right: 30px;  /* Space for right icon */
            }
        """)
        layout.addWidget(right_icon_lineedit)
        
        self.main_layout.addLayout(layout)
    
    def create_readonly_style_example(self):
        """Read-only state style sheet example"""
        section_label = QLabel("Read-only State Styles")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # Read-only line edit
        readonly_lineedit = QLineEdit()
        readonly_lineedit.setText("This is read-only text")
        readonly_lineedit.setReadOnly(True)
        readonly_lineedit.setStyleSheet("""
            QLineEdit {
                background-color: #F5F5F5;
                color: #757575;
                border: 2px solid #E0E0E0;
                border-radius: 4px;
                padding: 5px;
            }
            QLineEdit:read-only {
                background-color: #F5F5F5;
                color: #9E9E9E;
            }
        """)
        layout.addWidget(readonly_lineedit)
        
        # Disabled line edit
        disabled_lineedit = QLineEdit()
        disabled_lineedit.setText("This is disabled text")
        disabled_lineedit.setEnabled(False)
        disabled_lineedit.setStyleSheet("""
            QLineEdit {
                background-color: #FAFAFA;
                color: #BDBDBD;
                border: 2px solid #EEEEEE;
                border-radius: 4px;
                padding: 5px;
            }
            QLineEdit:disabled {
                background-color: #FAFAFA;
                color: #BDBDBD;
            }
        """)
        layout.addWidget(disabled_lineedit)
        
        self.main_layout.addLayout(layout)

# Startup function
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LineEditStylesWindow()
    window.show()
    sys.exit(app.exec())