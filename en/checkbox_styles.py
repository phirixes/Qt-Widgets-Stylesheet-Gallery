#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
QCheckBox Style Sheet Examples
This file demonstrates various style sheet usages for the QCheckBox widget in Qt, with detailed comments for each style.
"""

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QWidget, 
    QCheckBox, 
    QVBoxLayout, 
    QHBoxLayout, 
    QLabel
)
from PySide6.QtGui import QFont, QColor

class CheckBoxStylesWindow(QMainWindow):
    """QCheckBox Style Sheet Example Window"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QCheckBox Style Sheet Examples")
        self.resize(800, 600)
        
        # Create central widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        
        # Add title
        title_label = QLabel("QCheckBox Style Sheet Examples")
        title_label.setAlignment(Qt.AlignCenter)
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title_label.setFont(title_font)
        self.main_layout.addWidget(title_label)
        
        # Create style sheet explanations and checkbox examples
        self.create_basic_style_example()
        self.create_state_style_example()
        self.create_custom_indicator_style_example()
        self.create_gradient_style_example()
        self.create_flat_style_example()
        self.create_radio_button_style_example()
        self.create_size_style_example()
    
    def create_basic_style_example(self):
        """Basic style sheet example"""
        section_label = QLabel("Basic Styles")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # Default checkbox
        default_checkbox = QCheckBox("Default Checkbox")
        layout.addWidget(default_checkbox)
        
        # Basic style checkbox
        basic_checkbox = QCheckBox("Basic Style")
        basic_checkbox.setStyleSheet("""
            QCheckBox {
                color: #333333;
                font-size: 14px;
            }
            QCheckBox::indicator {
                width: 20px;
                height: 20px;
                border: 2px solid #CCCCCC;
                border-radius: 3px;
            }
            QCheckBox::indicator:checked {
                background-color: #2196F3;
                border-color: #2196F3;
            }
        """)
        layout.addWidget(basic_checkbox)
        
        self.main_layout.addLayout(layout)
    
    def create_state_style_example(self):
        """State style sheet example (normal, checked, hover)"""
        section_label = QLabel("State Styles")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # State style checkbox
        state_checkbox = QCheckBox("State Styles")
        state_checkbox.setStyleSheet("""
            QCheckBox {
                color: #333333;
                font-size: 14px;
            }
            QCheckBox::indicator {
                width: 20px;
                height: 20px;
                border: 2px solid #CCCCCC;
                border-radius: 3px;
                background-color: white;
            }
            QCheckBox::indicator:hover {
                border-color: #999999;
            }
            QCheckBox::indicator:checked {
                background-color: #4CAF50;
                border-color: #4CAF50;
            }
            QCheckBox::indicator:checked:hover {
                background-color: #66BB6A;
            }
            QCheckBox::indicator:unchecked:disabled {
                background-color: #F5F5F5;
                border-color: #E0E0E0;
            }
            QCheckBox::indicator:checked:disabled {
                background-color: #E8F5E9;
                border-color: #C8E6C9;
            }
        """)
        layout.addWidget(state_checkbox)
        
        # Disabled state checkbox
        disabled_checkbox = QCheckBox("Disabled State")
        disabled_checkbox.setEnabled(False)
        disabled_checkbox.setChecked(True)
        disabled_checkbox.setStyleSheet("""
            QCheckBox {
                color: #9E9E9E;
            }
            QCheckBox::indicator {
                width: 20px;
                height: 20px;
                border: 2px solid #E0E0E0;
                border-radius: 3px;
            }
            QCheckBox::indicator:checked:disabled {
                background-color: #E8F5E9;
                border-color: #C8E6C9;
            }
        """)
        layout.addWidget(disabled_checkbox)
        
        self.main_layout.addLayout(layout)
    
    def create_custom_indicator_style_example(self):
        """Custom indicator style sheet example"""
        section_label = QLabel("Custom Indicator Styles")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # Circular indicator checkbox
        circle_checkbox = QCheckBox("Circular Indicator")
        circle_checkbox.setStyleSheet("""
            QCheckBox {
                color: #333333;
                font-size: 14px;
            }
            QCheckBox::indicator {
                width: 22px;
                height: 22px;
                border: 2px solid #F44336;
                border-radius: 11px;  /* Half of width */
                background-color: white;
            }
            QCheckBox::indicator:checked {
                background-color: #F44336;
            }
        """)
        layout.addWidget(circle_checkbox)
        
        # Checkbox with custom checkmark
        checkmark_checkbox = QCheckBox("Custom Checkmark")
        checkmark_checkbox.setStyleSheet("""
            QCheckBox {
                color: #333333;
                font-size: 14px;
            }
            QCheckBox::indicator {
                width: 20px;
                height: 20px;
                border: 2px solid #2196F3;
                border-radius: 3px;
                background-color: white;
            }
            QCheckBox::indicator:checked {
                background-color: #2196F3;
            }
            /* Qt style sheets do not directly support custom checkmark shapes */
            /* In actual projects, this requires subclassing QCheckBox or using images */
        """)
        layout.addWidget(checkmark_checkbox)
        
        self.main_layout.addLayout(layout)
    
    def create_gradient_style_example(self):
        """Gradient background style sheet example"""
        section_label = QLabel("Gradient Background Styles")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # Gradient background checkbox
        gradient_checkbox = QCheckBox("Gradient Background")
        gradient_checkbox.setStyleSheet("""
            QCheckBox {
                color: #333333;
                font-size: 14px;
            }
            QCheckBox::indicator {
                width: 20px;
                height: 20px;
                border: 2px solid #9C27B0;
                border-radius: 3px;
                background-color: white;
            }
            QCheckBox::indicator:checked {
                background: qlineargradient(
                    x1: 0, y1: 0,    /* Gradient start point */
                    x2: 1, y2: 1,    /* Gradient end point */
                    stop: 0 #9C27B0, /* Start color */
                    stop: 1 #673AB7  /* End color */
                );
            }
        """)
        layout.addWidget(gradient_checkbox)
        
        # Glow effect checkbox
        glow_checkbox = QCheckBox("Glow Effect")
        glow_checkbox.setStyleSheet("""
            QCheckBox {
                color: #333333;
                font-size: 14px;
            }
            QCheckBox::indicator {
                width: 20px;
                height: 20px;
                border: 2px solid #FF9800;
                border-radius: 3px;
                background-color: white;
            }
            QCheckBox::indicator:checked {
                background-color: #FF9800;
                /* Qt style sheets do not directly support box-shadow, but can be implemented with custom painting */
            }
        """)
        layout.addWidget(glow_checkbox)
        
        self.main_layout.addLayout(layout)
    
    def create_flat_style_example(self):
        """Flat style sheet example"""
        section_label = QLabel("Flat Styles")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # Flat style checkbox
        flat_checkbox = QCheckBox("Flat Style")
        flat_checkbox.setStyleSheet("""
            QCheckBox {
                color: #333333;
                font-size: 14px;
            }
            QCheckBox::indicator {
                width: 18px;
                height: 18px;
                border: 2px solid #607D8B;
                border-radius: 2px;
                background-color: white;
            }
            QCheckBox::indicator:checked {
                background-color: #607D8B;
            }
        """)
        layout.addWidget(flat_checkbox)
        
        # Minimalist style checkbox
        minimal_checkbox = QCheckBox("Minimalist Style")
        minimal_checkbox.setStyleSheet("""
            QCheckBox {
                color: #212121;
                font-size: 14px;
            }
            QCheckBox::indicator {
                width: 16px;
                height: 16px;
                border: 1px solid #757575;
                border-radius: 0;
                background-color: white;
            }
            QCheckBox::indicator:checked {
                background-color: #212121;
            }
        """)
        layout.addWidget(minimal_checkbox)
        
        self.main_layout.addLayout(layout)
    
    def create_radio_button_style_example(self):
        """Radio button style checkbox"""
        section_label = QLabel("Radio Button Style")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # Circular radio button style checkbox
        radio_style_checkbox = QCheckBox("Radio Button Style")
        radio_style_checkbox.setStyleSheet("""
            QCheckBox {
                color: #333333;
                font-size: 14px;
            }
            QCheckBox::indicator {
                width: 20px;
                height: 20px;
                border: 2px solid #00BCD4;
                border-radius: 10px;
                background-color: white;
            }
            QCheckBox::indicator:checked {
                background-color: #00BCD4;
                /* In actual projects, you can add a custom-drawn dot */
            }
        """)
        layout.addWidget(radio_style_checkbox)
        
        # Radio style checkbox with dot
        dot_radio_checkbox = QCheckBox("Radio Style with Dot")
        dot_radio_checkbox.setStyleSheet("""
            QCheckBox {
                color: #333333;
                font-size: 14px;
            }
            QCheckBox::indicator {
                width: 20px;
                height: 20px;
                border: 2px solid #4CAF50;
                border-radius: 10px;
                background-color: white;
            }
            QCheckBox::indicator:checked {
                background-color: white;
                border-color: #4CAF50;
                /* Qt style sheets do not directly support drawing dots inside indicators */
                /* In actual projects, this requires subclassing QCheckBox */
            }
        """)
        layout.addWidget(dot_radio_checkbox)
        
        self.main_layout.addLayout(layout)
    
    def create_size_style_example(self):
        """Size and spacing style sheet example"""
        section_label = QLabel("Size and Spacing Styles")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # Small checkbox
        small_checkbox = QCheckBox("Small Checkbox")
        small_checkbox.setStyleSheet("""
            QCheckBox {
                color: #333333;
                font-size: 12px;
            }
            QCheckBox::indicator {
                width: 14px;
                height: 14px;
                border: 1px solid #CCCCCC;
                border-radius: 2px;
            }
            QCheckBox::indicator:checked {
                background-color: #9E9E9E;
            }
        """)
        layout.addWidget(small_checkbox)
        
        # Large checkbox
        large_checkbox = QCheckBox("Large Checkbox")
        large_checkbox.setStyleSheet("""
            QCheckBox {
                color: #333333;
                font-size: 18px;
            }
            QCheckBox::indicator {
                width: 24px;
                height: 24px;
                border: 2px solid #FF5722;
                border-radius: 4px;
            }
            QCheckBox::indicator:checked {
                background-color: #FF5722;
            }
        """)
        layout.addWidget(large_checkbox)
        
        self.main_layout.addLayout(layout)

# Startup function
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CheckBoxStylesWindow()
    window.show()
    sys.exit(app.exec())