#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
QRadioButton Styles Example
This file demonstrates various styles for QRadioButton widgets using Qt Style Sheets.
It includes different visual designs such as basic, filled, square, neon effect,
flat style, colored, custom size, and icon radio buttons.
"""

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,QRadioButton, QComboBox, QLabel
from PySide6.QtCore import Qt

class RadioButtonStylesWindow(QMainWindow):
    """Main window for showcasing QRadioButton styles"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QRadioButton Styles Example")
        self.setGeometry(100, 100, 800, 600)
        
        # Main widget and layout
        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)
        self.setCentralWidget(main_widget)
        
        # Title label
        title_label = QLabel("QRadioButton Style Examples")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; color: #333;")
        main_layout.addWidget(title_label)
        
        # Style selection combo box
        style_layout = QHBoxLayout()
        style_label = QLabel("Select Style:")
        self.style_combo = QComboBox()
        self.style_combo.addItems([
            "Basic Radio Button",
            "Filled Circle Radio Button",
            "Square Radio Button",
            "Neon Effect Radio Button",
            "Flat Style Radio Button",
            "Colored Radio Button",
            "Custom Size Radio Button",
            "Icon Radio Button"
        ])
        self.style_combo.currentIndexChanged.connect(self.update_radiobutton_style)
        
        style_layout.addWidget(style_label)
        style_layout.addWidget(self.style_combo)
        style_layout.addStretch()
        main_layout.addLayout(style_layout)
        
        # Reset button layout
        reset_layout = QHBoxLayout()
        self.reset_btn = QRadioButton("Reset Selection")
        self.reset_btn.toggled.connect(self.reset_selection)
        reset_layout.addWidget(self.reset_btn)
        reset_layout.addStretch()
        main_layout.addLayout(reset_layout)
        
        # Radio button container layout
        self.radiobutton_layout = QVBoxLayout()
        main_layout.addLayout(self.radiobutton_layout)
        
        # Info label for descriptions
        self.info_label = QLabel()
        self.info_label.setWordWrap(True)
        self.info_label.setStyleSheet("margin-top: 10px; padding: 8px; background-color: #f0f0f0; border-radius: 4px;")
        main_layout.addWidget(self.info_label)
        
        # Create all radio button groups
        self._create_radiobutton_groups()
        
        # Show the first style by default
        self.update_radiobutton_style(0)
    
    def _create_radiobutton_groups(self):
        """Create all radio button groups with different styles"""
        # 1. Basic Radio Button Style
        basic_group = QWidget()
        basic_layout = QVBoxLayout(basic_group)
        
        self.basic_radio1 = QRadioButton("Option 1")
        self.basic_radio2 = QRadioButton("Option 2")
        self.basic_radio3 = QRadioButton("Option 3")
        
        basic_style = """
            QRadioButton {
                color: #333333;
                font-size: 14px;
                spacing: 5px;
            }
            QRadioButton::indicator {
                width: 16px;
                height: 16px;
                border: 2px solid #CCCCCC;
                border-radius: 8px;
                background-color: white;
            }
            QRadioButton::indicator:checked {
                background-color: #2196F3;
                border-color: #2196F3;
            }
            QRadioButton::indicator:checked::after {
                content: "";
                position: absolute;
                width: 6px;
                height: 6px;
                border-radius: 3px;
                background-color: white;
                top: 5px;
                left: 5px;
            }
        """
        
        self.basic_radio1.setStyleSheet(basic_style)
        self.basic_radio2.setStyleSheet(basic_style)
        self.basic_radio3.setStyleSheet(basic_style)
        
        basic_layout.addWidget(self.basic_radio1)
        basic_layout.addWidget(self.basic_radio2)
        basic_layout.addWidget(self.basic_radio3)
        self.radiobutton_layout.addWidget(basic_group)
        
        # 2. Filled Circle Radio Button Style
        filled_group = QWidget()
        filled_layout = QVBoxLayout(filled_group)
        
        self.filled_radio1 = QRadioButton("Option A")
        self.filled_radio2 = QRadioButton("Option B")
        self.filled_radio3 = QRadioButton("Option C")
        
        filled_style = """
            QRadioButton {
                color: #333333;
                font-size: 14px;
                spacing: 5px;
            }
            QRadioButton::indicator {
                width: 18px;
                height: 18px;
                border: 2px solid #673AB7;
                border-radius: 9px;
                background-color: white;
            }
            QRadioButton::indicator:checked {
                background-color: #673AB7;
            }
            QRadioButton::indicator:checked::after {
                content: "✓";
                color: white;
                font-weight: bold;
                font-size: 12px;
                position: absolute;
                top: 1px;
                left: 4px;
            }
        """
        
        self.filled_radio1.setStyleSheet(filled_style)
        self.filled_radio2.setStyleSheet(filled_style)
        self.filled_radio3.setStyleSheet(filled_style)
        
        filled_layout.addWidget(self.filled_radio1)
        filled_layout.addWidget(self.filled_radio2)
        filled_layout.addWidget(self.filled_radio3)
        self.radiobutton_layout.addWidget(filled_group)
        
        # 3. Square Radio Button Style
        square_group = QWidget()
        square_layout = QVBoxLayout(square_group)
        
        self.square_radio1 = QRadioButton("Choice X")
        self.square_radio2 = QRadioButton("Choice Y")
        self.square_radio3 = QRadioButton("Choice Z")
        
        square_style = """
            QRadioButton {
                color: #333333;
                font-size: 14px;
                spacing: 5px;
            }
            QRadioButton::indicator {
                width: 18px;
                height: 18px;
                border: 2px solid #FF5722;
                border-radius: 2px;
                background-color: white;
            }
            QRadioButton::indicator:checked {
                background-color: #FF5722;
            }
            QRadioButton::indicator:checked::after {
                content: "";
                position: absolute;
                width: 10px;
                height: 6px;
                background-color: white;
                top: 4px;
                left: 3px;
                border-left: 2px solid white;
                border-bottom: 2px solid white;
                transform: rotate(-45deg);
            }
        """
        
        self.square_radio1.setStyleSheet(square_style)
        self.square_radio2.setStyleSheet(square_style)
        self.square_radio3.setStyleSheet(square_style)
        
        square_layout.addWidget(self.square_radio1)
        square_layout.addWidget(self.square_radio2)
        square_layout.addWidget(self.square_radio3)
        self.radiobutton_layout.addWidget(square_group)
        
        # 4. Neon Effect Radio Button Style
        neon_group = QWidget()
        neon_layout = QVBoxLayout(neon_group)
        
        self.neon_radio1 = QRadioButton("Option One")
        self.neon_radio2 = QRadioButton("Option Two")
        self.neon_radio3 = QRadioButton("Option Three")
        
        neon_style = """
            QRadioButton {
                color: #00BCD4;
                font-size: 14px;
                spacing: 5px;
            }
            QRadioButton::indicator {
                width: 20px;
                height: 20px;
                border: 2px solid #00BCD4;
                border-radius: 10px;
                background-color: #1A1A1A;
            }
            QRadioButton::indicator:checked {
                background-color: #00BCD4;
                box-shadow: 0 0 10px #00BCD4, 0 0 20px #00BCD4;
            }
            QRadioButton::indicator:checked::after {
                content: "";
                position: absolute;
                width: 10px;
                height: 10px;
                border-radius: 5px;
                background-color: #1A1A1A;
                top: 5px;
                left: 5px;
            }
        """
        
        self.neon_radio1.setStyleSheet(neon_style)
        self.neon_radio2.setStyleSheet(neon_style)
        self.neon_radio3.setStyleSheet(neon_style)
        
        neon_layout.addWidget(self.neon_radio1)
        neon_layout.addWidget(self.neon_radio2)
        neon_layout.addWidget(self.neon_radio3)
        self.radiobutton_layout.addWidget(neon_group)
        
        # 5. Flat Style Radio Button Style
        flat_group = QWidget()
        flat_layout = QVBoxLayout(flat_group)
        
        self.flat_radio1 = QRadioButton("Item 1")
        self.flat_radio2 = QRadioButton("Item 2")
        self.flat_radio3 = QRadioButton("Item 3")
        
        flat_style = """
            QRadioButton {
                color: #607D8B;
                font-size: 14px;
                spacing: 5px;
            }
            QRadioButton::indicator {
                width: 18px;
                height: 18px;
                border: 2px solid #CFD8DC;
                border-radius: 9px;
                background-color: white;
            }
            QRadioButton::indicator:checked {
                background-color: #26C6DA;
                border-color: #26C6DA;
            }
            QRadioButton::indicator:checked::after {
                content: "";
                position: absolute;
                width: 8px;
                height: 4px;
                background-color: white;
                top: 5px;
                left: 3px;
                border-left: 2px solid white;
                border-bottom: 2px solid white;
                transform: rotate(-45deg);
            }
        """
        
        self.flat_radio1.setStyleSheet(flat_style)
        self.flat_radio2.setStyleSheet(flat_style)
        self.flat_radio3.setStyleSheet(flat_style)
        
        flat_layout.addWidget(self.flat_radio1)
        flat_layout.addWidget(self.flat_radio2)
        flat_layout.addWidget(self.flat_radio3)
        self.radiobutton_layout.addWidget(flat_group)
        
        # 6. Colored Radio Button Style
        color_group = QWidget()
        color_layout = QVBoxLayout(color_group)
        
        self.color_radio1 = QRadioButton("Red Option")
        self.color_radio2 = QRadioButton("Green Option")
        self.color_radio3 = QRadioButton("Blue Option")
        
        # Red option
        color_red_style = """
            QRadioButton {
                color: #F44336;
                font-size: 14px;
                spacing: 5px;
            }
            QRadioButton::indicator {
                width: 16px;
                height: 16px;
                border: 2px solid #FFCDD2;
                border-radius: 8px;
                background-color: white;
            }
            QRadioButton::indicator:checked {
                background-color: #F44336;
                border-color: #F44336;
            }
        """
        
        # Green option
        color_green_style = """
            QRadioButton {
                color: #4CAF50;
                font-size: 14px;
                spacing: 5px;
            }
            QRadioButton::indicator {
                width: 16px;
                height: 16px;
                border: 2px solid #C8E6C9;
                border-radius: 8px;
                background-color: white;
            }
            QRadioButton::indicator:checked {
                background-color: #4CAF50;
                border-color: #4CAF50;
            }
        """
        
        # Blue option
        color_blue_style = """
            QRadioButton {
                color: #2196F3;
                font-size: 14px;
                spacing: 5px;
            }
            QRadioButton::indicator {
                width: 16px;
                height: 16px;
                border: 2px solid #BBDEFB;
                border-radius: 8px;
                background-color: white;
            }
            QRadioButton::indicator:checked {
                background-color: #2196F3;
                border-color: #2196F3;
            }
        """
        
        self.color_radio1.setStyleSheet(color_red_style)
        self.color_radio2.setStyleSheet(color_green_style)
        self.color_radio3.setStyleSheet(color_blue_style)
        
        color_layout.addWidget(self.color_radio1)
        color_layout.addWidget(self.color_radio2)
        color_layout.addWidget(self.color_radio3)
        self.radiobutton_layout.addWidget(color_group)
        
        # 7. Custom Size Radio Button Style
        size_group = QWidget()
        size_layout = QVBoxLayout(size_group)
        
        self.size_radio1 = QRadioButton("Small Size")
        self.size_radio2 = QRadioButton("Standard Size")
        self.size_radio3 = QRadioButton("Large Size")
        
        # Small size
        small_style = """
            QRadioButton {
                color: #333333;
                font-size: 12px;
                spacing: 4px;
            }
            QRadioButton::indicator {
                width: 12px;
                height: 12px;
                border: 1px solid #CCCCCC;
                border-radius: 6px;
                background-color: white;
            }
            QRadioButton::indicator:checked {
                background-color: #9C27B0;
                border-color: #9C27B0;
            }
        """
        
        # Standard size
        standard_style = """
            QRadioButton {
                color: #333333;
                font-size: 14px;
                spacing: 5px;
            }
            QRadioButton::indicator {
                width: 16px;
                height: 16px;
                border: 2px solid #CCCCCC;
                border-radius: 8px;
                background-color: white;
            }
            QRadioButton::indicator:checked {
                background-color: #9C27B0;
                border-color: #9C27B0;
            }
        """
        
        # Large size
        large_style = """
            QRadioButton {
                color: #333333;
                font-size: 16px;
                spacing: 6px;
            }
            QRadioButton::indicator {
                width: 24px;
                height: 24px;
                border: 2px solid #CCCCCC;
                border-radius: 12px;
                background-color: white;
            }
            QRadioButton::indicator:checked {
                background-color: #9C27B0;
                border-color: #9C27B0;
            }
            QRadioButton::indicator:checked::after {
                content: "";
                position: absolute;
                width: 12px;
                height: 12px;
                border-radius: 6px;
                background-color: white;
                top: 6px;
                left: 6px;
            }
        """
        
        self.size_radio1.setStyleSheet(small_style)
        self.size_radio2.setStyleSheet(standard_style)
        self.size_radio3.setStyleSheet(large_style)
        
        size_layout.addWidget(self.size_radio1)
        size_layout.addWidget(self.size_radio2)
        size_layout.addWidget(self.size_radio3)
        self.radiobutton_layout.addWidget(size_group)
        
        # 8. Icon Radio Button Style
        icon_group = QWidget()
        icon_layout = QVBoxLayout(icon_group)
        
        self.icon_radio1 = QRadioButton("Icon Option 1")
        self.icon_radio2 = QRadioButton("Icon Option 2")
        self.icon_radio3 = QRadioButton("Icon Option 3")
        
        icon_style = """
            QRadioButton {
                color: #333333;
                font-size: 14px;
                spacing: 8px;
                padding: 3px;
            }
            QRadioButton::indicator {
                width: 18px;
                height: 18px;
                border: 2px solid #FFC107;
                border-radius: 9px;
                background-color: white;
            }
            QRadioButton::indicator:checked {
                background-color: #FFC107;
                border-color: #FFC107;
            }
        """
        
        self.icon_radio1.setStyleSheet(icon_style)
        self.icon_radio2.setStyleSheet(icon_style)
        self.icon_radio3.setStyleSheet(icon_style)
        
        # For simplicity, icons are not actually added here, but in a real application you could use:
        # icon = QIcon("path/to/icon.png")
        # self.icon_radio1.setIcon(icon)
        # self.icon_radio1.setIconSize(QSize(16, 16))
        
        icon_layout.addWidget(self.icon_radio1)
        icon_layout.addWidget(self.icon_radio2)
        icon_layout.addWidget(self.icon_radio3)
        self.radiobutton_layout.addWidget(icon_group)
    
    def update_radiobutton_style(self, index):
        """Update the displayed radio button group style based on selection"""
        # Hide all radio button groups
        for i in range(self.radiobutton_layout.count()):
            widget = self.radiobutton_layout.itemAt(i).widget()
            if widget:
                widget.hide()
        
        # Show the selected radio button group
        selected_group = self.radiobutton_layout.itemAt(index).widget()
        if selected_group:
            selected_group.show()
        
        # Update description information
        descriptions = [
            "Basic radio buttons use a standard circular design with simple borders and fill effects.",
            "Filled circle radio buttons show a complete fill effect when selected, with a check mark.",
            "Square radio buttons use square indicators, creating a different visual effect.",
            "Neon effect radio buttons use glowing effects, creating a high-tech interface.",
            "Flat style radio buttons adopt modern flat design, clean and clear.",
            "Colored radio buttons set different colors for different options, improving visual distinction.",
            "Custom size radio buttons demonstrate how to adjust the size of radio buttons.",
            "Icon radio buttons can display custom icons before the text."
        ]
        self.info_label.setText(descriptions[index])
    
    def reset_selection(self):
        """Reset the selection state of all radio buttons"""
        if self.reset_btn.isChecked():
            # Reset all radio buttons
            radiobuttons = [
                self.basic_radio1, self.basic_radio2, self.basic_radio3,
                self.filled_radio1, self.filled_radio2, self.filled_radio3,
                self.square_radio1, self.square_radio2, self.square_radio3,
                self.neon_radio1, self.neon_radio2, self.neon_radio3,
                self.flat_radio1, self.flat_radio2, self.flat_radio3,
                self.color_radio1, self.color_radio2, self.color_radio3,
                self.size_radio1, self.size_radio2, self.size_radio3,
                self.icon_radio1, self.icon_radio2, self.icon_radio3
            ]
            
            for radio in radiobuttons:
                radio.setAutoExclusive(False)
                radio.setChecked(False)
                radio.setAutoExclusive(True)
            
            # Uncheck the reset button after operation
            self.reset_btn.setChecked(False)

# Launch function
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RadioButtonStylesWindow()
    window.show()
    sys.exit(app.exec())