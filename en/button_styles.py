#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
QPushButton Style Sheet Examples
This file demonstrates various style sheet usages for the QPushButton widget in Qt, with detailed comments for each style.
"""

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QWidget, 
    QPushButton, 
    QVBoxLayout, 
    QHBoxLayout, 
    QLabel
)
from PySide6.QtGui import QFont, QColor

class ButtonStylesWindow(QMainWindow):
    """QPushButton Style Sheet Example Window"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QPushButton Style Sheet Examples")
        self.resize(800, 600)
        
        # Create central widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        
        # Add title
        title_label = QLabel("QPushButton Style Sheet Examples")
        title_label.setAlignment(Qt.AlignCenter)
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title_label.setFont(title_font)
        self.main_layout.addWidget(title_label)
        
        # Create style sheet explanations and button examples
        self.create_basic_style_example()
        self.create_state_style_example()
        self.create_gradient_style_example()
        self.create_bordered_style_example()
        self.create_icon_style_example()
        self.create_custom_shapes_example()
        self.create_disabled_style_example()
    
    def create_basic_style_example(self):
        """Basic style sheet example"""
        section_label = QLabel("Basic Styles")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # Basic button style
        basic_button = QPushButton("Basic Style")
        basic_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;  /* Background color */
                color: white;              /* Text color */
                padding: 10px 20px;        /* Padding (top/bottom left/right) */
                font-size: 14px;           /* Font size */
                font-weight: normal;       /* Font weight */
            }
        """)
        layout.addWidget(basic_button)
        
        # Different colored buttons
        red_button = QPushButton("Red Button")
        red_button.setStyleSheet("""
            QPushButton {
                background-color: #f44336;  /* Red background */
                color: white;
                padding: 10px 20px;
            }
        """)
        layout.addWidget(red_button)
        
        blue_button = QPushButton("Blue Button")
        blue_button.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;  /* Blue background */
                color: white;
                padding: 10px 20px;
            }
        """)
        layout.addWidget(blue_button)
        
        self.main_layout.addLayout(layout)
    
    def create_state_style_example(self):
        """Button state style sheet example (normal, hover, pressed)"""
        section_label = QLabel("Button State Styles")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # Button with states
        state_button = QPushButton("Hover and Pressed Effects")
        state_button.setStyleSheet("""
            QPushButton {               /* Normal state */
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                border: none;            /* No border */
                font-size: 14px;
            }
            QPushButton:hover {         /* Hover state */
                background-color: #5CBF60;
                font-weight: bold;       /* Bold on hover */
            }
            QPushButton:pressed {       /* Pressed state */
                background-color: #3D8B40;
                padding-left: 12px;      /* Slight displacement when pressed */
                padding-top: 12px;
            }
        """)
        layout.addWidget(state_button)
        
        # Button with border state changes
        border_state_button = QPushButton("Border State Changes")
        border_state_button.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                padding: 10px 20px;
                border: 2px solid #1976D2;  /* Normal border */
            }
            QPushButton:hover {
                border-color: #BBDEFB;      /* Border color change on hover */
                border-width: 3px;          /* Border width increase on hover */
            }
            QPushButton:pressed {
                border-color: #0D47A1;      /* Border color change when pressed */
            }
        """)
        layout.addWidget(border_state_button)
        
        self.main_layout.addLayout(layout)
    
    def create_gradient_style_example(self):
        """Gradient background style sheet example"""
        section_label = QLabel("Gradient Background Styles")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # Linear gradient button
        linear_gradient_button = QPushButton("Linear Gradient")
        linear_gradient_button.setStyleSheet("""
            QPushButton {
                background: qlineargradient(
                    x1: 0, y1: 0,    /* Gradient start point */
                    x2: 1, y2: 0,    /* Gradient end point */
                    stop: 0 #4CAF50, /* Start color */
                    stop: 1 #8BC34A  /* End color */
                );
                color: white;
                padding: 10px 20px;
                border: none;
            }
        """)
        layout.addWidget(linear_gradient_button)
        
        # Radial gradient button
        radial_gradient_button = QPushButton("Radial Gradient")
        radial_gradient_button.setStyleSheet("""
            QPushButton {
                background: qradialgradient(
                    cx: 0.5, cy: 0.5,    /* Center point */
                    radius: 0.5,         /* Radius */
                    fx: 0.5, fy: 0.5,    /* Focus point */
                    stop: 0 #FF5722,     /* Center color */
                    stop: 1 #E64A19      /* Edge color */
                );
                color: white;
                padding: 10px 20px;
                border: none;
            }
        """)
        layout.addWidget(radial_gradient_button)
        
        self.main_layout.addLayout(layout)
    
    def create_bordered_style_example(self):
        """Border style sheet example"""
        section_label = QLabel("Border Styles")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # Rounded button
        rounded_button = QPushButton("Rounded Button")
        rounded_button.setStyleSheet("""
            QPushButton {
                background-color: #9C27B0;
                color: white;
                padding: 10px 20px;
                border-radius: 15px;     /* Border radius */
                border: 2px solid #7B1FA2;
            }
        """)
        layout.addWidget(rounded_button)
        
        # Dashed border button
        dashed_button = QPushButton("Dashed Border")
        dashed_button.setStyleSheet("""
            QPushButton {
                background-color: #FF9800;
                color: white;
                padding: 10px 20px;
                border-radius: 5px;
                border: 2px dashed #E65100;  /* Dashed border */
            }
        """)
        layout.addWidget(dashed_button)
        
        # Double border button
        double_border_button = QPushButton("Double Border")
        double_border_button.setStyleSheet("""
            QPushButton {
                background-color: #00BCD4;
                color: white;
                padding: 10px 20px;
                border-radius: 5px;
                border: 2px solid #006064;
                /* Use pseudo-element for double border effect */
                border-style: outset;
            }
        """)
        layout.addWidget(double_border_button)
        
        self.main_layout.addLayout(layout)
    
    def create_icon_style_example(self):
        """Icon button style sheet example"""
        section_label = QLabel("Icon Button Styles")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # Button with icon (using Unicode symbols instead of actual icons here)
        icon_button = QPushButton("🔍 Search")
        icon_button.setStyleSheet("""
            QPushButton {
                background-color: #607D8B;
                color: white;
                padding: 10px 20px;
                border-radius: 5px;
                text-align: left;         /* Text left-aligned */
                padding-left: 30px;       /* Space for icon on the left */
            }
            /* Note: In actual projects, it's recommended to use QIcon to set icons instead of relying on Unicode symbols */
        """)
        layout.addWidget(icon_button)
        
        # Button with separate icon and text
        split_button = QPushButton("Details ⋯")
        split_button.setStyleSheet("""
            QPushButton {
                background-color: #3F51B5;
                color: white;
                padding: 10px 20px;
                border-radius: 5px;
                text-align: left;         /* Text left-aligned */
            }
        """)
        layout.addWidget(split_button)
        
        self.main_layout.addLayout(layout)
    
    def create_custom_shapes_example(self):
        """Custom shape button style sheet example"""
        section_label = QLabel("Custom Shapes")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # Circular button
        circle_button = QPushButton("+")
        circle_button.setFixedSize(50, 50)  # Set fixed size to make button circular
        circle_button.setStyleSheet("""
            QPushButton {
                background-color: #F44336;
                color: white;
                border-radius: 25px;      /* Radius half of width */
                border: none;
                font-size: 20px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #D32F2F;
            }
            QPushButton:pressed {
                background-color: #B71C1C;
            }
        """)
        layout.addWidget(circle_button)
        
        # Capsule shape button
        capsule_button = QPushButton("Capsule Shape")
        capsule_button.setStyleSheet("""
            QPushButton {
                background-color: #009688;
                color: white;
                padding: 8px 25px;
                border-radius: 20px;      /* Larger border radius */
                border: none;
            }
        """)
        layout.addWidget(capsule_button)
        
        self.main_layout.addLayout(layout)
    
    def create_disabled_style_example(self):
        """Disabled state style sheet example"""
        section_label = QLabel("Disabled State Styles")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # Comparison of normal and disabled buttons
        enabled_button = QPushButton("Enabled Button")
        enabled_button.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                padding: 10px 20px;
            }
        """)
        layout.addWidget(enabled_button)
        
        disabled_button = QPushButton("Disabled Button")
        disabled_button.setEnabled(False)  # Set to disabled state
        disabled_button.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                padding: 10px 20px;
            }
            QPushButton:disabled {
                background-color: #BDBDBD;  /* Background color when disabled */
                color: #757575;             /* Text color when disabled */
                opacity: 0.6;               /* Opacity */
            }
        """)
        layout.addWidget(disabled_button)
        
        self.main_layout.addLayout(layout)

# Startup function
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ButtonStylesWindow()
    window.show()
    sys.exit(app.exec())