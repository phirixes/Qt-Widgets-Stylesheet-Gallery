#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
QSS Global Stylesheet Example
This example demonstrates the application of global stylesheets in PySide6
and the usage of various selectors.
"""

import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QPushButton, QLabel, QLineEdit, QComboBox, QCheckBox, QGroupBox,
    QTabWidget, QTextEdit, QGridLayout
)
from PySide6.QtCore import Qt

class GlobalStylesWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Global Stylesheet Example')
        self.setGeometry(100, 100, 800, 600)
        
        # Create main widget and layout
        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)
        
        # Create tab widget
        self.tab_widget = QTabWidget()
        
        # Add tabs
        self.tab_widget.addTab(self.create_global_styles_tab(), 'Global Styles')
        self.tab_widget.addTab(self.create_cascade_styles_tab(), 'Style Cascade')
        self.tab_widget.addTab(self.create_custom_classes_tab(), 'Custom Classes & IDs')
        self.tab_widget.addTab(self.create_pseudo_states_tab(), 'Pseudo States')
        
        # Add tab widget to main layout
        main_layout.addWidget(self.tab_widget)
        
        # Set central widget
        self.setCentralWidget(main_widget)
    
    def create_global_styles_tab(self):
        """Create the tab for global styles demonstration"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Add title label
        title = QLabel('Global Stylesheet Demonstration')
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet('font-size: 18px; font-weight: bold; margin-bottom: 20px;')
        layout.addWidget(title)
        
        # Create a widget grid to display various styled widgets
        widgets_grid = QGridLayout()
        
        # Add QPushButton
        btn_label = QLabel('QPushButton:')
        button = QPushButton('Click Me')
        widgets_grid.addWidget(btn_label, 0, 0)
        widgets_grid.addWidget(button, 0, 1)
        
        # Add QLabel
        label_label = QLabel('QLabel:')
        sample_label = QLabel('This is a sample label')
        widgets_grid.addWidget(label_label, 1, 0)
        widgets_grid.addWidget(sample_label, 1, 1)
        
        # Add QLineEdit
        lineedit_label = QLabel('QLineEdit:')
        lineedit = QLineEdit()
        lineedit.setPlaceholderText('Enter text here')
        widgets_grid.addWidget(lineedit_label, 2, 0)
        widgets_grid.addWidget(lineedit, 2, 1)
        
        # Add QComboBox
        combobox_label = QLabel('QComboBox:')
        combobox = QComboBox()
        combobox.addItems(['Option 1', 'Option 2', 'Option 3'])
        widgets_grid.addWidget(combobox_label, 3, 0)
        widgets_grid.addWidget(combobox, 3, 1)
        
        # Add QCheckBox
        checkbox_label = QLabel('QCheckBox:')
        checkbox = QCheckBox('Check this option')
        widgets_grid.addWidget(checkbox_label, 4, 0)
        widgets_grid.addWidget(checkbox, 4, 1)
        
        # Add QGroupBox
        groupbox_label = QLabel('QGroupBox:')
        groupbox = QGroupBox('Group Title')
        groupbox_layout = QVBoxLayout()
        groupbox_layout.addWidget(QLabel('Content inside the group'))
        groupbox.setLayout(groupbox_layout)
        widgets_grid.addWidget(groupbox_label, 5, 0)
        widgets_grid.addWidget(groupbox, 5, 1)
        
        # Add QTextEdit
        textedit_label = QLabel('QTextEdit:')
        textedit = QTextEdit()
        textedit.setPlaceholderText('Enter multiple lines of text here...')
        textedit.setMaximumHeight(80)
        widgets_grid.addWidget(textedit_label, 6, 0)
        widgets_grid.addWidget(textedit, 6, 1)
        
        # Add grid layout to main layout
        layout.addLayout(widgets_grid)
        layout.addStretch()
        
        return tab
    
    def create_cascade_styles_tab(self):
        """Create the tab for style cascade demonstration"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Add title label
        title = QLabel('Style Cascade Demonstration')
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet('font-size: 18px; font-weight: bold; margin-bottom: 20px;')
        layout.addWidget(title)
        
        # Create explanation label
        explanation = QLabel(
            'This demonstrates the cascading nature of stylesheets.\n'
            'Styles defined in parent widgets can be inherited by child widgets,\n'
            'but can also be overridden by more specific styles.'
        )
        explanation.setWordWrap(True)
        layout.addWidget(explanation)
        
        # Create a container widget with custom style
        container = QWidget()
        container.setStyleSheet(
            'background-color: #E3F2FD; border: 1px solid #2196F3; border-radius: 8px; padding: 10px;'
        )
        container_layout = QVBoxLayout(container)
        
        # Add widgets to the container
        container_layout.addWidget(QLabel('Widgets inside styled container:'))
        
        # Button that inherits style
        default_button = QPushButton('Default Style Button')
        container_layout.addWidget(default_button)
        
        # Button with overridden style
        custom_button = QPushButton('Custom Style Button')
        custom_button.setStyleSheet(
            'background-color: #FF9800; color: white; border-radius: 4px;'
        )
        container_layout.addWidget(custom_button)
        
        # Add container to main layout
        layout.addWidget(container)
        layout.addStretch()
        
        return tab
    
    def create_custom_classes_tab(self):
        """Create the tab for custom classes and IDs demonstration"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Add title label
        title = QLabel('Custom Classes & IDs Demonstration')
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet('font-size: 18px; font-weight: bold; margin-bottom: 20px;')
        layout.addWidget(title)
        
        # Create explanation label
        explanation = QLabel(
            'This demonstrates how to use custom IDs and attribute selectors\n'
            'to apply specific styles to widgets.'
        )
        explanation.setWordWrap(True)
        layout.addWidget(explanation)
        
        # Create button layout
        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(10)
        
        # Create buttons with different IDs and attributes
        special_button = QPushButton('Special Button')
        special_button.setObjectName('specialButton')
        
        danger_button = QPushButton('Danger Button')
        danger_button.setObjectName('dangerButton')
        
        primary_button = QPushButton('Primary Button')
        primary_button.setProperty('class', 'primary')
        
        secondary_button = QPushButton('Secondary Button')
        secondary_button.setProperty('class', 'secondary')
        
        large_primary_button = QPushButton('Large Primary')
        large_primary_button.setProperty('class', 'primary large')
        
        # Add buttons to layout
        buttons_layout.addWidget(special_button)
        buttons_layout.addWidget(danger_button)
        buttons_layout.addWidget(primary_button)
        buttons_layout.addWidget(secondary_button)
        buttons_layout.addWidget(large_primary_button)
        
        # Add buttons layout to main layout
        layout.addLayout(buttons_layout)
        layout.addStretch()
        
        return tab
    
    def create_pseudo_states_tab(self):
        """Create the tab for pseudo-states demonstration"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Add title label
        title = QLabel('Pseudo-States Demonstration')
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet('font-size: 18px; font-weight: bold; margin-bottom: 20px;')
        layout.addWidget(title)
        
        # Create explanation label
        explanation = QLabel(
            'This demonstrates how to style widgets based on their states.\n'
            'Hover over, click, or interact with the widgets below to see the effects.'
        )
        explanation.setWordWrap(True)
        layout.addWidget(explanation)
        
        # Create interactive widgets section
        interactive_section = QGroupBox('Interactive Widgets')
        interactive_layout = QVBoxLayout(interactive_section)
        
        # Add widgets that demonstrate pseudo-states
        button_layout = QHBoxLayout()
        normal_button = QPushButton('Normal Button')
        disabled_button = QPushButton('Disabled Button')
        disabled_button.setEnabled(False)
        button_layout.addWidget(normal_button)
        button_layout.addWidget(disabled_button)
        
        lineedit_layout = QHBoxLayout()
        lineedit_label = QLabel('Focus on this line edit:')
        focus_lineedit = QLineEdit()
        focus_lineedit.setPlaceholderText('Click here to focus')
        lineedit_layout.addWidget(lineedit_label)
        lineedit_layout.addWidget(focus_lineedit)
        
        checkbox_layout = QHBoxLayout()
        checkbox_label = QLabel('Check/uncheck this box:')
        toggle_checkbox = QCheckBox()
        checkbox_layout.addWidget(checkbox_label)
        checkbox_layout.addWidget(toggle_checkbox)
        
        # Add layouts to interactive section
        interactive_layout.addLayout(button_layout)
        interactive_layout.addLayout(lineedit_layout)
        interactive_layout.addLayout(checkbox_layout)
        
        # Add interactive section to main layout
        layout.addWidget(interactive_section)
        layout.addStretch()
        
        return tab


# Setup global stylesheet function
def setup_global_stylesheet(app):
    """Setup global stylesheet for the application"""
    global_stylesheet = """
    /* QMainWindow style */
    QMainWindow {
        background-color: #F5F5F5;
    }
    
    /* QWidget style */
    QWidget {
        background-color: transparent;
    }
    
    /* QPushButton basic style */
    QPushButton {
        background-color: #2196F3;
        color: white;
        border: none;
        border-radius: 4px;
        padding: 6px 12px;
        font-size: 14px;
    }
    QPushButton:hover {
        background-color: #1976D2;
    }
    QPushButton:pressed {
        background-color: #1565C0;
    }
    QPushButton:disabled {
        background-color: #BDBDBD;
        color: #757575;
    }
    
    /* QLabel style */
    QLabel {
        color: #333333;
        font-size: 14px;
    }
    
    /* QLineEdit style */
    QLineEdit {
        background-color: white;
        color: #333333;
        border: 1px solid #CCCCCC;
        border-radius: 4px;
        padding: 5px;
        font-size: 14px;
    }
    QLineEdit:hover {
        border-color: #999999;
    }
    QLineEdit:focus {
        border-color: #2196F3;
        background-color: #F5F5F5;
    }
    QLineEdit:disabled {
        background-color: #F5F5F5;
        color: #BDBDBD;
        border-color: #E0E0E0;
    }
    
    /* QComboBox style */
    QComboBox {
        background-color: white;
        color: #333333;
        border: 1px solid #CCCCCC;
        border-radius: 4px;
        padding: 5px;
        font-size: 14px;
    }
    QComboBox:hover {
        border-color: #999999;
    }
    QComboBox:focus {
        border-color: #2196F3;
    }
    QComboBox::drop-down {
        border-left: 1px solid #CCCCCC;
    }
    
    /* QCheckBox style */
    QCheckBox {
        color: #333333;
        font-size: 14px;
    }
    QCheckBox::indicator {
        width: 16px;
        height: 16px;
        border: 1px solid #CCCCCC;
        border-radius: 3px;
        background-color: white;
    }
    QCheckBox::indicator:checked {
        background-color: #2196F3;
        border-color: #2196F3;
    }
    
    /* QGroupBox style */
    QGroupBox {
        border: 1px solid #DDDDDD;
        border-radius: 4px;
        margin-top: 10px;
        padding: 10px;
        color: #333333;
        font-weight: bold;
    }
    QGroupBox::title {
        subcontrol-origin: margin;
        subcontrol-position: top left;
        padding: 0 5px;
        background-color: #F5F5F5;
    }
    
    /* QTabWidget style */
    QTabWidget::pane {
        border: 1px solid #CCCCCC;
        background-color: white;
        border-radius: 4px;
    }
    QTabBar::tab {
        background-color: #E0E0E0;
        color: #333333;
        border: 1px solid #CCCCCC;
        border-bottom: none;
        border-top-left-radius: 4px;
        border-top-right-radius: 4px;
        padding: 8px 16px;
        margin-right: 2px;
    }
    QTabBar::tab:selected {
        background-color: white;
        color: #2196F3;
        font-weight: bold;
    }
    
    /* QTextEdit style */
    QTextEdit {
        background-color: white;
        color: #333333;
        border: 1px solid #CCCCCC;
        border-radius: 4px;
        padding: 5px;
        font-size: 14px;
    }
    QTextEdit:read-only {
        background-color: #F5F5F5;
        color: #757575;
    }
    
    /* Custom ID selectors */
    QPushButton#specialButton {
        background-color: #4CAF50;
        font-weight: bold;
    }
    QPushButton#dangerButton {
        background-color: #F44336;
    }
    
    /* Custom attribute selectors */
    QPushButton[class="primary"] {
        background-color: #2196F3;
        border: 2px solid #1976D2;
    }
    QPushButton[class="secondary"] {
        background-color: #607D8B;
    }
    QPushButton[class="primary large"] {
        background-color: #2196F3;
        font-size: 16px;
        padding: 10px 20px;
    }
    """
    
    # Apply global stylesheet
    app.setStyleSheet(global_stylesheet)

# Startup function
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Set up global stylesheet
    setup_global_stylesheet(app)
    
    window = GlobalStylesWindow()
    window.show()
    sys.exit(app.exec())