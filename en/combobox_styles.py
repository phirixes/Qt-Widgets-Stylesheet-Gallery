#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
QComboBox Style Sheet Examples
This file demonstrates various style sheet usages for the QComboBox widget in Qt, with detailed comments for each style.
"""

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QWidget, 
    QComboBox, 
    QVBoxLayout, 
    QHBoxLayout, 
    QLabel
)
from PySide6.QtGui import QFont, QColor

class ComboBoxStylesWindow(QMainWindow):
    """QComboBox Style Sheet Example Window"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QComboBox Style Sheet Examples")
        self.resize(800, 600)
        
        # Create central widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        
        # Add title
        title_label = QLabel("QComboBox Style Sheet Examples")
        title_label.setAlignment(Qt.AlignCenter)
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title_label.setFont(title_font)
        self.main_layout.addWidget(title_label)
        
        # Create style sheet explanations and combobox examples
        self.create_basic_style_example()
        self.create_editable_style_example()
        self.create_gradient_style_example()
        self.create_custom_arrow_style_example()
        self.create_dropdown_style_example()
        self.create_state_style_example()
        self.create_size_style_example()
    
    def create_basic_style_example(self):
        """Basic style sheet example"""
        section_label = QLabel("Basic Styles")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # Default combobox
        default_combobox = QComboBox()
        default_combobox.addItems(["Option 1", "Option 2", "Option 3"])
        layout.addWidget(default_combobox)
        
        # Basic style combobox
        basic_combobox = QComboBox()
        basic_combobox.addItems(["Option 1", "Option 2", "Option 3"])
        basic_combobox.setStyleSheet("""
            QComboBox {
                background-color: #4CAF50;
                color: white;
                padding: 5px;
                border: 1px solid #388E3C;
                border-radius: 4px;
            }
        """)
        layout.addWidget(basic_combobox)
        
        self.main_layout.addLayout(layout)
    
    def create_editable_style_example(self):
        """Editable combobox style sheet example"""
        section_label = QLabel("Editable ComboBox Styles")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # Editable combobox
        editable_combobox = QComboBox()
        editable_combobox.setEditable(True)
        editable_combobox.addItems(["Option 1", "Option 2", "Option 3"])
        editable_combobox.setStyleSheet("""
            QComboBox {
                background-color: #2196F3;
                color: white;
                padding: 5px;
                border: 1px solid #1976D2;
                border-radius: 4px;
            }
            QComboBox::edit {
                background-color: #FFFFFF;
                color: #000000;
                selection-background-color: #2196F3;
                selection-color: white;
            }
        """)
        layout.addWidget(editable_combobox)
        
        self.main_layout.addLayout(layout)
    
    def create_gradient_style_example(self):
        """Gradient background style sheet example"""
        section_label = QLabel("Gradient Background Styles")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # Linear gradient combobox
        gradient_combobox = QComboBox()
        gradient_combobox.addItems(["Option 1", "Option 2", "Option 3"])
        gradient_combobox.setStyleSheet("""
            QComboBox {
                background: qlineargradient(
                    x1: 0, y1: 0,    /* Gradient start point */
                    x2: 1, y2: 0,    /* Gradient end point */
                    stop: 0 #FF9800, /* Start color */
                    stop: 1 #E91E63  /* End color */
                );
                color: white;
                padding: 5px;
                border: none;
                border-radius: 4px;
            }
        """)
        layout.addWidget(gradient_combobox)
        
        # Vertical linear gradient combobox
        vertical_gradient_combobox = QComboBox()
        vertical_gradient_combobox.addItems(["Option 1", "Option 2", "Option 3"])
        vertical_gradient_combobox.setStyleSheet("""
            QComboBox {
                background: qlineargradient(
                    x1: 0, y1: 0,    /* Gradient start point */
                    x2: 0, y2: 1,    /* Gradient end point */
                    stop: 0 #9C27B0, /* Start color */
                    stop: 1 #673AB7  /* End color */
                );
                color: white;
                padding: 5px;
                border: none;
                border-radius: 4px;
            }
        """)
        layout.addWidget(vertical_gradient_combobox)
        
        self.main_layout.addLayout(layout)
    
    def create_custom_arrow_style_example(self):
        """Custom arrow style sheet example"""
        section_label = QLabel("Custom Arrow Styles")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # Custom arrow combobox
        custom_arrow_combobox = QComboBox()
        custom_arrow_combobox.addItems(["Option 1", "Option 2", "Option 3"])
        custom_arrow_combobox.setStyleSheet("""
            QComboBox {
                background-color: #FF5722;
                color: white;
                padding: 5px;
                padding-right: 25px;  /* Space for arrow */
                border: none;
                border-radius: 4px;
            }
            QComboBox::down-arrow {
                image: url(:/icons/down_arrow.png);  /* Use image in actual projects */
                width: 12px;
                height: 12px;
                /* Using color simulation since no actual image is available */
                color: white;
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 20px;
                border-left-width: 1px;
                border-left-color: rgba(255, 255, 255, 0.3);
                border-left-style: solid;
            }
        """)
        layout.addWidget(custom_arrow_combobox)
        
        # Round dropdown button
        round_arrow_combobox = QComboBox()
        round_arrow_combobox.addItems(["Option 1", "Option 2", "Option 3"])
        round_arrow_combobox.setStyleSheet("""
            QComboBox {
                background-color: #009688;
                color: white;
                padding: 5px;
                padding-right: 30px;
                border: none;
                border-radius: 15px;
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 20px;
                height: 20px;
                border-radius: 10px;
                background-color: rgba(255, 255, 255, 0.2);
            }
            QComboBox::down-arrow {
                image: url(:/icons/down_arrow.png);
                width: 10px;
                height: 10px;
                color: white;
            }
        """)
        layout.addWidget(round_arrow_combobox)
        
        self.main_layout.addLayout(layout)
    
    def create_dropdown_style_example(self):
        """Dropdown list style sheet example"""
        section_label = QLabel("Dropdown List Styles")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # Custom dropdown list style
        dropdown_combobox = QComboBox()
        dropdown_combobox.addItems(["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"])
        dropdown_combobox.setStyleSheet("""
            QComboBox {
                background-color: #607D8B;
                color: white;
                padding: 5px;
                border: none;
                border-radius: 4px;
            }
            QComboBox::drop-down {
                border-left: 1px solid rgba(255, 255, 255, 0.3);
            }
            QComboBox::down-arrow {
                color: white;
            }
            QComboBox QAbstractItemView {
                background-color: #455A64;
                color: white;
                border: 1px solid #607D8B;
                selection-background-color: #607D8B;
                selection-color: white;
                outline: none;
            }
            QComboBox QAbstractItemView::item {
                padding: 5px 10px;
                height: 30px;
            }
            QComboBox QAbstractItemView::item:hover {
                background-color: #546E7A;
            }
        """)
        layout.addWidget(dropdown_combobox)
        
        # Alternative dropdown list style
        alternate_dropdown_combobox = QComboBox()
        alternate_dropdown_combobox.addItems(["Option 1", "Option 2", "Option 3"])
        alternate_dropdown_combobox.setStyleSheet("""
            QComboBox {
                background-color: #795548;
                color: white;
                padding: 5px;
                border: 1px solid #6D4C41;
                border-radius: 4px;
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
            }
            QComboBox QAbstractItemView {
                background-color: #8D6E63;
                color: white;
                border: 1px solid #6D4C41;
                selection-background-color: #5D4037;
            }
        """)
        layout.addWidget(alternate_dropdown_combobox)
        
        self.main_layout.addLayout(layout)
    
    def create_state_style_example(self):
        """State style sheet example"""
        section_label = QLabel("State Styles")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # Hover and focus state styles
        state_combobox = QComboBox()
        state_combobox.addItems(["Option 1", "Option 2", "Option 3"])
        state_combobox.setStyleSheet("""
            QComboBox {
                background-color: #3F51B5;
                color: white;
                padding: 5px;
                border: 2px solid transparent;
                border-radius: 4px;
            }
            QComboBox:hover {
                border-color: #7986CB;
                background-color: #5C6BC0;
            }
            QComboBox:focus {
                border-color: #2196F3;
                background-color: #3949AB;
            }
            QComboBox:disabled {
                background-color: #BDBDBD;
                color: #757575;
            }
        """)
        layout.addWidget(state_combobox)
        
        # Disabled state combobox
        disabled_combobox = QComboBox()
        disabled_combobox.addItems(["Option 1", "Option 2", "Option 3"])
        disabled_combobox.setEnabled(False)
        disabled_combobox.setStyleSheet("""
            QComboBox {
                background-color: #E0E0E0;
                color: #9E9E9E;
                padding: 5px;
                border: 1px solid #BDBDBD;
                border-radius: 4px;
            }
        """)
        layout.addWidget(disabled_combobox)
        
        self.main_layout.addLayout(layout)
    
    def create_size_style_example(self):
        """Size and spacing style sheet example"""
        section_label = QLabel("Size and Spacing Styles")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # Small combobox
        small_combobox = QComboBox()
        small_combobox.addItems(["Option 1", "Option 2", "Option 3"])
        small_combobox.setStyleSheet("""
            QComboBox {
                background-color: #F44336;
                color: white;
                padding: 3px;
                font-size: 12px;
                border: none;
                border-radius: 3px;
            }
        """)
        layout.addWidget(small_combobox)
        
        # Large combobox
        large_combobox = QComboBox()
        large_combobox.addItems(["Option 1", "Option 2", "Option 3"])
        large_combobox.setStyleSheet("""
            QComboBox {
                background-color: #00BCD4;
                color: white;
                padding: 8px;
                font-size: 16px;
                border: none;
                border-radius: 6px;
            }
        """)
        layout.addWidget(large_combobox)
        
        # Wide combobox
        wide_combobox = QComboBox()
        wide_combobox.addItems(["Option 1", "Option 2", "Option 3"])
        wide_combobox.setMinimumWidth(200)
        wide_combobox.setStyleSheet("""
            QComboBox {
                background-color: #8BC34A;
                color: white;
                padding: 5px;
                border: none;
                border-radius: 4px;
            }
        """)
        layout.addWidget(wide_combobox)
        
        self.main_layout.addLayout(layout)

# Startup function
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ComboBoxStylesWindow()
    window.show()
    sys.exit(app.exec())