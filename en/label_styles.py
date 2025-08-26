#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
QLabel Style Sheet Example
This file demonstrates various stylesheet usages for the QLabel widget in Qt, with detailed comments for each style.
"""

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QWidget, 
    QLabel, 
    QVBoxLayout, 
    QHBoxLayout,
    QGridLayout
)
from PySide6.QtGui import QFont, QColor

class LabelStylesWindow(QMainWindow):
    """QLabel stylesheet example window"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QLabel Style Sheet Example")
        self.resize(800, 600)
        
        # Create central widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        
        # Add title
        title_label = QLabel("QLabel Style Sheet Example")
        title_label.setAlignment(Qt.AlignCenter)
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title_label.setFont(title_font)
        self.main_layout.addWidget(title_label)
        
        # Create stylesheet explanations and label examples
        self.create_basic_style_example()
        self.create_font_style_example()
        self.create_background_style_example()
        self.create_border_style_example()
        self.create_shadow_style_example()
        self.create_gradient_style_example()
        self.create_html_style_example()
        self.create_image_style_example()
    
    def create_basic_style_example(self):
        """Basic style sheet example"""
        section_label = QLabel("Basic Styles")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # Default label
        default_label = QLabel("Default Label")
        layout.addWidget(default_label)
        
        # Text color label
        color_label = QLabel("Red Text")
        color_label.setStyleSheet("color: #f44336;")
        layout.addWidget(color_label)
        
        # Background color label
        bg_color_label = QLabel("Blue Background")
        bg_color_label.setStyleSheet("background-color: #2196F3; color: white;")
        layout.addWidget(bg_color_label)
        
        self.main_layout.addLayout(layout)
    
    def create_font_style_example(self):
        """Font style sheet example"""
        section_label = QLabel("Font Styles")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QGridLayout()
        
        # Different font sizes
        small_font_label = QLabel("Small Font")
        small_font_label.setStyleSheet("font-size: 10px;")
        layout.addWidget(small_font_label, 0, 0)
        
        medium_font_label = QLabel("Medium Font")
        medium_font_label.setStyleSheet("font-size: 16px;")
        layout.addWidget(medium_font_label, 0, 1)
        
        large_font_label = QLabel("Large Font")
        large_font_label.setStyleSheet("font-size: 24px;")
        layout.addWidget(large_font_label, 0, 2)
        
        # Different font weights
        normal_label = QLabel("Normal Weight")
        layout.addWidget(normal_label, 1, 0)
        
        bold_label = QLabel("Bold Weight")
        bold_label.setStyleSheet("font-weight: bold;")
        layout.addWidget(bold_label, 1, 1)
        
        italic_label = QLabel("Italic Style")
        italic_label.setStyleSheet("font-style: italic;")
        layout.addWidget(italic_label, 1, 2)
        
        # Different font families
        serif_label = QLabel("Serif Font")
        serif_label.setStyleSheet("font-family: 'Times New Roman', serif;")
        layout.addWidget(serif_label, 2, 0)
        
        sans_serif_label = QLabel("Sans-serif Font")
        sans_serif_label.setStyleSheet("font-family: Arial, sans-serif;")
        layout.addWidget(sans_serif_label, 2, 1)
        
        monospace_label = QLabel("Monospace Font")
        monospace_label.setStyleSheet("font-family: 'Courier New', monospace;")
        layout.addWidget(monospace_label, 2, 2)
        
        self.main_layout.addLayout(layout)
    
    def create_background_style_example(self):
        """Background style sheet example"""
        section_label = QLabel("Background Styles")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # Label with padding
        padding_label = QLabel("Label with Padding")
        padding_label.setStyleSheet("""
            background-color: #4CAF50;
            color: white;
            padding: 15px;  /* Padding all around */
        """)
        layout.addWidget(padding_label)
        
        # Label with different padding
        different_padding_label = QLabel("Different Padding")
        different_padding_label.setStyleSheet("""
            background-color: #FF9800;
            color: white;
            padding-top: 5px;
            padding-right: 15px;
            padding-bottom: 10px;
            padding-left: 20px;
        """)
        layout.addWidget(different_padding_label)
        
        self.main_layout.addLayout(layout)
    
    def create_border_style_example(self):
        """Border style sheet example"""
        section_label = QLabel("Border Styles")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # Solid border label
        solid_border_label = QLabel("Solid Border")
        solid_border_label.setStyleSheet("""
            border: 2px solid #2196F3;
            padding: 10px;
        """)
        layout.addWidget(solid_border_label)
        
        # Dashed border label
        dashed_border_label = QLabel("Dashed Border")
        dashed_border_label.setStyleSheet("""
            border: 2px dashed #f44336;
            padding: 10px;
        """)
        layout.addWidget(dashed_border_label)
        
        # Rounded border label
        rounded_label = QLabel("Rounded Border")
        rounded_label.setStyleSheet("""
            background-color: #9C27B0;
            color: white;
            border-radius: 10px;
            padding: 10px;
        """)
        layout.addWidget(rounded_label)
        
        # No border but with background color
        no_border_label = QLabel("Background Without Border")
        no_border_label.setStyleSheet("""
            background-color: #FFEB3B;
            color: #333;
            padding: 10px;
        """)
        layout.addWidget(no_border_label)
        
        self.main_layout.addLayout(layout)
    
    def create_shadow_style_example(self):
        """Shadow effect style sheet example"""
        section_label = QLabel("Shadow Effects")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # Text shadow label
        text_shadow_label = QLabel("Text Shadow")
        text_shadow_label.setStyleSheet("""
            color: white;
            background-color: #3F51B5;
            padding: 10px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);  /* Horizontal offset, vertical offset, blur radius, color */
            font-size: 16px;
            font-weight: bold;
        """)
        layout.addWidget(text_shadow_label)
        
        # Box shadow label
        box_shadow_label = QLabel("Box Shadow")
        box_shadow_label.setStyleSheet("""
            background-color: #4CAF50;
            color: white;
            padding: 10px;
            border-radius: 5px;
            /* Note: Qt stylesheets don't directly support box-shadow, but you can achieve similar effects */
            /* with QFrame's shadow properties or custom painting */
            /* Here we use border color to simulate a simple shadow effect */
            border: 1px solid rgba(0, 0, 0, 0.2);
        """)
        layout.addWidget(box_shadow_label)
        
        self.main_layout.addLayout(layout)
    
    def create_gradient_style_example(self):
        """Gradient background style sheet example"""
        section_label = QLabel("Gradient Backgrounds")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # Horizontal linear gradient label
        horizontal_gradient_label = QLabel("Horizontal Gradient")
        horizontal_gradient_label.setStyleSheet("""
            background: qlineargradient(
                x1: 0, y1: 0,    /* Gradient start point */
                x2: 1, y2: 0,    /* Gradient end point */
                stop: 0 #FF9800, /* Start color */
                stop: 1 #E91E63  /* End color */
            );
            color: white;
            padding: 15px;
            font-size: 16px;
            font-weight: bold;
        """)
        layout.addWidget(horizontal_gradient_label)
        
        # Vertical linear gradient label
        vertical_gradient_label = QLabel("Vertical Gradient")
        vertical_gradient_label.setStyleSheet("""
            background: qlineargradient(
                x1: 0, y1: 0,    /* Gradient start point */
                x2: 0, y2: 1,    /* Gradient end point */
                stop: 0 #2196F3, /* Start color */
                stop: 1 #00BCD4  /* End color */
            );
            color: white;
            padding: 15px;
            font-size: 16px;
            font-weight: bold;
        """)
        layout.addWidget(vertical_gradient_label)
        
        # Radial gradient label
        radial_gradient_label = QLabel("Radial Gradient")
        radial_gradient_label.setStyleSheet("""
            background: qradialgradient(
                cx: 0.5, cy: 0.5,    /* Center point */
                radius: 0.5,         /* Radius */
                fx: 0.5, fy: 0.5,    /* Focus point */
                stop: 0 #9C27B0,     /* Center color */
                stop: 1 #673AB7      /* Edge color */
            );
            color: white;
            padding: 15px;
            font-size: 16px;
            font-weight: bold;
        """)
        layout.addWidget(radial_gradient_label)
        
        self.main_layout.addLayout(layout)
    
    def create_html_style_example(self):
        """HTML style sheet example"""
        section_label = QLabel("HTML Styles")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QVBoxLayout()
        
        # Text with HTML tags
        html_label = QLabel()
        html_label.setText("""
            <html>
            <head></head>
            <body>
                <p>This is <strong>bold</strong> text, this is <em>italic</em> text, this is <u>underlined</u> text.</p>
                <p><font color="#f44336">Red</font>, <font color="#2196F3">blue</font>, <font color="#4CAF50">green</font> text.</p>
                <p><font size="5">Large font</font> and <font size="2">small font</font>.</p>
            </body>
            </html>
        """)
        html_label.setStyleSheet("padding: 10px;")
        layout.addWidget(html_label)
        
        # Combining stylesheets with HTML
        mixed_label = QLabel()
        mixed_label.setText("<html><body><p>Stylesheet + HTML</p></body></html>")
        mixed_label.setStyleSheet("""
            background-color: #00BCD4;
            color: white;
            padding: 10px;
            font-size: 18px;
        """)
        layout.addWidget(mixed_label)
        
        self.main_layout.addLayout(layout)
    
    def create_image_style_example(self):
        """Image style sheet example"""
        section_label = QLabel("Image Backgrounds")
        section_label.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        self.main_layout.addWidget(section_label)
        
        layout = QHBoxLayout()
        
        # Label with image background
        # Note: Since we don't have actual image files, we use gradients to simulate
        # In real projects, you can use the background-image property to set image backgrounds
        image_bg_label = QLabel("Label with Background Image")
        image_bg_label.setStyleSheet("""
            background: qlineargradient(
                x1: 0, y1: 0, x2: 1, y2: 1,
                stop: 0 #FFC107, stop: 1 #FF5722
            );
            color: white;
            padding: 20px;
            font-weight: bold;
            /* In real projects, use the following code to set image background */
            /* background-image: url('path/to/image.png'); */
            /* background-repeat: no-repeat; */
            /* background-position: center; */
        """)
        layout.addWidget(image_bg_label)
        
        # Semi-transparent background label
        transparent_label = QLabel("Semi-transparent Background")
        transparent_label.setStyleSheet("""
            background-color: rgba(0, 150, 136, 0.5);  /* RGBA color, last parameter is opacity */
            color: white;
            padding: 20px;
            border: 2px solid #009688;
        """)
        layout.addWidget(transparent_label)
        
        self.main_layout.addLayout(layout)

# Startup function
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LabelStylesWindow()
    window.show()
    sys.exit(app.exec())